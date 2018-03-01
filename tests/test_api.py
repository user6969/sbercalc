import requests
import json
import csv
from decimal import *
from utils.base_page import ConverterSection
from utils.conftest import *

URL = 'http://www.sberbank.ru/ru/quotes/converter'
TEST_DATA = 'test_artifacts/currency.csv'


def currency_code(value):
    return {
        'RUB': '',
        'USD': '840',
        'EUR': '978',
        'JPY': '392',
        'GBP': '826',
        'CHF': '756'
    }[value]


def api_parameters():
    params = []
    with open(TEST_DATA, 'rb') as data_file:
        data = csv.reader(data_file)
        for row in data:
            api_params = [currency_code(x) for x in row[:-1]]
            api_params.append(row[2])
            params.append(tuple(api_params))
    return params


@pytest.mark.parametrize('convert_from, convert_to, amount', api_parameters())
def test_api(browser, convert_from, convert_to, amount):
    browser.get(URL)
    converter = ConverterSection(browser)
    converter.select_amount(amount)
    converter.select_convert_from(convert_from, api=True)
    converter.select_convert_to(convert_to, api=True)
    url = 'http://www.sberbank.ru/portalserver/proxy/?' \
          'pipe=shortCachePipe&' \
          'url=http%3A%2F%2Flocalhost%2Frates-web%2F' \
          'rateService%2Frate%2Fconversion%3F' \
          'regionId%3D77%26' \
          'sourceCode%3Dcard%26' \
          'destinationCode%3Daccount%26' \
          'exchangeType%3Dibank%26' \
          'servicePack%3Dempty%26' \
          'fromCurrencyCode%3D{}%26' \
          'toCurrencyCode%3D{}%26' \
          'amount%3D{}'.format(convert_from, convert_to, amount)
    r = requests.get(url)
    precision = Decimal(10) ** -2
    api_result = Decimal(json.loads(r.content)['amount']).quantize(precision)
    expected_result = (converter.get_exchange_rate()*Decimal(amount)).quantize(precision) \
        if convert_to == '' \
        else (Decimal(amount)/converter.get_revert_rate()).quantize(precision)
    assert api_result == expected_result
