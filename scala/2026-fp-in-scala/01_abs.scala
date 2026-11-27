/*
Given a number, return its abs
 */

object MyProgram:
  def abs(n: Double): Double =
    if (n <= 0) then -n
    else n
@main
def main() =
  println(MyProgram.abs(42))
  println(MyProgram.abs(-42))
  println(MyProgram.abs(-0))
  println(MyProgram.abs(-12141341.023443))
