import unittest
import time
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys



class AddNewActivity(unittest.TestCase):

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
       time.sleep(1)
       #Manage Activities button
       driver.find_element_by_xpath ( "/html/body/div/div[2]/div/div[1]/div/p/a" ).click ( )
       #Add new Activity button
       driver.find_element_by_xpath ("/html/body/div/a[3]" ).click ( )
       activity = Select ( driver.find_element_by_id ( 'id_activity' ) )
       activity.select_by_visible_text ( 'SWIMMING CLASS' )
       shift =  driver.find_element_by_id ( 'id_time' )
       shift.send_keys ( '3:00 pm - 4:00 pm' )
       location = driver.find_element_by_id('id_location')
       location.send_keys('MGS Room 103')

       startDate = driver.find_element_by_id('id_start_date')
       startDate.send_keys('05/08/2020')

       saveButton = driver.find_element_by_xpath(" /html/body/form/table/tbody/tr[5]/td/button").click()
       nextMonthButton = driver.find_element_by_xpath(
           "/html/body/div/a[2]").click()
        #Edit
       edit = driver.find_element_by_xpath(" / html / body / table / tbody / tr[4] / td[5] / ul / a[1]").click()
       shift = driver.find_element_by_id('id_time')
       shift.send_keys('4:00 pm - 5:00 pm')
       saveButton = driver.find_element_by_xpath(" /html/body/form/table/tbody/tr[5]/td/button").click()
       driver.get("https://mavgym.herokuapp.com/calendar/?month=2020-5")
       time.sleep(1)
       # delete activity
       deleteLink = driver.find_element_by_xpath(" / html / body / table / tbody / tr[4] / td[5] / ul / a[2]").click()
       obj = driver.switch_to.alert
       time.sleep(1)
       obj.accept()

       driver.get("https://mavgym.herokuapp.com/calendar/?month=2020-5")



   def tearDown(self):
       self.driver.close()

   if __name__ == "__main__":
       unittest.main()
