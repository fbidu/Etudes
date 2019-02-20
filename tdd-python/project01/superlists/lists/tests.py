import re

from django.http import HttpRequest
from django.shortcuts import render
from django.test import TestCase
from django.urls import resolve

from lists.views import home_page


class HomePageTest(TestCase):
    def test_root_url_resolves_to_homepage_view(self):
        found = resolve("/")
        self.assertEqual(found.func, home_page)

    def test_home_page_returns_correct_html(self):
        """
        Tests if the home page actually render the home page
        """
        # Makes a request to our home
        request = HttpRequest()
        response = home_page(request)

        # That request will include an CSRF token. That token changes with each
        # request. We need to remove it in order to be able to test properly
        csrf_regex = r"<input[^>]+csrfmiddlewaretoken[^>]+>"
        observed_html = re.sub(csrf_regex, "", response.content.decode())

        # We'll have the same problem while rendering the expected response.
        expected_html = render(request, "home.html")
        expected_html = re.sub(csrf_regex, "", expected_html.content.decode())

        # Finally, we check everything
        self.assertEqual(observed_html, expected_html)

    def test_home_page_can_save_a_POST_request(self):
        request = HttpRequest()
        request.method = "POST"
        request.POST["item_text"] = "A new list item"

        response = home_page(request)

        self.assertIn("A new list item", response.content.decode())
