class Cafe:
  def buyCoffee(cc: CreditCard, p: Payments): Coffee =
    val cup = Coffee()
    p.charge(cc, cup.price)
    cup

class CreditCard:
  def charge(price: Double): Unit =
    println("charging " + price)

class Coffee:
  val price: Double = 2.0

trait Payments:
  def charge(cc: CreditCard, price: Double): Unit

class SimulatedPayments extends Payments:
  def charge(cc: CreditCard, price: Double): Unit =
    println("Charging " + price + " to " + cc)

@main def run(): Unit =
  val cc = CreditCard()
  val cafe = Cafe()
  val p = SimulatedPayments()
  val cup = cafe.buyCoffee(cc, p)
