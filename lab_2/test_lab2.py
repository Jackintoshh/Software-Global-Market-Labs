# -*- coding: utf-8 -*-
#The first line is the encoding to use in this file in this case UTF-8

from selenium import webdriver
import unittest
import time
#Next we import all the packages we need
#We import selenium and unittest which is a test package in python
#We are also importing time which allows us to set a wait so that we can see the output in the brower 

#We create a class NewVistorTest which inherits from TestCase  
class NewVisitorTest(unittest.TestCase):
 
#setUp runs at the begining of the test and setups whatever we need, in this case it lauches the Firefox browser
    def setUp(self):
        self.browser = webdriver.Firefox() #lauch Firefox browser, requires geckodriver.exe to be on your PATH
        self.browser.implicitly_wait(3)

#tearDown runs at the end of the test and will clear up anything we have setup so in this case it will quit the browser
    def tearDown(self):
   		self.browser.quit() #

 	def test_title(self):
 		self.browser.get('http://localhost:8000')
 		self.assertIn("A Sample Django App!", self.browser.title)
 		time.sleep(5)

 	def test_h1_css(self):
 		self.browser.get('http://localhost8000')
 		h1 = self.browser.find_element_by_tag_name("h1")
 		print (h1.value_of_css_property("color"))
 		self.assertEqual(h1.value_of_css_property("color"), "rgb(255, 192, 203)")