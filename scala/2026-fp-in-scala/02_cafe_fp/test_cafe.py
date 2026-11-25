from cafe import Charge, CreditCard


def test_coalesce_merges_non_adjacent_charges_to_the_same_card() -> None:
    """
    Scala's `groupBy` groups charges by card wherever they sit in the list.
    A customer who pays with card A, then B, then A again must end up with
    one charge on A, not one charge per run of consecutive A charges.
    """
    # Setup
    card_a = CreditCard()
    card_b = CreditCard()
    assert card_a != card_b  # sanity check: cards compare by identity

    # Act
    charges = Charge.coalesce(
        [Charge(card_a, 2.0), Charge(card_b, 2.0), Charge(card_a, 2.0)]
    )

    # Assert
    assert len(charges) == 2
    assert Charge(card_a, 4.0) in charges
    assert Charge(card_b, 2.0) in charges
