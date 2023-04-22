class Account:
    def __init__(self):
        # self.__username = username
        # self.__password = password
        self.__allaccount = []
    
    def add_account(self, account):
        self.allaccount.append(account)
    
    def dict_account(self,account):
        pass
    
    @property
    def allaccount(self):
        return self.__allaccount

# acc=[["Pearwa","LOLO","aHah"],["mon","Kaka","yaga"],["bo","jaja","papa"],["tae","kim","lala"]]