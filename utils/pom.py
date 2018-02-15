from utils import Utils


class CalcPage(Utils):

    def select_amount(self, amount):
        Utils.select_amount(self, amount)

    def select_convert_from(self, convert_from):
        Utils.select_convert_from(self, convert_from)

    def select_convert_to(self, convert_to):
        Utils.select_convert_to(self, convert_to)

    def submit(self):
        Utils.submit(self)

    def get_exchange_rate(self):
        Utils.get_exchange_rate(self)
