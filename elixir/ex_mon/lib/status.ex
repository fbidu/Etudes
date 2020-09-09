defmodule ExMon.Status do
  alias ExMon.Game
  def print_round_message do
    IO.puts("THE GAME")
    IO.inspect(Game.info)
    IO.puts("---------------------")
  end
end
