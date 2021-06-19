import pytest
from pytest_django.asserts import assertContains
from django.urls import reverse
from .factories import CheeseFactory
from .factories import UserFactory
from ..models import Cheese
from ..views import CheeseListView, CheeseDetailView

pytestmark = pytest.mark.django_db


@pytest.fixture
def user():
    return UserFactory()


def test_good_cheese_list_view_expanded(rf):
    # Determine the URL
    url = reverse("cheeses:list")
    # rf is pytest shortcut to django.test.RequestFactory
    # We generate a request as if from a user accessing
    # the cheese list view
    request = rf.get(url)
    # Call as_view() to make a callable object
    # callable_obj is analogous to a function-based view
    callable_obj = CheeseListView.as_view()
    # Pass in the request into the callable_obj to get an
    # HTTP response served up by Django
    response = callable_obj(request)
    # Test that the HTTP response has 'Cheese List' in the
    # HTML and has a 200 response code
    assertContains(response, "Cheese List")


def test_good_cheese_list_view(rf):
    # Get the request
    request = rf.get(reverse("cheeses:list"))
    # Use the request to get the response
    response = CheeseListView.as_view()(request)
    # Test that the response is valid
    assertContains(response, "Cheese List")


def test_good_cheese_detail_view(rf):
    # Order some cheese from the CheeseFactory
    cheese = CheeseFactory()
    # Make a request for our new cheese
    url = cheese.get_absolute_url()
    request = rf.get(url)
    # Use the request to get the response
    callable_obj = CheeseDetailView.as_view()
    response = callable_obj(request, slug=cheese.slug)
    # Test that the response is valid
    assertContains(response, cheese.name)


def test_good_cheese_create_view(client, user):
    # Make the client authenticate
    client.force_login(user)
    # Specify the URL of the view
    url = reverse("cheeses:add")
    # Use the client to make the request
    response = client.get(url)
    # Test that the response is valid
    assert response.status_code == 200


def test_cheese_list_contains_cheese(rf):
    cheese_1 = CheeseFactory()
    cheese_2 = CheeseFactory()

    request = rf.get(reverse("cheeses:list"))
    response = CheeseListView.as_view()(request)

    assertContains(response, cheese_1.name)
    assertContains(response, cheese_2.name)


def test_detail_contains_cheese_data(rf):
    cheese = CheeseFactory()
    request = rf.get(cheese.get_absolute_url())
    callable_obj = CheeseDetailView.as_view()
    response = callable_obj(request, slug=cheese.slug)

    assertContains(response, cheese.name)
    assertContains(response, cheese.get_firmness_display())
    assertContains(response, cheese.country_of_origin.name)
    assertContains(response, cheese.country_of_origin.flag)
    assertContains(response, cheese.creator.username)


def test_cheese_create_form_valid(client, user):
    client.force_login(user)
    form_data = {
        "name": "catupiry",
        "description": "world's best",
        "firmness": Cheese.Firmness.SOFT,
    }

    url = reverse("cheeses:add")
    response = client.post(url, form_data)

    assert response.status_code == 302

    cheese = Cheese.objects.get(name=form_data["name"])

    assert cheese.name == form_data["name"]
    assert cheese.firmness == form_data["firmness"]
    assert cheese.creator == user