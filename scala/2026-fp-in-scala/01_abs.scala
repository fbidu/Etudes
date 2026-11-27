/*
Given a number, return its abs
 */

object MyProgram:
  def abs(n: Double): Double =
    if n <= 0 then -n
    else n

  private def formatAbs(n: Double) =
    val msg = "The absolute value of %f is %f"
    msg.format(n, abs(n))

  @main def printAbs() =
    println(abs(42))
    println(abs(-42))
    println(formatAbs(-0))
    println(formatAbs(-12141341.023443))
