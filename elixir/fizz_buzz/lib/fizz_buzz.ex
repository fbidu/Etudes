defmodule FizzBuzz do
  def build(file_name) do
    file_name
    |> File.read()
    |> handle_file_read()
  end

  defp handle_file_read({:ok, result}) do
    result = result
      |> String.split(",")
      |> Enum.map(&convert_and_evaluate/1)

    {:ok, result}
  end

  defp handle_file_read({:error, reason}), do: {:error, "Error reading the file: #{reason}"}

  defp convert_and_evaluate(elem) do
    elem
    |> String.to_integer
    |> evaluate
  end

  defp evaluate(elem) when rem(elem, 15) == 0, do: :fizzbuzz
  defp evaluate(elem) when rem(elem, 3) == 0, do: :fizz
  defp evaluate(elem) when rem(elem, 5) == 0, do: :buzz
  defp evaluate(elem), do: elem
end
