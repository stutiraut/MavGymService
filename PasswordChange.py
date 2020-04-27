import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class PasswordChange(unittest.TestCase):

   def setUp(self):
       self.driver = webdriver.Chrome()

   def test_login(self):
           user = "pwdtest"
           pwd = "team12345"
           driver = self.driver
           driver.maximize_window()
           driver.get("https://mavgym.herokuapp.com")

           #Login
           elem = driver.find_element_by_xpath("/html/body/div[1]/div/div/a").click()
           elem = driver.find_element_by_id("id_username")
           elem.send_keys(user)
           elem = driver.find_element_by_id("id_password")
           elem.send_keys(pwd)
           elem.send_keys(Keys.RETURN)
           time.sleep(1)

           time.sleep(1)
           #Click pwd change
           elem = driver.find_element_by_xpath("/ html / body / nav / div / div[2] / ul[2] / div / div / a[2]").click()
           opwd="team12345"
           npwd = "team12345"
           elem = driver.find_element_by_id("id_old_password")
           elem.send_keys(opwd)
           elem = driver.find_element_by_id("id_new_password1")
           elem.send_keys(npwd)
           elem = driver.find_element_by_id("id_new_password2")
           elem.send_keys(npwd)
           elem.send_keys(Keys.RETURN)
           time.sleep(1)




   def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
 unittest.main()
