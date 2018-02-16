import pytest
import csv
from selenium import webdriver
from utils.pom import *
from utils.utils import Utils
from decimal import *

URL = 'http://www.sberbank.ru/ru/quotes/converter'
TEST_DATA = 'test_artifacts/currency.csv'


def parameters():
    params = []
    with open(TEST_DATA, 'rb') as data_file:
        data = csv.reader(data_file)
        for row in data:
            params.append(tuple(row))
    return params


@pytest.yield_fixture(scope='session')
def browser():
    options = webdriver.ChromeOptions()
    options.add_argument("--kiosk")
    driver = webdriver.Chrome(chrome_options=options)
    yield driver
    driver.quit()


@pytest.mark.parametrize('convert_from, convert_to, amount', parameters())
def test_calc(browser, convert_from, convert_to, amount):
    browser.get(URL)
    calcpage = CalcPage(browser)
    calcpage.select_amount(amount)
    calcpage.select_convert_from(convert_from, False)
    calcpage.select_convert_to(convert_to, False)
    calcpage.submit()
    result = Utils(browser).get_conversion_result()
    precision = Decimal(10) ** -2
    expected_result = (Utils(browser).get_exchange_rate()*Decimal(amount)).quantize(precision) if convert_to == 'RUB' \
        else (Decimal(amount)/Utils(browser).get_revert_rate()).quantize(precision)
    assert expected_result == result

