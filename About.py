import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class About(unittest.TestCase):

   def setUp(self):
       self.driver = webdriver.Chrome()

   def test_login(self):

           driver = self.driver
           driver.maximize_window()
           driver.get("https://mavgym.herokuapp.com/")
           time.sleep(1)
           #About page
           elem = driver.find_element_by_xpath("/html/body/div[2]/div/div[1]/div/p[2]/a").click()
           time.sleep(1)


   def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
 unittest.main()
