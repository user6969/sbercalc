import pytest
from selenium import webdriver
from utils.pom import *
from utils.utils import Utils


URL = 'http://www.sberbank.ru/ru/quotes/converter'


@pytest.yield_fixture(scope='session')
def browser():
    options = webdriver.ChromeOptions()
    options.add_argument("--kiosk")
    driver = webdriver.Chrome(chrome_options=options)
    yield driver
    driver.quit()


@pytest.mark.parametrize('amount, convert_from, convert_to',
                            [('1000', 'GBP', 'RUB'),
                             # ('100', 'EUR', 'RUB'),
                             # ('100', 'GBP', 'RUB')
                             ]
                         )
def test_calc(browser, amount, convert_from, convert_to):
    browser.get(URL)
    calcpage = CalcPage(browser)
    calcpage.select_amount(amount)
    calcpage.select_convert_from(convert_from)
    calcpage.select_convert_to(convert_to)
    calcpage.submit()
    result = Utils(browser).get_conversion_result()
    expected_result = Utils(browser).get_exchange_rate()*int(amount)
    assert expected_result == result

