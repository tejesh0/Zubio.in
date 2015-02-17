from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest
from django.test import TestCase

from users_zubio.views import SellerForm



class SellerFormTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def test_seller_form_details(self):
	    # Edith has heard about a cool new online to-do app. She goes
	    # to check out its homepage
	    self.browser.get('http://localhost:8000/sell/')

	    form_data = {'prod_description':'oneplusone','months_used':'3','selling_price':'55000','is_negotiable':''}
	    form = SellerForm(data=form_data)
	    self.assertEqual(form.is_valid(), True)