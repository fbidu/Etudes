import 'dart:math';

void benchmark(String option, [size = 10000, max = 10000]) {
  var generator = Random();
  var data;
  switch (option.toUpperCase()) {
    case "LIST":
      data = [for (var i = 0; i < size; i++) generator.nextInt(max)];
      break;
    case "SET":
      data = {for (var i = 0; i < size; i++) generator.nextInt(max)};
  }

  for (var i = 0; i < max; i++) {
    data.contains(generator.nextInt(max));
  }
}
void main(args) {
  benchmark(args[0]);
}
