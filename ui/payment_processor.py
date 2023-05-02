from ui.payment import Payment
class PaymentProcessor:
    def __init__(self,build):
        self.__build = build
        self.__amount = int(self.__build.totalprice)
        self.__current_transaction = 'None'
        
    @property
    def amount(self):
        return self.__amount
    
    def get_price(self):
        self.__amount = int(self.__build.totalprice)
    
    def select_payment(self,payment_method):
        self.__payment_method = payment_method
        if self.__payment_method == "credit_card":
            self.__current_transaction = 'credit_card'
            return self.__current_transaction
        elif self.__payment_method == "cash_transfer":
            self.__current_transaction = 'cash_transfer'
            return self.__current_transaction
        else:
            return "payment error!"

    def process_credit_card_payment(self,card_number,expiration_date,cvv,user):
        if card_number == None or expiration_date == None or cvv == None:
            return {'Status': 'Fail'}
        user.add_transaction(Payment(self.__build, 'complete').data_payment())
        return {'Status': 'Complete'}

    def process_cash_Transfer_payment(self,cash: int, user):
        self.get_price()
        if int(cash) != int(self.__amount):
            return {'Status': f'Please insert exact amount {self.__amount}'}
        else:
            user.add_transaction(Payment(self.__build, 'complete').data_payment())
            return {'Status': 'Complete'}

