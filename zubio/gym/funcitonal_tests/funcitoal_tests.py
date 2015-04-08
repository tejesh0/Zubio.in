from django.test import TestCase
from selenium import webdriver
import unittest
import logging
import os

# Create your tests here.
"""
behavioural test go here....

coming sooon

"""


class GymProfileFormTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        # self.browser.implicitly_wait(3)

    # def tearDown(self):
    #     self.browser.quit()

    def test_fill_full_form_and_submits(self):
        # zubio marketing boy opens browser and enter list form loaction
        self.browser.get('http://localhost:8000/list')

        # check title of page(funky basic test, it fails here, you lost your
        # cover)
        self.assertIn('zubio', self.browser.title)
        print self.browser.title
        logging.warn("start filling form")
        # jumbo enters the fitness center name,(less than 100 characters)
        fitness_center_name = self.browser.find_element_by_id(
            'id_Name_Of_The_Fitness_Center')
        fitness_center_name.send_keys('Zubio fitness center')

        address = self.browser.find_element_by_id('id_Address')
        address.send_keys('Marathahalli village, Marathahalli, Bengaluru, Karnataka')

        phone_number = self.browser.find_element_by_id('id_phone_number')
        phone_number.send_keys('+918019810256')

        email_id = self.browser.find_element_by_id('id_Email')
        email_id.send_keys('zubio_admin@zubio.in')


        pricing = self.browser.find_element_by_id('id_Monthly')
        pricing.send_keys('1400')

        description = self.browser.find_element_by_id('id_Description')
        description.send_keys('Zubio is world class gym, spa, saloon with dance classes and yoga classes')

        print os.getcwd()
        self.browser.find_element_by_id("id_Gallery").send_keys("~/Desktop/Zubio.in/15.jpg")

        submit = self.browser.find_element_by_xpath("//input[@type='submit']")
        submit.click()

        # self.browser.implicitly_wait(30)

        # self.fail('Finish the test')


if __name__ == '__main__':
    unittest.main()
