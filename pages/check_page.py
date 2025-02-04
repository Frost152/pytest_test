from base.base_class import Base
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CheckPage(Base):
    def __init__(self, driver):
        super().__init__(driver)

    # Locators
    carts = "//div[@class='cart_item']"
    price = ".//div[@class='inventory_item_price']"
    button = "//button[contains(@class, 'cart_button')]"

    # Getters
    def get_cart(self, seq):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.carts.format(seq))))

    def get_price(self, seq):
        return self.get_cart(seq).find_element(By.XPATH, self.price)

    def get_carts(self):
        return WebDriverWait(self.driver, 10).until(EC.visibility_of_all_elements_located((By.XPATH, self.carts)))

    def get_prices(self):
        return [i.find_element(By.XPATH, self.price) for i in self.get_carts()]

    def get_prices_text(self):
        return [i.text.strip("$") for i in self.get_prices()]

    def get_button(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.button)))

    # Actions

    def click_finish_button(self):
        self.get_button().click()

    # Methods
    def confirm_order(self, prices):
        assert self.get_prices_text() == prices
        self.click_finish_button()
        self.assert_word(self.get_title().text, "Checkout: Complete!")
        self.get_screen_shot()
        self.assert_url("https://www.saucedemo.com/checkout-complete.html")
        print("Заказ успешно сформирован")