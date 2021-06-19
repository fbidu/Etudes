import pytest

pytestmark = pytest.mark.django_db

from .factories import CheeseFactory


def test__str__():
    cheese = CheeseFactory()

    assert cheese.__str__() == cheese.name
    assert str(cheese) == cheese.name


def test_cheese_has_country():
    cheese = CheeseFactory()

    assert cheese.country_of_origin


def test_cheese_has_creator():
    cheese = CheeseFactory()

    assert cheese.creator