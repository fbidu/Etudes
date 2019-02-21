import re

from django.http import HttpRequest
from django.shortcuts import render
from django.test import TestCase
from django.urls import resolve

from lists.models import Item
from lists.views import home_page


class HomePageTest(TestCase):
    def test_root_url_resolves_to_homepage_view(self):
        found = resolve("/")
        self.assertEqual(found.func, home_page)

    def _remove_csrf_token(self, response):
        """
        _remove_csrf_token removes the contents of a CSRF token present in a 
        rendered template.
        
        Those tokens change everytime the page is rendered, so they must be
        extracted before we try to assert that the contents are equal.
        """
        csrf_regex = r"<input[^>]+csrfmiddlewaretoken[^>]+>"
        return re.sub(csrf_regex, "", response.content.decode())

    def test_home_page_returns_correct_html(self):
        """
        Tests if the home page actually render the home page
        """
        # Makes a request to our home
        request = HttpRequest()
        response = home_page(request)

        # That request will include an CSRF token. That token changes with each
        # request. We need to remove it in order to be able to test properly
        observed_html = self._remove_csrf_token(response)

        # We'll have the same problem while rendering the expected response.
        expected_response = render(request, "home.html")
        expected_html = self._remove_csrf_token(expected_response)

        # Finally, we check everything
        self.assertEqual(observed_html, expected_html)

    def test_home_page_can_save_a_POST_request(self):
        request = HttpRequest()
        request.method = "POST"
        request.POST["item_text"] = "A new list item"

        response = home_page(request)
        observed_html = self._remove_csrf_token(response)

        self.assertIn("A new list item", observed_html)

        expected_response = render(
            request, "home.html", {"new_item_text": "A new list item"}
        )
        expected_html = self._remove_csrf_token(expected_response)

        self.assertEqual(observed_html, expected_html)


class ItemModelTest(TestCase):
    def test_saving_and_retrieving_items(self):
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
