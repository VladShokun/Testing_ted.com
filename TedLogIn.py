import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

with open('logindata.txt') as f:
  credentials = [x.strip().split(':') for x in f.readlines()]

for username,password in credentials:

    class TedLogIn(unittest.TestCase):

         def setUp(self):
            self.driver = webdriver.Firefox()

         def test_ted_log_in(self):
            driver = self.driver
            driver.get("https://www.ted.com")
            elem = driver.find_element_by_xpath('//*[@id="main-nav"]/div[3]/a')
            elem.send_keys(Keys.RETURN)
            driver.find_elements_by_xpath("//*[contains(text(), 'Log in to TED')]")
            elem = driver.find_element_by_name("user[email]")
            elem.send_keys(username)
            elem = driver.find_element_by_name("user[password]")
            elem.send_keys(password)
            elem = driver.find_element_by_xpath("/html/body/div[2]/div[2]/div/div/div/div[2]/form/div[5]/button")
            elem.send_keys(Keys.RETURN)

         def tearDown(self):
             self.driver.close()

    if __name__ == "__main__":
        unittest.main()