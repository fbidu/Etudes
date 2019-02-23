"""
Unit tests for the functions in the list app
"""
import re

from django.http import HttpRequest
from django.shortcuts import render
from django.test import TestCase
from django.urls import resolve

from lists.models import Item, List
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


class ListAndItemModelTest(TestCase):
    """
    ItemModelTest provides tests for the Item ORM model
    """

    def test_saving_and_retrieving_items(self):
        """
        Tests if we are able to create new lists and items,
        save them and then retrieve all of them
        """
        list_ = List()
        list_.save()

        first_item = Item()
        first_item.text = "The first (ever) list item"
        first_item.list = list_
        first_item.save()

        second_item = Item()
        second_item.text = "Item the second"
        second_item.list = list_
        second_item.save()

        saved_list = List.objects.first()
        self.assertEqual(saved_list, list_)

        saved_items = Item.objects.all()
        self.assertEqual(saved_items.count(), 2)

        first_saved_item = saved_items[0]
        second_saved_item = saved_items[1]
        self.assertEqual(first_saved_item.text, "The first (ever) list item")
        self.assertEqual(first_saved_item.list, list_)
        self.assertEqual(second_saved_item.text, "Item the second")
        self.assertEqual(second_saved_item.list, list_)


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

        new_list = List.objects.first()
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, f"/lists/{new_list.id}/")


class ListViewTest(TestCase):
    """
    ListViewTest tests if the rendering and displaying of a created list
    works correctly
    """

    def test_uses_list_template(self):
        """
        Is the list rendered with the correct template?
        """
        list_ = List.objects.create()
        response = self.client.get(f"/lists/{list_.id}/")
        self.assertTemplateUsed(response, "list.html")

    def test_displays_only_items_for_that_list(self):
        """
        Do we display just the correct list items?
        """
        first_list = List.objects.create()
        Item.objects.create(text="item1", list=first_list)
        Item.objects.create(text="item2", list=first_list)

        second_list = List.objects.create()
        Item.objects.create(text="other list item 1", list=second_list)
        Item.objects.create(text="other list item 2", list=second_list)

        response = self.client.get(f"/lists/{first_list.id}/")

        self.assertContains(response, "item1")
        self.assertContains(response, "item2")
        self.assertNotContains(response, "other list item 1")
        self.assertNotContains(response, "other list item 2")

    def test_passes_correct_list_to_template(self):
        other_list = List.objects.create()
        correct_list = List.objects.create()
        response = self.client.get(f"/lists/{correct_list.id}/")

        self.assertEqual(response.context["list"], correct_list)


class NewItemTest(TestCase):
    """
    Tests the addition of new items to a current list
    """

    def test_can_save_a_post_request_to_an_existing_list(self):
        """
        as written by me!
        """
        list_ = List.objects.create()
        first_item = Item.objects.create(text="Hai", list=list_)
        new_item = {"item_text": "new item!"}
        self.client.post(f"/lists/{list_.id}/add_item", data=new_item)

        response = self.client.get(f"/lists/{list_.id}/")

        # This assertion looks more like an functional test than an unit one
        # Notice how in the book's test below, the author did not check
        # for the response contents.
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, new_item["item_text"])
        self.assertContains(response, first_item.text)

    def test_can_save_a_post_request_to_an_existing_list_book(self):
        """
        as appears on the book
        """
        other_list = List.objects.create()
        correct_list = List.objects.create()

        self.client.post(
            f"/lists/{correct_list.id}/add_item", data={"item_text": "A new item!"}
        )

        self.assertEqual(Item.objects.count(), 1)
        new_item = Item.objects.first()
        self.assertEqual(new_item.text, "A new item!")
        self.assertEqual(new_item.list, correct_list)
        self.assertEqual(Item.objects.filter(list=other_list).count(), 0)

    def test_redirects_to_list_view(self):
        """
        Tests if the correct redirection is being used
        """
        other_list = List.objects.create()
        correct_list = List.objects.create()

        response = self.client.post(
            f"/lists/{correct_list.id}/add_item", data={"item_text": "Anothe item!"}
        )

        self.assertRedirects(response, f"/lists/{correct_list.id}/")
