import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class Signup(unittest.TestCase):

   def setUp(self):
       self.driver = webdriver.Chrome()

   def test_login(self):

           driver = self.driver
           driver.maximize_window()
           driver.get("https://mavgym.herokuapp.com/")
           time.sleep(1)
           #CLick Signup page
           elem = driver.find_element_by_xpath("/html/body/div[2]/div/div[2]/div/p[2]/a").click()
           username="test"
           emailid="test@gmail.com"
           fname="Test"
           lname="Test1"
           pwd="team12345"
           repwd="team12345"
           time.sleep(1)
           elem = driver.find_element_by_id("id_username")
           elem.send_keys(username)
           time.sleep(1)
           elem = driver.find_element_by_id("id_email")
           elem.send_keys(emailid)
           time.sleep(1)
           elem = driver.find_element_by_id("id_first_name")
           elem.send_keys(fname)
           time.sleep(1)
           elem = driver.find_element_by_id("id_last_name")
           elem.send_keys(lname)
           time.sleep(1)
           elem = driver.find_element_by_id("id_password1")
           elem.send_keys(pwd)
           time.sleep(1)
           elem = driver.find_element_by_id("id_password2")
           elem.send_keys(repwd)
           #Click signup
           elem = driver.find_element_by_xpath("/html/body/div/form/p/button").click()
           time.sleep(2)


   def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
 unittest.main()
