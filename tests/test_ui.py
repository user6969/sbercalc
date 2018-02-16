import pytest
from selenium import webdriver
from utils.pom import *

URL = 'http://www.sberbank.ru/ru/quotes/converter'


@pytest.yield_fixture(scope='session')
def browser():
    options = webdriver.ChromeOptions()
    options.add_argument("--kiosk")
    driver = webdriver.Chrome(chrome_options=options)
    yield driver
    driver.quit()


def test_navigate_to_login_page(browser):
    browser.get(URL)
    calcpage = CalcPage(browser)
    calcpage.move_to_login_page()
    loaded = True
    assert Utils(browser).login_page_loaded() == loaded


def test_navigate_to_personal_page(browser):
    browser.get(URL)
    calcpage = CalcPage(browser)
    calcpage.move_to_personal_page()
    loaded = True
    assert Utils(browser).personal_page_loaded() == loaded


def test_private_banking_option(browser):
    browser.get(URL)
    calcpage = CalcPage(browser)
    calcpage.select_convert_from('RUB', False)
    calcpage.select_convert_to('CHF', False)
    calcpage.check_private_banking_r_button()
    error_displayed = True
    assert Utils(browser).error_displayed() == error_displayed
