from dataclasses import dataclass
from functools import reduce
class CreditCard:
    def charge(self, price: float) -> None:
        print(f"Charging {price}")

@dataclass(frozen=True)
class Coffee:
    price: float = 2

@dataclass(frozen=True)
class Charge:
    credit_card: CreditCard
    amount: float

    def __add__(self, other: Charge) -> Charge:
        if (self.credit_card == other.credit_card):
            return Charge(self.credit_card, self.amount + other.amount)
        else:
            raise ValueError("Can't combine charges of different credit cards")

class Cafe:
    @staticmethod
    def buy_coffee(cc: CreditCard) -> tuple[Coffee, Charge]:
        cup = Coffee()
        return (cup, Charge(cc, cup.price))

    @staticmethod
    def buy_coffees(cc: CreditCard, n: int) -> tuple[list[Coffee], Charge]:
        purchases = [Cafe.buy_coffee(cc) for _ in range(n)]
        coffees: list[Coffee] = [p[0] for p in purchases]
        charges: list[Charge] = [p[1] for p in purchases]
        charge = reduce(lambda a, b: a + b, charges)
        return (coffees, charge)

if __name__ == "__main__":
    card = CreditCard()
    cafe = Cafe()
    cup = cafe.buy_coffee(card)
    print(cup)

    print("Buying 10 coffees")
    result = cafe.buy_coffees(card, 10)
    print(result)
