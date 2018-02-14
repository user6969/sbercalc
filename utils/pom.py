from utils import Utils


class CalcPage(object):

    def __init__(self, driver, base_url):
        self.url = base_url
        self.driver = driver
        self.actions = Utils(driver)

    def select_amount(self, amount):
        self.actions.select_amount(amount)

    def select_convert_from(self, convert_from):
        self.actions.select_convert_from(convert_from)

    def select_convert_to(self, convert_to):
        self.actions.select_convert_to(convert_to)

    def submit(self):
        self.actions.submit()

    def get_exchange_rate(self):
        self.actions.get_exchange_rate()
