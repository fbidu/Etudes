defmodule FizzBuzzTest do
  use ExUnit.Case

  describe "build/1" do
    test "when a valid file is provided, returns a correct converted list" do
      expected = {:ok, [1, 2, :fizz, 4, :buzz, :buzz, :fizzbuzz, :buzz]}
      assert FizzBuzz.build("numbers.txt") == expected
    end

    test "when an invalid file is provided, returns a nice error" do
      expected = {:error, "Error reading the file: enoent"}
      assert FizzBuzz.build("invalid.txt") == expected
    end
  end
end
