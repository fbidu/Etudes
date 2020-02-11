defmodule ToolshedTest do
  use ExUnit.Case
  doctest Toolshed

  test "greets the world" do
    assert Toolshed.hello() == :world
  end
end
