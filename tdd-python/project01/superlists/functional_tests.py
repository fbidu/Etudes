from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest


class NewVisitorTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        # Edith heard about a cool new online to-do app. She checks the homepage.
        self.browser.get("http://localhost:8000")

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

        table = self.browser.find_element_by_id("id_list_table")
        rows = table.find_elements_by_tag_name("tr")
        self.assertTrue(
            any(row.text == "1: Buy 00 Flour" for row in rows),
            "New to-do item did not appear in table",
        )

        self.fail("Finish the test!")
        # There is still a text box inviting her to add another item. She
        # enters "Buy canned tomatoes"
        #
        # The page updates again, and now shows both items on her list
        #
        # Edith wonders whether the site will remember her list. Then she sees
        # that the site has generated a unique URL for her -- there is some
        # explanatory text to that effect
        #
        # She visits that URL - her to-do list is still there
        #
        # Satistfied, she goes back to sleep


if __name__ == "__main__":
    unittest.main(warnings="ignore")
