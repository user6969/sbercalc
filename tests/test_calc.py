from decimal import *
from utils.base_page import ConverterSection
from utils.conftest import *

URL = 'http://www.sberbank.ru/ru/quotes/converter'


@pytest.mark.parametrize('convert_from, convert_to, amount',
                         [('USD', 'RUB', '100'),
                          ('EUR', 'RUB', '7403.33'),
                          ('CHF', 'RUB', '100.23'),
                          ('RUB', 'EUR', '4444.50'),
                          ('RUB', 'USD', '2'),
                          ('RUB', 'CHF', '666.6')
                          ])
def test_c(browser, convert_from, convert_to, amount):
    browser.get(URL)
    converter = ConverterSection(browser)
    converter.select_amount(amount)
    converter.select_convert_from(convert_from, False)
    converter.select_convert_to(convert_to, False)
    converter.submit()
    result = converter.get_conversion_result()
    precision = Decimal(10) ** -2
    expected_result = (converter.get_exchange_rate()*Decimal(amount)).quantize(precision) \
        if convert_to == 'RUB' \
        else (Decimal(amount)/converter.get_revert_rate()).quantize(precision)
    assert expected_result == result
