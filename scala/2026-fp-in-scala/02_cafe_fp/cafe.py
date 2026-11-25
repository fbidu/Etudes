from dataclasses import dataclass

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

class Cafe:
    @staticmethod
    def buy_coffee(cc: CreditCard) -> tuple[Coffee, Charge]:
        cup = Coffee()
        return (cup, Charge(cc, cup.price))

if __name__ == "__main__":
    card = CreditCard()
    cafe = Cafe()
    cup = cafe.buy_coffee(card)
    print(cup)