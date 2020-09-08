defmodule FizzBuzz do
  def build(file_name) do
    file_name
    |> File.read()
    |> handle_file_read()
  end

  def handle_file_read({:ok, result}) do
    result
    |> String.split(",")
    |> Enum.map(&convert_and_evaluate/1)
  end

  def handle_file_read({:error, reason}), do: "Error reading the file: #{reason}"

  def convert_and_evaluate(elem) do
    elem
    |> String.to_integer
    |> evaluate
  end

  def evaluate(elem) when rem(elem, 15) == 0, do: :fizzbuzz 
  def evaluate(elem) when rem(elem, 3) == 0, do: :fizz
  def evaluate(elem) when rem(elem, 5) == 0, do: :buzz
  def evaluate(elem), do: elem
end
