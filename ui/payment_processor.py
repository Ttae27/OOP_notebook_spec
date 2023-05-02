from ui.payment import Payment
class PaymentProcessor:
    def __init__(self, build: object) -> None:
        self.__build = build
        self.__amount = int(self.__build.totalprice)
        self.__current_transaction = 'None'
        
    
    def get_price(self):
        self.__amount = int(self.__build.totalprice)
    
    def select_payment(self, payment_method: str) -> str:
        self.__payment_method = payment_method
        if self.__payment_method == "credit_card":
            self.__current_transaction = 'credit_card'
            return self.__current_transaction
        elif self.__payment_method == "cash_transfer":
            self.__current_transaction = 'cash_transfer'
            return self.__current_transaction
        else:
            return "payment error!"

    def process_credit_card_payment(self, card_number: str, expiration_date: str, cvv: str, user: object) -> dict:
        if card_number == None or expiration_date == None or cvv == None:
            return {'Status': 'Fail'}
        user.add_transaction(Payment(self.__build, 'complete'))
        return {'Status': 'Complete'}

    def process_cash_Transfer_payment(self, cash: int, user: object) -> dict:
        self.get_price()
        if int(cash) != int(self.__amount):
            return {'Status': f'Please insert exact amount {self.__amount}'}
        else:
            user.add_transaction(Payment(self.__build, 'complete'))
            return {'Status': 'Complete'}

    @property
    def amount(self):
        return self.__amount