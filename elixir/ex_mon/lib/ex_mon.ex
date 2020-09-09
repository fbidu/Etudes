defmodule ExMon do
  def create_player(name, move_rnd, move_avg, move_heal) do
    ExMon.Player.build(name, move_rnd, move_avg, move_heal)
  end

  def start_game(player) do
    "Robotinikkkk"
    |> create_player(:punch, :kink, :heal)
    |> ExMon.Game.start(player)
  end
end
