from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from base.base_class import Base


class CartPage(Base):
    def __init__(self, driver):
        super().__init__(driver)

    # Locators
    checkout_button = "//button[@data-test='checkout']"

    # Getters
    def get_checkout_button(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.checkout_button)))

    # Actions
    def click_checkout_button(self):
        self.get_checkout_button().click()

    # Methods
    def checkout_order(self):
        self.click_checkout_button()
        self.assert_word(self.get_title().text, "Checkout: Your Information")
        print("Заказ сформирован")
