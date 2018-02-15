#!/usr/bin/env python
# -*- coding: utf-8 -*-
from locators import *
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.action_chains import ActionChains as ac
import pdb


TIME_OUT = 10


class Utils(object):

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, TIME_OUT)

    def select_amount(self, amount):
        field = self.wait.until(ec.presence_of_element_located((By.XPATH, PageLocators.amount)))
        field.clear()
        field.send_keys(amount)

    def currency(self, value):
        return {
            'USD': PageLocators.USD,
            'RUB': PageLocators.RUB,
            'EUR': PageLocators.EUR,
            'JPY': PageLocators.JPY,
            'GBP': PageLocators.GBP,
            'CHF': PageLocators.CHF
        }[value]

    def select_convert_from(self, value):
        menu = self.wait.until(ec.presence_of_all_elements_located((By.TAG_NAME, PageLocators.convert_from_menu)))
        ac(self.driver).move_to_element(menu[0]).click(menu[0]).perform()
        option = self.wait.until(ec.presence_of_element_located((By.CSS_SELECTOR, self.currency(value))))
        ac(self.driver).move_to_element(option).click(option).perform()

    def select_convert_to(self, value):
        menu = self.wait.until(ec.presence_of_all_elements_located((By.TAG_NAME, PageLocators.convert_to_menu)))
        ac(self.driver).move_to_element(menu[1]).click(menu[1]).perform()
        option = self.wait.until(ec.presence_of_element_located((By.CSS_SELECTOR, self.currency(value))))
        ac(self.driver).move_to_element(option).click(option).perform()

    def submit(self):
        el = self.wait.until(ec.presence_of_element_located((By.XPATH, PageLocators.submit)))
        self.driver.execute_script("return arguments[0].scrollIntoView();", el)
        el.click()

    def get_exchange_rate(self):
        rate = self.wait.until(ec.presence_of_all_elements_located((By.CSS_SELECTOR, PageLocators.rate)))
        return float(rate[0].text.replace(',', '.'))

    def get_conversion_result(self):
        result = self.wait.until(ec.presence_of_element_located((By.CSS_SELECTOR, PageLocators.conversion_result)))
        print result.text[0:-4].replace(',', '.').replace(' ', '')
        return float(result.text[0:-4].replace(',', '.').replace(' ', ''))

