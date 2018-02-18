#!/usr/bin/env python
# -*- coding: utf-8 -*-
from locators import *
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.action_chains import ActionChains as ac
from decimal import *



TIME_OUT = 20


class Utils(object):

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, TIME_OUT)

    def currency(self, value):
        return {
            'USD': PageLocators.USD,
            'RUB': PageLocators.RUB,
            'EUR': PageLocators.EUR,
            'JPY': PageLocators.JPY,
            'GBP': PageLocators.GBP,
            'CHF': PageLocators.CHF
        }[value]

    def code(self, value):
        return {
            '': PageLocators.RUB,
            '840': PageLocators.USD,
            '978': PageLocators.EUR,
            '392': PageLocators.JPY,
            '826': PageLocators.GBP,
            '756': PageLocators.CHF
        }[value]

    def select_amount(self, amount):
        field = self.wait.until(ec.presence_of_element_located((By.XPATH, PageLocators.amount)))
        field.clear()
        field.send_keys(amount)

    def select_convert_from(self, value, api):
        menu = self.wait.until(ec.presence_of_all_elements_located((By.TAG_NAME, PageLocators.convert_from_menu)))
        ac(self.driver).move_to_element(menu[0]).click(menu[0]).perform()
        option = self.wait.until(ec.presence_of_element_located((By.CSS_SELECTOR, self.currency(value)))) if not api\
            else self.wait.until(ec.presence_of_element_located((By.CSS_SELECTOR, self.code(value))))
        ac(self.driver).move_to_element(option).click(option).perform()

    def select_convert_to(self, value, api):
        menu = self.wait.until(ec.presence_of_all_elements_located((By.TAG_NAME, PageLocators.convert_to_menu)))
        ac(self.driver).move_to_element(menu[1]).click(menu[1]).perform()
        option = self.wait.until(ec.presence_of_element_located((By.CSS_SELECTOR, self.currency(value)))) if not api\
            else self.wait.until(ec.presence_of_element_located((By.CSS_SELECTOR, self.code(value))))
        ac(self.driver).move_to_element(option).click(option).perform()

    def submit(self):
        el = self.wait.until(ec.presence_of_element_located((By.XPATH, PageLocators.submit)))
        self.driver.execute_script("return arguments[0].scrollIntoView();", el)
        el.click()

    def get_exchange_rate(self):
        rate = self.wait.until(ec.presence_of_all_elements_located((By.CSS_SELECTOR, PageLocators.rate)))
        precision = Decimal(10) ** -2
        return Decimal(rate[0].text.replace(',', '.')).quantize(precision)

    def get_revert_rate(self):
        rate = self.wait.until(ec.presence_of_all_elements_located((By.CSS_SELECTOR, PageLocators.rate)))
        precision = Decimal(10) ** -2
        return Decimal(rate[1].text.replace(',', '.')).quantize(precision)

    def get_conversion_result(self):
        result = self.wait.until(ec.presence_of_element_located((By.CSS_SELECTOR, PageLocators.conversion_result)))
        precision = Decimal(10) ** -2
        return Decimal(result.text[0:-4].replace(',', '.').replace(' ', '')).quantize(precision)

    def move_to_login_page(self):
        login_link = self.wait.until(ec.presence_of_element_located((By.LINK_TEXT, PageLocators.login_link)))
        login_link.click()

    def login_page_loaded(self):
        login_page = self.wait.until(ec.presence_of_element_located((By.ID, PageLocators.login_page)))
        return login_page.is_displayed()

    def move_to_personal_page(self):
        login_link = self.wait.until(ec.presence_of_element_located((By.LINK_TEXT, PageLocators.personal_link)))
        login_link.click()

    def personal_page_loaded(self):
        p_page = self.wait.until(ec.presence_of_element_located((By.CLASS_NAME, PageLocators.personal_page)))
        return p_page.is_displayed()

    def check_private_banking_r_button(self):
        submit_button = self.wait.until(ec.presence_of_element_located((By.XPATH, PageLocators.submit)))
        button = self.wait.until(ec.presence_of_all_elements_located((By.XPATH, PageLocators.private_banking_r_button)))
        ac(self.driver).move_to_element(submit_button).move_to_element(button[1]).click(button[1]).perform()

    def error_displayed(self):
        error = self.wait.until(ec.presence_of_element_located((By.CLASS_NAME, PageLocators.error)))
        return error.is_displayed()
