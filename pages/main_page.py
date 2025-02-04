from base.base_class import Base
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class MainPage(Base):
    def __init__(self, driver):
        super().__init__(driver)

    # Locators
    inventory_item_description = "(//div[@class='inventory_item_description'])[{}]"
    inventory_item_name = ".//div[@data-test='inventory-item-name']"
    inventory_item_desc = ".//div[@data-test='inventory-item-desc']"
    inventory_item_price = ".//div[@data-test='inventory-item-price']"
    inventory_item_add_button = ".//button[contains(@data-test, 'add-to-cart')]"
    inventory_item_remove_button = ".//button[contains(@data-test, 'remove')]"
    cart = "//a[@data-test='shopping-cart-link']"

    # Getters

    def get_item(self, seq):
        return WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.inventory_item_description.format(seq))))

    def get_item_name(self, seq):
        return self.get_item(seq).find_element(By.XPATH, self.inventory_item_name)

    def get_item_desc(self, seq):
        return self.get_item(seq).find_element(By.XPATH, self.inventory_item_desc)

    def get_item_price(self, seq):
        return self.get_item(seq).find_element(By.XPATH, self.inventory_item_price)

    def get_add_button(self, seq):
        return self.get_item(seq).find_element(By.XPATH, self.inventory_item_add_button)
        print('get_add_button')

    def get_remove_button(self, seq):
        return self.get_item(seq).find_element(By.XPATH, self.inventory_item_remove_button)

    def get_cart(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.cart)))

    # Actions

    def get_name_text(self, seq):
        return self.get_item_name(seq).text

    def get_desc_text(self, seq):
        return self.get_item_desc(seq).text

    def get_price_text(self, seq):
        return self.get_item_price(seq).text.strip('$')

    def click_add_button(self, seq):
        self.get_add_button(seq).click()
        assert self.get_remove_button(seq)

    def click_remove_button(self, seq):
        self.get_remove_button(seq).click()
        assert self.get_add_button(seq)

    def click_to_cart(self):
        self.get_cart().click()
        self.assert_word(self.get_title().text, "Your Cart")
        print('Переход в корзину успешен')

    # Methods
    def add_to_cart_one_elem(self, elem):
        self.click_add_button(elem)

    def remove_cart_one_elem(self, elem):
        self.click_remove_button(elem)

    def add_to_cart_many_elem(self, start, stop):
        for i in range(start, stop + 1):
            self.click_add_button(i)

    def remove_cart_many_elem(self, start, stop):
        for i in range(start, stop + 1):
            self.click_remove_button(i)

    def getting_prices(self, start, stop):
        a = []
        for i in range(start, stop + 1):
            a.append(self.get_price_text(i))
        return a
