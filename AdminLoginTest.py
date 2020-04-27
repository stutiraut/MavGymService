import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class AdminLoginTest(unittest.TestCase):

   def setUp(self):
       self.driver = webdriver.Chrome()

   def test_login(self):
           user = "instructor"
           pwd = "maverick1a"
           driver = self.driver
           driver.maximize_window()
           driver.get("https://mavgym.herokuapp.com/admin/login/?next=/admin/")
           elem = driver.find_element_by_id("id_username")
           elem.send_keys(user)
           elem = driver.find_element_by_id("id_password")
           elem.send_keys(pwd)
           elem.send_keys(Keys.RETURN)
           time.sleep(1)
           #Admin homepage
           elem = driver.find_element_by_xpath("/html/body/div/div[1]/div[2]/a[1]").click()


           #logout
           elem = driver.find_element_by_xpath("/html/body/nav/div/div[2]/ul[2]/div/div/a[1]").click()


   def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
 unittest.main()
