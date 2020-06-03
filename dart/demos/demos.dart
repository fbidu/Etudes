int add(a, b) => a + b;
int multiply(a, b) => a * b;

int fibonnaci(n, [log=false]) {
  if (log) {
    print("Fib invoked for ${n}");
  }
  if (n < 0) {
    throw Exception("n must be > 0!");
  }

  if (n == 0) {
    return 0;
  }

  if (n == 1) {
    return 1;
  }

  return fibonnaci(n - 1) + fibonnaci(n - 2);
}

var cache = {0: 0, 1: 1, 2: 1};

int fib_cached(n) {
  if (cache.containsKey(n)) {
    print("Returning from cache!");
    return cache[n];
  }

  print("Cache ${cache} does not contain the key ${n}");

  int fib = fib_cached(n - 1) + fib_cached(n - 2);
  cache[n] = fib;

  return fib;
}

sep() => print("-*-*" * 20);

main(List<String> args) {
  print("Hey");
  print("20 + 30 = ${add(20, 30)}");
  print("20 * 30 = ${multiply(20, 30)}");

  sep();

  print("Computing Fibonnaci with recursion");
  for (var i = 0; i < 10; i++) {
    print("Fib(${i}) = ${fibonnaci(i)}");
  }

  sep();

  print("Computing Fibonnaci with cached recursion");
  for (var i = 0; i < 10; i++) {
    print("Fib(${i}) = ${fib_cached(i)}");
  }

  sep();

  print("The cache state is $cache");
  print(
      "Cache has the key 0? ${cache.containsKey(0)}. Its value is ${cache[0]}");

  sep();

  try {
    print("Try catch with `catch (Exception)`");
    fibonnaci(-10);
    print("This expression is never reached");
  } catch (Exception) {
    print("Got an error, as expected!");
  }

  sep();

  try {
    print("Try catch with `catch (e)`");
    fibonnaci(-10);
    print("This expression is never reached");
  } catch (e) {
    print("Got an error, as expected!");
    print("The error is \"$e\"");
  }

  sep();

  try {
    print("Try catch with `on Exception`");
    fibonnaci(-10);
    print("This expression is never reached");
  } on Exception {
    print("Got an error, as expected!");
  }

  sep();

  try {
    print("Try catch with `on Exception catch (e)`");
    fibonnaci(-10);
    print("This expression is never reached");
  } on Exception catch (e) {
    print("Got an error, as expected!");
    print("The exception was \"$e\"");
  }
}
