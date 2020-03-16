defmodule Toolshed do
  @moduledoc """
  Documentation for `Toolshed`.
  """

  @doc """
  Checks if an integer is even.

  ## Parameters
    - n: The integer to be tested

  ## Examples
    iex> Toolshed.is_even?(2)
    true

    iex> Toolshed.is_even?(3)
    false
  """
  @spec is_even?(integer) :: boolean
  def is_even?(n) do
    rem(n, 2) == 0
  end

  @doc """
  Sorts a string's characters

  ## Parameters
    - str: The string to be sorted

  ## Examples
    iex> Toolshed.sort_str("bcabca")
    ["a", "a", "b", "b", "c", "c"]
  """
  @spec sort_str(String.t()) :: List.t()
  def sort_str(str) do
    str
    |> String.downcase
    |> String.graphemes
    |> Enum.sort
  end


end
