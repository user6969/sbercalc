import pytest
from selenium import webdriver
from utils.pom import *
from utils.utils import Utils
from time import sleep
import pdb

URL = 'http://www.sberbank.ru/ru/quotes/converter'


@pytest.yield_fixture(scope='session')
def browser():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


@pytest.mark.parametrize('amount, convert_from, convert_to, result',
                            [('150', 'from_USD', 'to_RUB', 'result'),
                             ('200', 'from_RUB', 'to_USD', 'result')
                             ]
                         )
def test_calc(browser, amount, convert_from, convert_to, result):
    browser.get(URL)
    calcpage = CalcPage(browser, URL)
    calcpage.select_amount(amount)
    #pdb.set_trace()
    sleep(2)
    calcpage.select_convert_from(convert_from)
    calcpage.select_convert_to(convert_to)
    calcpage.submit()
    sleep(3)
    #pdb.set_trace()
    result = Utils(browser).get_conversion_result()
    expected_result = Utils(browser).get_exchange_rate()*int(amount)
    assert expected_result == result

