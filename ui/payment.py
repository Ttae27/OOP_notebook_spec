from datetime import datetime
import random
class Payment():
    def __init__(self,build: object,status: str) -> None:
        self.__build = build.build
        self.__amount = build.totalprice
        self.__created_on = datetime.now()
        self.__transaction_id = random.randint(1000000, 9999999)
        self.__status = status
        self.__transaction = self.payment_data()
    
    def get_data_from_build(self):
        lst = []
        for i in range(len(self.__build)):
            lst.append(self.__build[i].model)
        return lst
    
    def payment_data(self) -> dict:
        self.__date = self.__created_on.strftime("%d/%m/%Y")
        self.__time = self.__created_on.strftime('%H:%M:%S')
        model_list = self.get_data_from_build()
        transaction = {'Transaction id': self.__transaction_id,'Date': self.__date,'Time': self.__time,'Build': model_list,'Price': self.__amount,'Status': self.__status}
        return transaction
    
    @property
    def transaction(self):
        return self.__transaction
    
    @property
    def amount(self):
        return self.__amount
    
    @property
    def transaction_id(self):
        return self.__transaction_id
    
    @property
    def status(self):
        return self.__status
    
    @property
    def build(self):
        return self.__build
    
    @property
    def lstbuild(self):
        return self.__lstbuild