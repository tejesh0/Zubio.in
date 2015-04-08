from django.test import TestCase
from selenium import webdriver
import unittest
import logging


# Create your tests here.
"""
behavioural test go here....

coming sooon

"""

class GymProfileFormTest(unittest.TestCase):
	def setUp(self):
		self.browser = webdriver.Firefox()
		# self.browser.implicitly_wait(3)

	def tearDown(self):
		self.browser.quit()

	def test_fill_full_form_and_submits(self):
		#zubio marketing boy opens browser and enter list form loaction
		self.browser.get('http://localhost:8000/list')

		#check title of page(funky basic test, it fails here, you lost your cover)
		self.assertIn('zubio', self.browser.title)
		print self.browser.title
		logging.warn("start filling form")
		#jumbo enters the fitness center name,(less than 100 characters)
		fitness_center_name = self.browser.find_element_by_id('id_Name_Of_The_Fitness_Center')
		fitness_center_name.send_keys('Zubio fitness center')
		self.assertEqual(fitness_center_name.get_attribute('value'),'Zubio fitness center')

		

		self.fail('Finish the test')


if __name__ == '__main__':
	unittest.main()



