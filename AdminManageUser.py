import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class AdminManageUser(unittest.TestCase):

   def setUp(self):
       self.driver = webdriver.Chrome()

   def test_login(self):
           user = "instructor"
           pwd = "maverick1a"
           driver = self.driver
           driver.maximize_window()
           driver.get("https://mavgym.herokuapp.com/")
           time.sleep(1)
           elem = driver.find_element_by_xpath("/html/body/nav/div/div[2]/ul[2]/a").click()
           elem = driver.find_element_by_id("id_username")
           elem.send_keys(user)
           elem = driver.find_element_by_id("id_password")
           elem.send_keys(pwd)
           elem.send_keys(Keys.RETURN)
           time.sleep(1)
           #displays all users in table
           elem = driver.find_element_by_xpath("/html/body/div/div[2]/div/div[1]/div/p/a").click()

          #Add new user
           elem = driver.find_element_by_xpath("/html/body/div[2]/div/div/div/a/span").click()
           time.sleep(1)
           elem = driver.find_element_by_id("id_first_name")
           elem.send_keys("Clara")
           elem = driver.find_element_by_id("id_last_name")
           elem.send_keys("Smith")
           elem = driver.find_element_by_id("id_email")
           elem.send_keys("csmith@gmail.com")
           elem = driver.find_element_by_id("id_username")
           elem.send_keys("csmith")
           elem = driver.find_element_by_xpath("/html/body/div/form/button").click()
           time.sleep(1)
           # Edit User
           elem = driver.find_element_by_xpath("/html/body/div[2]/div/div/table/tbody/tr[1]/td[6]/a").click()

           fname = "Stuti"
           elem = driver.find_element_by_id("id_first_name")
           elem.clear()
           elem.send_keys(fname)
           time.sleep(1)

           lname = "Raut"
           elem = driver.find_element_by_id("id_last_name")
           elem.clear()
           elem.send_keys(lname)
           time.sleep(1)

           email = "stutsraut1@gmail.com"
           elem = driver.find_element_by_id("id_email")
           elem.clear()
           elem.send_keys(email)
           time.sleep(1)

           username = "stutsraut1"
           elem = driver.find_element_by_id("id_username")
           elem.clear()
           elem.send_keys(email)
           time.sleep(1)

           elem = driver.find_element_by_xpath("/html/body/div/form/button").click()

           #Delete User
           elem = driver.find_element_by_xpath("/html/body/div[2]/div/div/table/tbody/tr[1]/td[6]/a").click()

           alert = driver.switch_to.alert
           time.sleep(1)
           alert.accept()
           time.sleep(1)

   def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
 unittest.main()
