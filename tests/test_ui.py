from utils.base_page import NavigationSection, ConverterSection
from utils.conftest import *


URL = 'http://www.sberbank.ru/ru/quotes/converter'


def test_navigate_to_login_page(browser):
    browser.get(URL)
    browser.get(URL)
    navigation = NavigationSection(browser)
    navigation.move_to_login_page()
    loaded = True
    assert navigation.login_page_loaded() == loaded


def test_navigate_to_personal_page(browser):
    browser.get(URL)
    navigation = NavigationSection(browser)
    navigation.move_to_personal_page()
    loaded = True
    assert navigation.personal_page_loaded() == loaded


def test_private_banking_option(browser):
    browser.get(URL)
    converter = ConverterSection(browser)
    converter.select_convert_from('RUB', False)
    converter.select_convert_to('CHF', False)
    converter.check_private_banking_r_button()
    error_displayed = True
    assert converter.error_displayed() == error_displayed
