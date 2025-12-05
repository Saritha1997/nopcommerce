import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from utilities.read_properties import Read_Config
from utilities.custom_logger import Log_Maker
from base_pages.Login_Admin_Page import Login_Admin_Page

class Test_01_Admin_Login:
    admin_page_url = Read_Config.get_admin_page_url()
    username = Read_Config.get_username()
    password = Read_Config.get_password()
    invalid_username = Read_Config.get_invalid_username()
    logger = Log_Maker.log_gen()

    @pytest.mark.regression
    def test_verify_title(self, setup):
        self.logger.info("**************Test_01_Admin_Login*************")
        self.logger.info("*******test_verify_title started *************")
        self.driver = setup
        self.driver.get(self.admin_page_url)
        actual_title = self.driver.title
        expected_title = "nopCommerce demo store. Login"
        if actual_title == expected_title:
            self.logger.info("*******test_verify_title Passed *************")
            assert True
            self.driver.close()
        else:
            self.logger.info("*******test_verify_title Failed *************")
            self.driver.save_screenshot("screenshots/test_verify_title.png")
            self.driver.close()
            assert False

    @pytest.mark.regression
    @pytest.mark.sanity
    def test_verify_admin_login(self, setup):
        self.driver = setup
        self.driver.get(self.admin_page_url)
        self.admin_lp = Login_Admin_Page(self.driver)
        self.admin_lp.enter_username(self.username)
        self.admin_lp.enter_password(self.password)
        self.admin_lp.click_login()
        actual_dashboard_text = self.driver.find_element(By.XPATH, "//div[@class='content-header']/h1").text
        if actual_dashboard_text == "Dashboard":
            assert True
            self.driver.close()
        else:
            self.driver.save_screenshot("screenshots/test_verify_admin_login.png")
            self.driver.close()
            assert False

    @pytest.mark.regression
    def test_verify_admin_invalid_login(self, setup):
        self.driver = setup
        self.driver.get(self.admin_page_url)
        self.admin_lp = Login_Admin_Page(self.driver)
        self.admin_lp.enter_username(self.invalid_username)
        self.admin_lp.enter_password(self.password)
        self.admin_lp.click_login()
        error_message = self.driver.find_element(By.XPATH, "//li").text
        if error_message == "No customer account found":
            assert True
            self.driver.close()
        else:
            self.driver.save_screenshot("screenshots/test_verify_admin_invalid_login.png")
            self.driver.close()
            assert False

