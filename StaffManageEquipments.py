import unittest
import time
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys



class StaffManageEquipments(unittest.TestCase):

   def setUp(self):
       self.driver = webdriver.Chrome()

   def test_blog(self):
       user = "Staff1"
       pwd = "team12345"
       driver = self.driver
       driver.maximize_window()
       driver.get("https://mavgym.herokuapp.com/")

       loginEle = driver.find_element_by_xpath ( "/html/body/nav/div/div[2]/ul[2]/a" ).click ( )
       loginEle = driver.find_element_by_id("id_username")
       loginEle.send_keys(user)
       loginEle = driver.find_element_by_id("id_password")
       loginEle.send_keys(pwd)
       loginEle.send_keys(Keys.RETURN)
       assert "Logged In"

       #Manage Equipments button
       driver.find_element_by_xpath ( "/html/body/div/div[2]/div/div[2]/div/p/a" ).click ( )
       time.sleep(1)

       #Add new equip button
       driver.find_element_by_xpath ("/html/body/div[2]/div/div/div/a/span" ).click ( )

       elem = driver.find_element_by_id("id_name")
       elem.send_keys("Bar")
       elem = driver.find_element_by_id("id_description")
       elem.send_keys("Bar for push ups")
       shift =  driver.find_element_by_id ( 'id_weight' )
       shift.send_keys ( '10 pound' )

        #Save button
       driver.find_element_by_xpath("/ html / body / div / form / button").click()

       #Edit equip
       driver.find_element_by_xpath("/html/body/div[2]/div/div/table/tbody/tr[3]/td[4]/a").click()
       time.sleep(1)
       elem = driver.find_element_by_id("id_name")
       elem.send_keys("Bar")
       elem = driver.find_element_by_id("id_description")
       elem.send_keys("Bar for push ups")
       shift = driver.find_element_by_id('id_weight')
       shift.send_keys('10 pound')
       #Save
       elem = driver.find_element_by_xpath("/ html / body / div / form / button").click()

       # Delete User
       elem = driver.find_element_by_xpath("/html/body/div[2]/div/div/table/tbody/tr[3]/td[5]/a").click()

       alert = driver.switch_to.alert
       time.sleep(1)
       alert.accept()
       time.sleep(1)



   def tearDown(self):
       self.driver.close()

   if __name__ == "__main__":
       unittest.main()
