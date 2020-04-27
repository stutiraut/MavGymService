import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class AdminManageUsersReport(unittest.TestCase):

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
           #clicks the manage report button
           elem = driver.find_element_by_xpath("/html/body/div/div[2]/div/div[2]/div/p/a").click()
           time.sleep(1)

           #User report
           elem = driver.find_element_by_xpath("/html/body/div/div[2]/div/div[1]/div/p/a").click()


           driver.get("https://mavgym.herokuapp.com/reports_list/")
           # Activities report
           elem = driver.find_element_by_xpath("/html/body/div/div[2]/div/div[2]/div/p/a").click()

           driver.get("https://mavgym.herokuapp.com/reports_list/")
           # Equipments report
           elem = driver.find_element_by_xpath("/html/body/div/div[2]/div/div[3]/div/p/a").click()



   def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
 unittest.main()
