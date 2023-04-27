from datetime import datetime
class Payment:
    def __init__(self,amount,transaction_id,payment_status):
        self.__amount = amount
        self.__created_on = datetime.now()
        self.__transaction_id = transaction_id
        self.__status = payment_status
    
    @property    
    def data_payment(self):
        date = self.__created_on.strftime("%d/%m/%Y")
        time = self.__created_on.strftime('%H:%M:%S')
        return {'Transaction id': self.__transaction_id,'Date': date,'Time': time,'Amount': self.__amount,'Status': self.__status}