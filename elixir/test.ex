defmodule Mat do
    def is_even?(n) do
        rem(n, 2) == 0
    end

    def is_odd?(n) do
        not Mat.is_even?(n)
    end
end

defmodule Greeters do
    def greet(name, greeting \\ "Hello") do
        "#{greeting}, #{name}"
    end
end
