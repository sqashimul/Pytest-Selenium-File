import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import pytest

class TestOrangeHRM():
    @pytest.fixture()
    def setup(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.maximize_window()
        yield
        self.driver.close()

    def test_homePageTitle(self, setup):
        self.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        assert self.driver.title == "OrangeHRM123"

    def test_login(self, setup):
        self.driver.get("https://www.facebook.com/")
        print(self.driver.title)
        self.driver.find_element(By.NAME, "email").send_keys("Admin")
        self.driver.find_element(By.NAME, "pass").send_keys("admin123")
        self.driver.find_element(By.NAME, "login").click()
        assert self.driver.title == "Facebook – log in or sign up"
        time.sleep(5)

#PS C:\Learn Pytest\Pytest-HTML_Reports> pytest -v -s --html=report.html --self-contained-html Pytstreportshtml.py