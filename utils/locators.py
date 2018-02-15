#!/usr/bin/env python
# -*- coding: utf-8 -*-


class PageLocators(object):
    amount = '//input[@placeholder="Сумма"]'
    select_from_menu = 'converterTo'
    select_to_menu = 'converterFrom'
    convert_from_menu = 'em'
    convert_to_menu = 'em'
    from_RUB = '//select[@name="convertFrom"]//*[contains(text(), "RUB")]'
    RUB = 'div.visible > span:nth-child(1)'
    USD = 'div.visible > span:nth-child(6)'
    EUR = 'div.visible > span:nth-child(3)'
    CHF = 'div.visible > span:nth-child(2)'
    GBP = 'div.visible > span:nth-child(4)'
    JPY = 'div.visible > span:nth-child(5)'
    submit = '//*[contains(text(), "Показать")]'
    rate = 'span.rates-current__rate-value'
    conversion_result = 'span.rates-converter-result__total-to'

