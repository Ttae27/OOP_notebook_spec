from data import *

class Account:
    def __init__(self):
        self.__allaccount = []
        self.__loginstatus = "Success"
    
    def sign_in(self, username: str, password: str):
        self.__allaccount = get_user()
        for account in self._allaccount:
            if account.username == username and account.password == password:
                return {"Status": "log in successfully"}
        return {"Status" : "Try again"}

    def get_allaccount(self,account):
        self.__allaccount = get_user()
    
    def login(self,username,password):
        for i in range(len(self.__allaccount)):
            if self.__allaccount[i].username == username and password == self.__allaccount[i].password:
                self.__loginstatus = "Success"
                break
            else:
                self.__loginstatus = "Failed"
        return self.__loginstatus
    
    @property
    def loginstatus(self):
        return self.__loginstatus
    
    @property
    def allaccount(self):
        return self.__allaccount
    
    # @property
    # def find_account(self):
    #     return self.__allaccount[0].username

# acc=[["Pearwa","LOLO","aHah"],["mon","Kaka","yaga"],["bo","jaja","papa"],["tae","kim","lala"]]