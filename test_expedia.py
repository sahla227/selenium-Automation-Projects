
import logging
import pytest
import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestFlightTicket:

    @pytest.fixture(autouse=True)
    def driver(self):
        options = webdriver.ChromeOptions()
        options.add_argument("--disable-blink-features=AutomationControlled")

        self.driver = webdriver.Chrome(options=options)
        self.driver.maximize_window()
        self.driver.get("https://www.expedia.com/")

        yield self.driver

        logging.info("Testing is Completed")
        self.driver.quit()

    def test_click_flight_ticket(self, driver):
        wait = WebDriverWait(driver, 10)

        # Click Flights tab (better locator)
        flight = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//span[text()='Flights']"))
        )
        flight.click()

        # Verify page content
        wait = WebDriverWait(driver, 10)

        roundtrip = wait.until(
            EC.presence_of_element_located((By.XPATH, "//span[text()='Roundtrip']"))
        )

        assert roundtrip.is_displayed()
        logging.info("Working as Expected")
        # input_text=wait.until(
        #     EC.presence_of_element_located((By.NAME, "destination_select"))
        # )
    def test_booking(self, driver):
        wait = WebDriverWait(driver, 10)

        # Click Flights tab (better locator)
        flight = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//span[text()='Flights']"))
        )
        flight.click()

        # Verify page content
        wait = WebDriverWait(driver, 10)

        roundtrip = wait.until(
            EC.presence_of_element_located((By.XPATH, "//span[text()='Roundtrip']"))
        )

        assert roundtrip.is_displayed()

        time.sleep(10)
        text_search=self.driver.find_element(By.NAME, "destination_select")

        time.sleep(2)
        text_search.send_keys("Dubai")
        time.sleep(2)
        text_search.send_keys(Keys.ENTER)
        calendar = wait.until(
            EC.visibility_of_element_located((By.XPATH, "//span[text()='Sun']"))

        )

        time.sleep(2)
        assert calendar.is_displayed()
        logging.info("Working as Expected")
        time.sleep(2)
        date_15 = wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, "//div[@role='button'][.//div[text()='15']]")
            )
        )
        time.sleep(2)
        date_15.click()
        done=wait.until(EC.element_to_be_clickable(
            (By.XPATH,"//button[@data-stid='apply-date-selector']")
            )
        )
        done.click()
        search_button = wait.until(EC.element_to_be_clickable(
            (By.ID, "search_button")
            ))
        search_button.click()
        time.sleep(10)
        assert self.driver.title=='CNN to DXB flights333'
        logging.info("Testing is Completed")
        time.sleep(2)