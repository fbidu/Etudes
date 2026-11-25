class Cafe:
  def buyCoffee(cc: CreditCard): (Coffee, Charge) =
    val cup = Coffee()
    (cup, Charge(cc, cup.price))

  def buyCoffees(cc: CreditCard, n: Int): (List[Coffee], Charge) =
    var coffees = List[Coffee]()
    var charge = Charge(cc, 0)
    for (i <- 1 to n) do
      val cup = buyCoffee(cc)
      charge = charge.combine(cup._2)
      coffees = coffees.appended(cup._1)
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
