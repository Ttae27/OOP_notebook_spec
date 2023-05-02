class User:
    def __init__(self, id: int, username: str, password: str, delivery_address: str, phone: str):
        self.__id = id
        self.__username = username
        self.__password = password
        self.__delivery_address = delivery_address
        self.__phone = phone
        self.__transaction_history = []

    def auth(self, username: str, password: str):
        if self.__username == username and self.__password == password:
            return True
        else:
            return False
        
    def add_transaction(self, transaction):
        self.__transaction_history.append(transaction)

    @property
    def username(self):
        return self.__username

    @property
    def phone(self):
        return self.__phone

    @property
    def delivery_address(self):
        return self.__delivery_address
    
    @property
    def id(self):
        return self.__id
    
    @property
    def transaction_history(self):
        transaction_dict = []
        for transaction in self.__transaction_history:
            transaction_dict.append(transaction.transaction)
        return self.__transaction_history