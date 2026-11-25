class Cafe:
  def buyCoffee(cc: CreditCard): (Coffee, Charge) =
    val cup = Coffee()
    (cup, Charge(cc, cup.price))

  def buyCoffees(cc: CreditCard, n: Int): (List[Coffee], Charge) =
    val purchases: List[(Coffee, Charge)] = List.fill(n)(buyCoffee(cc))
    val (coffees, charges) = purchases.unzip
    var charge = charges.reduce(_.combine(_))
    (coffees, charge)

class CreditCard:
  def charge(price: Double): Unit =
    println("charging " + price)

class Coffee:
  val price: Double = 2.0

case class Charge(cc: CreditCard, amount: Double):
  def combine(other: Charge): Charge =
    if (cc == other.cc) then Charge(cc, amount + other.amount)
    else throw Exception("Can't combine charges of different CCs")

// "Companion Object" to Charge to expose `Charge.coalesce`
// ref:https://docs.scala-lang.org/scala3/book/domain-modeling-tools.html#companion-objects
object Charge:
  def coalesce(charges: List[Charge]): List[Charge] =
    /* Combine charges made to the same credit cards */
    val final_charges = charges.groupBy(_.cc).values.map(_.reduce(_.combine(_)))
    final_charges.toList

@main def run(): Unit =
  val cc = CreditCard()
  val cafe = Cafe()
  val cup = cafe.buyCoffee(cc)
  println(cup)

  println("Buying 10 coffees")
  val result = cafe.buyCoffees(cc, 10)
  println(result)
  println(result._1.length)

  println("Testing charge coalescing")
  val cc1 = CreditCard()
  val cc2 = CreditCard()
  val (_, c1) = cafe.buyCoffee(cc1)
  val (_, c2) = cafe.buyCoffee(cc1)
  val (_, c3) = cafe.buyCoffee(cc1)
  val (_, c4) = cafe.buyCoffee(cc2)
  val (_, c5) = cafe.buyCoffee(cc2)
  val charges = Charge.coalesce(List(c1, c2, c3, c4, c5))
  println(charges)
