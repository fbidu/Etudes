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

@main def run(): Unit =
  val cc = CreditCard()
  val cafe = Cafe()
  val cup = cafe.buyCoffee(cc)
  println(cup)

  println("Buying 10 coffees")
  val result = cafe.buyCoffees(cc, 10)
  println(result)
  println(result._1.length)
