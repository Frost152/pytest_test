from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from base.base_class import Base
from pages.main_page import MainPage

class LoginPage(Base):
    url = "https://www.saucedemo.com/"

    def __init__(self, driver):
        super().__init__(driver)

    # Locators
    login = (By.XPATH, "//input[@id='user-name']")
    password = (By.XPATH, "//input[@id='password']")
    button = (By.XPATH, "//input[@id='login-button']")

    # Getters
    def get_login_input(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.login))

    def get_password_input(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.password))

    def get_button(self):
        return WebDriverWait(self.driver, 10).until((EC.element_to_be_clickable(self.button)))

    # Actions
    def input_login(self, user_name):
        self.get_login_input().send_keys(user_name)
        print('Логин заполнен')

    def input_password(self, user_password):
        self.get_password_input().send_keys(user_password)

    def click_login_button(self):
        self.get_button().click()

    # Methods
    def open(self):
        self.driver.get(self.url)
        self.driver.maximize_window()
    def authorization(self, login_, password_):
        self.input_login(login_)
        self.input_password(password_)
        self.click_login_button()
        self.assert_word(self.get_title().text, "Products")
        self.assert_url("https://www.saucedemo.com/inventory.html")
        print('Авторизация прошла успешно')
        # return MainPage(self.driver, login_) тут тестировал передачу параметров на следующую страницу
