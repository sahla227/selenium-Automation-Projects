import logging
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class TestBrowsProducts:

    @pytest.fixture(autouse=True)
    def driver(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://bstackdemo.com/")
        time.sleep(3)
        yield self.driver
        logging.info("Testing is Completed")
        self.driver.quit()

    def test_stack_demo(self):
        self.driver.get("https://bstackdemo.com/")
        time.sleep(3)
        logging.info("Testing is Completed")
    # def test_checkout(self):
    #     self.driver.find_element(By.ID, "__next").click()

    def test_stack_add_cart_checkout(self):
        self.driver.get("https://bstackdemo.com/")
        time.sleep(3)
        add_cart=self.driver.find_element(By.XPATH, "(//div[@class='shelf-item__buy-btn'])[1]")
        add_cart.click()
        assert "Bag" in self.driver.page_source
        time.sleep(2)
        checkout=self.driver.find_element(By.XPATH, "//div[@class='buy-btn']")
        checkout.click()
        time.sleep(3)
    # def test_login(self ):
        self.driver.get("https://bstackdemo.com/signin?checkout=true")
        time.sleep(3)

        user_name=self.driver.find_element(By.ID,"username")
        user_name.click()
        dropdown=self.driver.find_element(By.XPATH,  "//div[text()='demouser']")
        dropdown.click()
        time.sleep(3)
        password_drp=self.driver.find_element(By.ID,"password")
        password_drp.click()
        dropdown_ps = self.driver.find_element(By.XPATH, "//div[text()='testingisfun99']")
        dropdown_ps.click()
        login_btn=self.driver.find_element(By.ID,"login-btn")
        login_btn.click()

        time.sleep(2)

        assert "StackDemo" in self.driver.page_source
        input_first=self.driver.find_element(By.ID, "firstNameInput")
        input_first.send_keys("John")
        input_second=self.driver.find_element(By.ID, "lastNameInput")
        input_second.send_keys("Doe")
        address=self.driver.find_element(By.ID, "addressLine1Input")
        address.send_keys("Kannur")
        state=self.driver.find_element(By.ID, "provinceInput")
        state.send_keys("Kerala")
        postal_code=self.driver.find_element(By.ID, "postCodeInput")
        postal_code.send_keys("12345")
        submit=self.driver.find_element(By.ID, "checkout-shipping-continue")
        submit.click()
        time.sleep(3)
        # assert "Your Order has been successfully placed." in self.driver.page_source
        actual = self.driver.find_element(By.ID, "confirmation-message").text

        print(actual)  # debug

        assert "cancelled" in actual.lower()


