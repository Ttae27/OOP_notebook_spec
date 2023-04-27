from datetime import datetime
import random
class Payment():
    def __init__(self,build,payment,user):
        self.__build = build.build
        self.__amount = build.totalprice
        self.__current_user = user.current_user
        self.__created_on = datetime.now()
        self.__transaction_id = random.randint(1000000, 9999999)
        self.__status = payment.paystatus
        self.__transaction = []
        self.__lstbuild = []
    
    def get_data_from_build(self):
        for i in range(len(self.__build)):
            self.__lstbuild.append(self.__build[i].model)
    
    def data_payment(self):
        self.__date = self.__created_on.strftime("%d/%m/%Y")
        self.__time = self.__created_on.strftime('%H:%M:%S')
        self.get_data_from_build()
        self.__transaction.append(self.__transaction_id)
        self.__transaction.append(self.__current_user)
        self.__transaction.append(self.__lstbuild)
        self.__transaction.append(self.__date)
        self.__transaction.append(self.__time)
        self.__transaction.append(self.__amount)
        self.__transaction.append(self.__status)
        # self.__transaction_history.append([self.__transaction_id,self.__date,self.__time,self.__amount,self.__status])
        print ({'Transaction id': self.__transaction_id,'Date': self.__date,'Time': self.__time,'Build': self.__lstbuild,'Price': self.__amount,'Status': self.__status})
        return self.__transaction
        
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