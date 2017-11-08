# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class TedWatch(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.ted.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_ted_watch(self):
        driver = self.driver
        driver.get(self.base_url + "/")
        driver.find_element_by_link_text("Watch").click()
        driver.find_element_by_xpath("//nav[@id='main-nav']/div[3]/ul/li/ul/li/a/div").click()
        try: self.assertEqual("to stir your curiosity", driver.find_element_by_xpath("//div[@id='shoji']/div[2]/div/div[2]/header/div/div/span[2]").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        driver.find_element_by_link_text("Watch").click()
        driver.find_element_by_xpath("//nav[@id='main-nav']/div[3]/ul/li/ul/li[2]/a/div[2]").click()
        try: self.assertEqual("Playlists", driver.find_element_by_css_selector("h1.h1.playlists-header__heading").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        driver.find_element_by_link_text("Watch").click()
        driver.find_element_by_xpath("//nav[@id='main-nav']/div[3]/ul/li/ul/li[3]/a/div").click()
        try: self.assertEqual("TED-Ed videos", driver.find_element_by_xpath("//div[@id='shoji']/div[2]/div/div[2]/div/div/div/h1").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        driver.find_element_by_link_text("Watch").click()
        driver.find_element_by_xpath("//nav[@id='main-nav']/div[3]/ul/li/ul/li[4]/a/div[2]").click()
        try: self.assertEqual("TEDx Talks", driver.find_element_by_xpath("//div[@id='shoji']/div[2]/div/div[2]/div/div/div/h1").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        driver.find_element_by_link_text("Watch").click()
        driver.find_element_by_xpath("//nav[@id='main-nav']/div[3]/ul/li/ul/li[5]/a").click()
        try: self.assertEqual("Let us surprise you.", driver.find_element_by_css_selector("h1.h2").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
    
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True
    
    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
