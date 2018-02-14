#!/usr/bin/env python
# -*- coding: utf-8 -*-
from selenium.webdriver.common.by import By


class PageLocators(object):
    amount = (By.XPATH, '//input[@placeholder="Сумма"]')
    select_from_menu = (By.NAME, 'converterTo')
    select_to_menu = (By.NAME, 'converterFrom')
    convert_from_menu = (By.TAG_NAME, 'em')
    convert_to_menu = (By.TAG_NAME, 'em')
    from_RUB = (By.XPATH, '//select[@name="convertFrom"]/option[text(), "RUB")]')
    from_USD = (By.XPATH, '//select[@name="convertFrom"]/option[text(), "USD")]')
    from_EUR = (By.XPATH, '//select[@name="convertFrom"]/option[text(), "EUR")]')
    from_CHF = (By.XPATH, '//select[@name="convertFrom"]/option[text(), "CHF")]')
    from_GBP = (By.XPATH, '//select[@name="convertFrom"]/option[text(), "GBP")]')
    from_JPY = (By.XPATH, '//select[@name="convertFrom"]/option[text(), "JPY")]')
    to_RUB = (By.XPATH, '//select[@name="convertTo"]/option[text(), "RUB")]')
    to_USD = (By.XPATH, '//select[@name="convertTo"]/option[text(), "USD")]')
    to_EUR = (By.XPATH, '//select[@name="convertTo"]/option[text(), "EUR")]')
    to_CHF = (By.XPATH, '//select[@name="convertTo"]/option[text(), "CHF")]')
    to_GBP = (By.XPATH, '//select[@name="convertTo"]/option[text(), "GBP")]')
    to_JPY = (By.XPATH, '//select[@name="convertTo"]/option[text(), "JPY")]')

    # RUB = (By.XPATH, '//span[contains(text(), "RUB")]')
    # USD = (By.XPATH, '//span[contains(text(), "USD")]')
    # EUR = (By.XPATH, '//span[contains(text(), "EUR")]')
    # CHF = (By.XPATH, '//span[contains(text(), "CHF")]')
    # GBP = (By.XPATH, '//span[contains(text(), "GBP")]')
    # JPY = (By.XPATH, '//span[contains(text(), "JPY")]')
    submit = (By.XPATH, '//*[contains(text(), "Показать")]')
    rate = (By.CSS_SELECTOR, 'span.rates-current__rate-value')
    conversion_result = (By.CSS_SELECTOR, 'span.rates-converter-result__total-to')

