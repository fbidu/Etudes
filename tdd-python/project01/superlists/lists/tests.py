"""
Unit tests for the functions in the list app
"""
import re

from django.http import HttpRequest
from django.shortcuts import render
from django.test import TestCase
from django.urls import resolve

from lists.models import Item
from lists.views import home_page


def remove_csrf_token(response):
    """
    remove_csrf_token removes the contents of a CSRF token present in a 
    rendered template.
    
    Those tokens change everytime the page is rendered, so they must be
    extracted before we try to assert that the contents are equal.
    """
    csrf_regex = r"<input[^>]+csrfmiddlewaretoken[^>]+>"
    return re.sub(csrf_regex, "", response.content.decode())


class HomePageTest(TestCase):
    """
    HomePageTest provides a suite of tests for our homepage
    """

    def test_root_url_resolves_to_homepage_view(self):
        """
        Tests if the homepage works!
        """
        found = resolve("/")
        self.assertEqual(found.func, home_page)

    def test_home_page_returns_correct_html(self):
        """
        Tests if the home page actually renders the home page
        """
        # Makes a request to our home
        request = HttpRequest()
        response = home_page(request)

        # That request will include an CSRF token. That token changes with each
        # request. We need to remove it in order to be able to test properly
        observed_html = remove_csrf_token(response)

        # We'll have the same problem while rendering the expected response.
        expected_response = render(request, "home.html")
        expected_html = remove_csrf_token(expected_response)

        # Finally, we check everything
        self.assertEqual(observed_html, expected_html)


class ItemModelTest(TestCase):
    """
    ItemModelTest provides tests for the Item ORM model
    """

    def test_saving_and_retrieving_items(self):
        """
        Tests if we are able to create new items, save them
        and then retrieve all of them
        """
        first_item = Item()
        first_item.text = "The first (ever) list item"
        first_item.save()

        second_item = Item()
        second_item.text = "Item the second"
        second_item.save()

        saved_items = Item.objects.all()
        self.assertEqual(saved_items.count(), 2)

        first_saved_item = saved_items[0]
        second_saved_item = saved_items[1]
        self.assertEqual(first_saved_item.text, "The first (ever) list item")
        self.assertEqual(second_saved_item.text, "Item the second")


class NewListTest(TestCase):
    """
    NewListTest provides tests for creating a new list
    """

    def test_saving_a_post_request(self):
        """
        Tests if a simple POST request is actually saved
        """
        self.client.post("/lists/new", data={"item_text": "A new list item"})

        self.assertEqual(Item.objects.count(), 1)
        new_item = Item.objects.first()
        self.assertEqual(new_item.text, "A new list item")

    def test_redirects_after_post(self):
        """
        Tests if we're redirected after a POST
        """
        response = self.client.post("/lists/new", data={"item_text": "A new list item"})

        self.assertEqual(response.status_code, 302)
        self.assertEqual(response["location"], "/lists/the-first-list/")


class ListViewTest(TestCase):
    """
    ListViewTest tests if the rendering and displaying of a created list
    works correctly
    """

    def test_uses_list_template(self):
        """
        Is the list rendered with the correct template?
        """
        response = self.client.get("/lists/the-first-list/")
        self.assertTemplateUsed(response, "list.html")

    def test_displays_all_item(self):
        """
        Do we display all of the list items?
        """
        Item.objects.create(text="item1")
        Item.objects.create(text="item2")

        response = self.client.get("/lists/the-first-list/")

        self.assertContains(response, "item1")
        self.assertContains(response, "item2")
