class PaymentProcessor:
    def __init__(self,cart):
        self.__paystatus = "Completed"
        self.__amount = int(cart.totalprice)
        self.__current_transaction = 'None'
        
    @property
    def amount(self):
        return self.__amount
    
    def select_payment(self,payment_method):
        self.__payment_method = payment_method
        if self.__payment_method == "credit_card":
            self.__current_transaction = 'credit_card'
            return {self.__current_transaction}
        elif self.__payment_method == "cash_transfer":
            self.__current_transaction = 'cash_transfer'
            return self.__current_transaction
        else:
            return "payment error!"
    
    # def process_payment(self,current_transaction):
    #     self.__current_transaction = current_transaction
    #     if self.__current_transaction == "credit_card":
    #         return self.process_credit_card_payment()
    #     elif self.__current_transaction == "cash_transfer":
    #         return self.process_cash_Transfer_payment()
    #     else:
    #         return "payment error!"

    def process_credit_card_payment(self,card_number,expiration_date,cvv):
        # self.__card_number = card_number
        # self.__expiration_date = expiration_date
        # self.__cvv = cvv
        # Logic to process credit card payment
        # print(f"Paid {self.__amount} by credit card.")
        return {self.__paystatus}

    def process_cash_Transfer_payment(self,cash: int):
        self.__cash = cash
        return self.__amount
        if int(self.__cash) != int(self.__amount):
            # print("Not enough cash provided.")
            self.__paystatus = "Failed"
            return {self.__paystatus}
        else:
            
            # print(f"Paid ${self.__amount} by cash tranfer. Balance: ${change:.2f}")
            self.__paystatus = "Completed"
            return {self.__paystatus}
        
    @property
    def paystatus(self):
        return self.__paystatus
    
# payment_ui = PaymentUI("credit_card", 50.0)
    def paystatus(self):
        return self.__paystatus
    
# payment_ui = PaymentUI("credit_card", 50.0)