from ui.payment import Payment
class PaymentProcessor:
    def __init__(self, build: object) -> None:
        self.__build = build
        self.__amount = int(self.__build.totalprice)

    def get_price(self):
        self.__amount = int(self.__build.totalprice)

    def process_credit_card_payment(self, card_number: str, expiration_date: str, cvv: str, user: object) -> dict:
        if card_number == None or expiration_date == None or cvv == None:
            return {'Status': 'Fail'}
        user.add_transaction(Payment(self.__build, 'complete'))
        return {'Status': 'Complete'}

    def process_cash_Transfer_payment(self, user: object) -> dict:
        user.add_transaction(Payment(self.__build, 'complete'))
        return {'Status': 'Complete'}

    @property
    def amount(self):
        return self.__amount