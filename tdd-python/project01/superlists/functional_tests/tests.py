"""
Functional tests for the Lists app
"""
import time

from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class NewVisitorTest(StaticLiveServerTestCase):
    """
    Functional tests for a new user
    """

    def setUp(self):
        """
        setUp starts up our environment before running the tests
        """
        # Defines the browser engine we're going to use
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        """
        cleans up ou environment after the tests
        """
        # Closes the browser
        self.browser.quit()

    def check_for_row_in_list_table(self, row_text):
        """
        Helper function that checks if a text occurs inside
        the id_list_table table
        """
        table = self.browser.find_element_by_id("id_list_table")
        rows = table.find_elements_by_tag_name("tr")
        self.assertIn(row_text, [row.text for row in rows])

    def test_can_start_a_list_and_retrieve_it_later(self):
        """
        Tests if a client can start a list, add items and
        open it later
        """
        # Edith heard about a cool new online to-do app. She checks the homepage.
        self.browser.get(self.live_server_url)
        self.browser.set_window_size(1024, 768)

        # She notices the input box is nicely centered
        input_box = self.browser.find_element_by_id("id_new_item")
        self.assertAlmostEqual(
            input_box.location["x"] + input_box.size["width"] / 2, 512, delta=5
        )

        # She notices the page title and header mention to-do lists
        self.assertIn("To-Do", self.browser.title)

        header_text = self.browser.find_element_by_tag_name("h1").text
        self.assertIn("To-Do", header_text)

        # She is invited to enter a to-do item straight away
        input_box = self.browser.find_element_by_id("id_new_item")
        self.assertEqual(input_box.get_attribute("placeholder"), "Enter a to-do item")

        # She types "Buy 00 Flour" into a text box
        input_box.send_keys("Buy 00 Flour")

        # When she hits enter, the page updates, and now the page lists
        # "1: Buy 00 Flour" as an item in a to-do list
        input_box.send_keys(Keys.ENTER)
        time.sleep(2)
        edith_list_url = self.browser.current_url
        self.assertRegex(edith_list_url, "/lists/.+")
        self.check_for_row_in_list_table("1: Buy 00 Flour")

        # There is still a text box inviting her to add another item. She
        # enters "Buy canned tomatoes"
        input_box = self.browser.find_element_by_id("id_new_item")
        input_box.send_keys("Buy canned tomatoes")
        input_box.send_keys(Keys.ENTER)
        time.sleep(2)

        # The page updates again, and now shows both items on her list
        self.check_for_row_in_list_table("1: Buy 00 Flour")
        self.check_for_row_in_list_table("2: Buy canned tomatoes")

        # Now a new user, Francis, comes along to the site.
        self.browser.quit()
        self.browser = webdriver.Firefox()

        # Francis visits the home page. There is no sign of Edith's list
        self.browser.get(self.live_server_url)
        page_text = self.browser.find_element_by_tag_name("body").text

        self.assertNotIn("Buy 00 Flour", page_text)
        self.assertNotIn("Buy canned tomatoes", page_text)

        # Francis starts a new list by entering a new item
        input_box = self.browser.find_element_by_id("id_new_item")
        input_box.send_keys("Buy milk")
        input_box.send_keys(Keys.ENTER)
        time.sleep(2)
        # Francis gets his own unique URL
        francis_list_url = self.browser.current_url
        self.assertRegex(francis_list_url, "/lists/.+")
        self.assertNotEqual(francis_list_url, edith_list_url)

        # Again, there's no trace of Edith's list
        page_text = self.browser.find_element_by_tag_name("body").text

        self.assertNotIn("Buy 00 Flour", page_text)
        self.assertNotIn("Buy canned tomatoes", page_text)
        self.assertIn("milk", page_text)

        self.fail("Finish the test!")
        # She visits that URL - her to-do list is still there
        #
        # Satistfied, she goes back to sleep
