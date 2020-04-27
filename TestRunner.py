from unittest import TestLoader, TestSuite, TextTestRunner
from About import About
from AdminLoginTest import AdminLoginTest
from StaffLoginTest import StaffLoginTest
from AdminManageUsersReport import AdminManageUsersReport
from AddNewActivity import AddNewActivity
from StaffManageEquipments import StaffManageEquipments
from CustomerViewActivities import CustomerViewActivities
from CustomerViewEquipments import CustomerViewEquipments
from CustomerLoginTest import CustomerLoginTest
from PasswordChange import PasswordChange

if __name__ == "__main__":
    loader = TestLoader()
    suite = TestSuite((
        loader.loadTestsFromTestCase(About),
        loader.loadTestsFromTestCase(AdminLoginTest),
        loader.loadTestsFromTestCase(StaffLoginTest),
        loader.loadTestsFromTestCase(CustomerLoginTest),
        loader.loadTestsFromTestCase(PasswordChange),
        loader.loadTestsFromTestCase(AdminManageUsersReport),
        loader.loadTestsFromTestCase(AddNewActivity),
        loader.loadTestsFromTestCase(StaffManageEquipments),
        loader.loadTestsFromTestCase(CustomerViewActivities),
        loader.loadTestsFromTestCase(CustomerViewEquipments),


    ))

    runner = TextTestRunner(verbosity=2)
    runner.run(suite)
