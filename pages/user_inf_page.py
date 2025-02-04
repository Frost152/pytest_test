from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from base.base_class import Base


class UserInfPage(Base):
    def __init__(self, driver):
        super().__init__(driver)

    # Locators
    first_name = "//input[@data-test='firstName']"
    last_name = "//input[@data-test='lastName']"
    zip_code = "//input[@data-test='postalCode']"
    continue_button = "//input[@data-test='continue']"

    # Getters
    def get_first_name(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.first_name)))

    def get_last_name(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.last_name)))

    def get_zip_code(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.zip_code)))

    def get_continue_button(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.continue_button)))

    # Actions

    def input_first_name(self, first_name):
        self.get_first_name().send_keys(first_name)

    def input_last_name(self, last_name):
        self.get_last_name().send_keys(last_name)

    def input_zip_code(self, zip_code):
        self.get_zip_code().send_keys(zip_code)

    def click_continue_button(self):
        self.get_continue_button().click()

    # Methods

    def fill_user_information(self, first_name, last_name, zip_code):
        self.input_first_name(first_name)
        self.input_last_name(last_name)
        self.input_zip_code(zip_code)
        self.click_continue_button()
        self.assert_word(self.get_title().text, "Checkout: Overview")
        print('Данные по пользователю заполнены')
