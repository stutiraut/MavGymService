import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class CustomerLoginTest(unittest.TestCase):

   def setUp(self):
       self.driver = webdriver.Chrome()

   def test_login(self):
           user = "Customer1"
           pwd = "team12345"
           driver = self.driver
           driver.maximize_window()
           driver.get("https://mavgym.herokuapp.com/")
           elem = driver.find_element_by_xpath("/html/body/nav/div/div[2]/ul[2]/a").click()

           elem = driver.find_element_by_id("id_username")
           elem.send_keys(user)
           elem = driver.find_element_by_id("id_password")
           elem.send_keys(pwd)
           elem = driver.find_element_by_xpath("/html/body/div/div/form/p[3]/input").click()


   def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
   unittest.main()

