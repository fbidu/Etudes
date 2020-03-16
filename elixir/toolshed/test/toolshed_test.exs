defmodule ToolshedTest do
  use ExUnit.Case
  doctest Toolshed

  test "is even" do
    assert Toolshed.is_even?(2)
    assert Toolshed.is_even?(4)
    assert Toolshed.is_even?(80)
    assert Toolshed.is_even?(20)
    assert Toolshed.is_even?(0)
    assert Toolshed.is_even?(-4)
  end
end
