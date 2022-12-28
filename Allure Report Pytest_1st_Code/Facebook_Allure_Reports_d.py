import allure
from allure_commons.types import AttachmentType
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import pytest

@allure.severity(allure.severity_level.NORMAL)
class TestFacebook:
    @allure.severity(allure.severity_level.MINOR)
    def test_logo(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.maximize_window()

        self.driver.get("https://www.facebook.com/")
        status = self.driver.find_element(By.XPATH, "//img[@alt='Facebook']").is_displayed()
        if status == True:
            assert True
        else:
            assert False
        self.driver.close()

    @allure.severity(allure.severity_level.MINOR)
    def test_listemployees(self):
        pytest.skip('Skiping test.. Later I will implement...')

    @allure.severity(allure.severity_level.CRITICAL)
    def test_login(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get("https://www.facebook.com/")
        self.driver.maximize_window()
        print(self.driver.title)
        self.driver.find_element(By.NAME, "email").send_keys("Admin")
        self.driver.find_element(By.NAME, "pass").send_keys("admin123")
        self.driver.find_element(By.NAME, "login").click()
        act_title = self.driver.title

        if act_title == "Facebook – log in or sign up or register":
            self.driver.close()
            assert True
        else:
            allure.attach(self.driver.get_screenshot_as_png(), name = "testloginscripts", attachment_type = AttachmentType.PNG)
            self.driver.close()
            assert False


#pytest -v -s Allure_Reports_D\Facebook_Allure_Reports_d.py
#pytest -v -s --alluredir="C:\Learn Pytest\Pytest-HTML_Reports\Allure_Reports_D\report_allure" Allure_Reports_D\Facebook_All
#ure_Reports_d.py


