import pytest

pytestmark = pytest.mark.django_db

from ..models import Cheese


def test__str__():
    cheese = Cheese.objects.create(
        name="Branco",
        description="Brazilian white fresh soft cheese",
        firmness=Cheese.Firmness.SOFT,
    )

    assert cheese.__str__() == "Branco"
    assert str(cheese) == "Branco"