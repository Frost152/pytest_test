from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from pages.login_page import LoginPage

# Опции драйвера
# options = webdriver.ChromeOptions()
# options.add_experimental_option("detach", True)
# driver = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))


def test_loggin(browser):
    login = LoginPage(browser)
    login.open()
    login.authorization("standard_user", "secret_sauce")
    print(login.get_current_url())
    print('zalupa')