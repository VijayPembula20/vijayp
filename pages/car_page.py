from selenium import webdriver
from selenium.common import UnexpectedAlertPresentException, NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class CarPage:
    URL =  "https://www.webuyanycar.com/car-valuation"
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)

    def open(self):
        self.driver.get(self.URL)
        self.driver.implicitly_wait(10)
        self.accept_cookies()
        self.driver.implicitly_wait(10)
        # self.clear_popups()

    def enter_registration(self, registration):
        reg_input = self.driver.find_element(By.XPATH, "//*[@id='vehicleReg']")
        reg_input.click()
        # reg_input.clear()
        reg_input.send_keys(registration)
        reg_input.send_keys(Keys.RETURN)

    def enter_mileage(self, mileage):
        reg_input = self.driver.find_element(By.ID, "mileageInput")
        reg_input.clear()
        reg_input.send_keys(mileage)
        reg_input.send_keys(Keys.RETURN)


    def get_car_details(self):
        registration = self.driver.find_element(By.ID, "registrationNumber")
        make = self.driver.find_element(By.ID, "make").text
        model = self.driver.find_element(By.ID, "model").text
        value = self.driver.find_element(By.ID, "value").text
        return {
            "registration": registration,
            "make": make,
            "model": model,
            "value": value,

        }

    def clear_popups(self):
        try:
            alert = self.driver.switch_to.alert
            alert.accept()
        except UnexpectedAlertPresentException:
            pass
        except NoSuchElementException:
            pass

        try:
            close_button = self.driver.find_element(By.CSS_SELECTOR, ".close")
            close_button.click()
        except NoSuchElementException:
            pass

    def accept_cookies(self):
        try:
            accept_button = self.driver.find_element(By.ID, "onetrust-accept-btn-handler")
            accept_button.click()
        except NoSuchElementException:
            pass


    def close(self):
        self.driver.quit()




