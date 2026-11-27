/*
Given a number, return its abs
 */

object MyProgram:
  /*
  Curly braces are optional but supported
   */
  def abs(n: Double): Double = {
    if n <= 0 then -n
    else n
  }

  private def formatAbs(n: Double): String =
    val msg = "The absolute value of %f is %f"
    /*
    Optional, last statement is always `return`ed.
    When used, the return type must be declared
     */
    return msg.format(n, abs(n))

  /*
  "Outer, inpure shell" that has side effects.
  Those are sometimes called "procedures" to separate
  from functions, which are supposed to be "pure"
   */
  @main def printAbs()
      : Unit = // Unit == `none` in Python. Used generaly in "procedures"
    println(abs(42))
    println(abs(-42))
    println(formatAbs(-0))
    println(formatAbs(-12141341.023443))
    () // This is the actual and only "Unit". Optional.
