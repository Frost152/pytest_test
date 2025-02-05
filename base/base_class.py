from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from datetime import datetime
class Base:
    def __init__(self, driver):
        self.driver = driver

    """Метод получения текущего url"""

    def get_current_url(self):
        return self.driver.current_url

    """Метод проверки значения слова"""

    def assert_word(self, word, text):
        assert word == text
        print('Text assertion')

    """Метод проверки url"""

    def assert_url(self, url):
        assert self.driver.current_url == url
        print("URL верный")

    """Получение заголовка"""

    def get_title(self):
        return WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//span[@class='title']")))

    """Скриншот"""
    def get_screen_shot(self):
        postfix = datetime.now().strftime("%H-%M-%S")
        file_name = f"screenshot{postfix}.png"
        self.driver.save_screenshot(f"screen/{file_name}")
        # Запрос на изменение базового класса67

        еуые]
c