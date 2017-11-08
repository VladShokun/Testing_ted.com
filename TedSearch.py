import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class TedSearch(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()

    def test_ted_search(self):
        driver = self.driver
        driver.get("https://www.ted.com")
        self.assertIn("Ideas worth spreading", driver.title)
        elem = driver.find_element_by_id("main-nav-search")
        elem.send_keys(Keys.RETURN)
        elem = driver.find_element_by_name("q")
        elem.send_keys("Elon Mask")
        elem.send_keys(Keys.RETURN)
        driver.find_elements_by_xpath("//*[contains(text(), 'Elon Mask')]")

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()