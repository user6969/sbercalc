from utils import Utils


class CalcPage(Utils):

    def select_amount(self, amount):
        Utils.select_amount(self, amount)

    def select_convert_from(self, convert_from, api):
        Utils.select_convert_from(self, convert_from, api)

    def select_convert_to(self, convert_to, api):
        Utils.select_convert_to(self, convert_to, api)

    def submit(self):
        Utils.submit(self)

    def get_exchange_rate(self):
        Utils.get_exchange_rate(self)
