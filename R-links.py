# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import unittest, time, re

class ALinks(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://deanza.edu/"
        self.verificationErrors = []
    
    def test_a_links(self):
        link_title = {
            "Red Wheelbarrow Literary Magazine" : "Red Wheelbarrow Literary Magazine",
            "Registration Information" : "De Anza College :: Registration Information ::  How to Register for Classes",
            "Admission Requirements" : "De Anza College :: Admissions :: Admission Requirements",
            "Registration System, Online" : "De Anza College :: Registration :: De Anza Admissions and MyPortal Registration",
            "Facility Rentals" : "De Anza College :: Facilities Rental ::  Home",
            "Research" : "Welcome!",
            "Residency Requirements" : "De Anza College :: Admissions :: Residency Requirements",
            "Russian Department " : "De Anza College :: Russian :: Home",
            }
        
        driver = self.driver
        driver.get(self.base_url + "directory/dir-az.html")

        for link in link_title:
            title = link_title[link]
            driver.find_element_by_link_text(link).click()
            try: self.assertEqual(title, driver.title)
            except AssertionError as e: self.verificationErrors.append(str(e))
            driver.back()

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
