import datetime
class Paymentprocessing:
    def __init__(self,amount,transaction_id,payment_status):
        self.__amount = amount
        self.__created_on = datetime.date.today()
        self.__transaction_id = transaction_id
        self.__status = payment_status

