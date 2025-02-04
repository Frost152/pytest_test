import pytest

from pages.login_page import LoginPage
from pages.main_page import MainPage
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from pages.cart_page import CartPage
from pages.user_inf_page import UserInfPage
from pages.check_page import CheckPage

# Опции драйвера
# options = webdriver.ChromeOptions()
# options.add_experimental_option("detach", True)
# driver = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))


@pytest.mark.order(1)
def test_main_page(browser):

    login = LoginPage(browser)
    login.open()
    mp = login.authorization("standard_user", "secret_sauce")
    print(login.get_current_url())

    mp = MainPage(browser)
    mp.add_to_cart_many_elem(2, 6)
    prices = mp.getting_prices(2, 6)
    print(prices)
    # mp.remove_cart_many_elem(2,4)

    # mp.add_to_cart_one_elem(2)
    mp.click_to_cart()

    cp = CartPage(browser)
    cp.checkout_order()
    uip = UserInfPage(browser)
    uip.fill_user_information("Иван", "Иванов", "604667")
    check = CheckPage(browser)
    check.confirm_order(prices)


@pytest.mark.order(3)
def test_buy_one(browser):
    driver = browser
    print('Второй')
    log = LoginPage(driver)
    log.open()
    log.authorization("standard_user", "secret_sauce")

    mp = MainPage(driver)
    mp.add_to_cart_one_elem(1)


@pytest.mark.order(2)
def test_buy_two(browser):
    print('Третий')
    log = LoginPage(browser)
    log.open()
    log.authorization("standard_user", "secret_sauce")

    mp = MainPage(browser)
    mp.add_to_cart_one_elem(2)
