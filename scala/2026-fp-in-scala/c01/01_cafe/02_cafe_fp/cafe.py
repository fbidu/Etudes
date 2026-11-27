from __future__ import annotations

import operator
from collections import defaultdict
from dataclasses import dataclass
from functools import reduce


class CreditCard:
    def charge(self, price: float) -> None:
        print(f"Charging {price}")


@dataclass(frozen=True)
class Coffee:
    price: float = 2.0


@dataclass(frozen=True)
class Charge:
    credit_card: CreditCard
    amount: float

    def __add__(self, other: Charge) -> Charge:
        if self.credit_card == other.credit_card:
            return Charge(self.credit_card, self.amount + other.amount)

        raise ValueError("Can't combine charges of different credit cards")

    @staticmethod
    def coalesce(charges: list[Charge]) -> list[Charge]:
        """
        Takes a list of charges, groups them by credit card
        and returns a list of the final charges to each card.
        """
        charges_per_cc: dict[CreditCard, list[Charge]] = defaultdict(list)
        for charge in charges:
            charges_per_cc[charge.credit_card].append(charge)

        return [
            reduce(operator.add, cc_charges) for cc_charges in charges_per_cc.values()
        ]


class Cafe:
    @staticmethod
    def buy_coffee(cc: CreditCard) -> tuple[Coffee, Charge]:
        cup = Coffee()
        return (cup, Charge(cc, cup.price))

    @staticmethod
    def buy_coffees(cc: CreditCard, n: int) -> tuple[list[Coffee], Charge]:
        purchases = [Cafe.buy_coffee(cc) for _ in range(n)]
        coffees = [p[0] for p in purchases]
        charges = [p[1] for p in purchases]
        charge = reduce(operator.add, charges)
        return (coffees, charge)


if __name__ == "__main__":
    card = CreditCard()
    cafe = Cafe()
    cup = cafe.buy_coffee(card)
    print(cup)

    print("Buying 10 coffees")
    result = cafe.buy_coffees(card, 10)
    print(result)
    print(len(result[0]))

    print("Testing charge coalescing")
    cc1 = CreditCard()
    cc2 = CreditCard()
    _, p1 = cafe.buy_coffee(cc1)
    _, p2 = cafe.buy_coffee(cc1)
    _, p3 = cafe.buy_coffee(cc1)
    _, p4 = cafe.buy_coffee(cc2)
    _, p5 = cafe.buy_coffee(cc2)
    charges = Charge.coalesce([p1, p2, p3, p4, p5])
    print(charges)
