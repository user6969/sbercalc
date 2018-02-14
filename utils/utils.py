from locators import *
import pdb


class Utils(object):

    def __init__(self, driver):
        self.driver = driver

    def select_amount(self, amount):
        field = self.driver.find_element(*PageLocators.amount)
        field.clear()
        field.send_keys(amount)

    def currency(self, value):
        return {
            'from_USD': PageLocators.from_USD,
            'from_RUB': PageLocators.from_RUB,
            'from_EUR': PageLocators.from_EUR,
            'from_JPY': PageLocators.from_JPY,
            'from_GBP': PageLocators.from_GBP,
            'from_CHF': PageLocators.from_CHF,
            'to_USD': PageLocators.to_USD,
            'to_RUB': PageLocators.to_RUB,
            'to_EUR': PageLocators.to_EUR,
            'to_JPY': PageLocators.to_JPY,
            'to_GBP': PageLocators.to_GBP,
            'to_CHF': PageLocators.to_CHF
        }[value]

    def select_convert_from(self, value):
        menu = self.driver.find_elements(*PageLocators.convert_from_menu)
        #self.driver.execute_script("return arguments[0].scrollIntoView();", menu[0])
        menu[0].click()
        pdb.set_trace()
        #self.driver.find_element(*self.currency(value)).click()
        option = self.driver.find_element(*self.currency(value))
        self.driver.execute_script("return arguments[0].scrollIntoView();", option)
        self.driver.execute_script("$(arguments[0]).click();", option)

    def select_convert_to(self, value):
        menu = self.driver.find_elements(*PageLocators.convert_to_menu)
        #self.driver.execute_script("return arguments[0].scrollIntoView();", menu[1])
        menu[1].click()
        pdb.set_trace()
        option = self.driver.find_element(*self.currency(value))
        self.driver.execute_script("return arguments[0].scrollIntoView();", option)
        self.driver.execute_script("$(arguments[0]).click();", option)

    def submit(self):
        el = self.driver.find_element(*PageLocators.submit)
        self.driver.execute_script("return arguments[0].scrollIntoView();", el)
        el.click()

    def get_exchange_rate(self):
        rate = self.driver.find_elements(*PageLocators.rate)
        return float(rate[0].text.replace(',', '.'))

    def get_conversion_result(self):
        #pdb.set_trace()
        result = self.driver.find_element(*PageLocators.conversion_result)
        return float(result.text[0:-4].replace(',', '.').replace(' ', ''))


find_element_by_xpath("//select[@name='element_name']/option[text()='option_text']").click()

span.selected:nth-child(3)
div.rates-aside__filter-block-line:nth-child(4) > div:nth-child(2) > div:nth-child(2) > div:nth-child(2) > span:nth-child(1)