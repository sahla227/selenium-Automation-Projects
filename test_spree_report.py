import logging

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class TestSpreeProducts:

    @pytest.fixture(autouse=True)
    def driver(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://demo.spreecommerce.org/us/en/products")
        time.sleep(3)
        yield self.driver
        logging.info("Testing is Completed")
        self.driver.quit()

    def test_click_product(self,driver):
        product = self.driver.find_element(By.XPATH, "//a[@href='/us/en/products/automatic-espresso-machine']")
        product.click()
        assert "Kitchen" in self.driver.page_source
        logging.info("Working as expected")
    def test_add_to_cart(self,driver):
        product = self.driver.find_element(By.XPATH, "//a[@href='/us/en/products/automatic-espresso-machine']")
        product.click()
        assert "Kitchen" in self.driver.page_source
        time.sleep(2)
        add_cart=self.driver.find_element(By.XPATH, "//button[@data-variant='default']")
        add_cart.click()
        # cart_box=self.driver.find_element(By.XPATH, "//a[@href='/us/en/checkout/cart_cjkfuasQi8']")
        # assert "Checkout22" in self.driver.page_source
        actual_text = self.driver.page_source
        expected_text = "Checkout22"

        assert expected_text in actual_text, f"Expected '{expected_text}' but got different content"
        logging.info("Working as expected")
