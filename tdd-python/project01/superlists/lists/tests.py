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

        home_page(request)

        self.assertEqual(Item.objects.count(), 1)
        new_item = Item.objects.first()
        self.assertEqual(new_item.text, "A new list item")

    def test_home_page_redirects_after_POST(self):
        request = HttpRequest()
        request.method = "POST"
        request.POST["item_text"] = "A new list item"

        response = home_page(request)

        self.assertEqual(response.status_code, 302)
        self.assertEqual(response["location"], "/lists/the-first-list")

    def test_home_page_only_saves_items_when_necessary(self):
        request = HttpRequest()
        home_page(request)
        self.assertEqual(Item.objects.count(), 0)


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


class ListViewTest(TestCase):
    def test_uses_list_template(self):
        response = self.client.get("/lists/the-first-list")
        self.assertTemplateUsed(response, "list.html")

    def test_displays_all_item(self):
        Item.objects.create(text="item1")
        Item.objects.create(text="item2")

        response = self.client.get("/lists/the-first-list")

        self.assertContains(response, "item1")
        self.assertContains(response, "item2")
