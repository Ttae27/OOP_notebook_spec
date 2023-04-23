class PaymentProcessor:
    def __init__(self,payment_method,cart):
        self.payment_method = payment_method
        self.__paystatus = "Completed"
        self.__amount = cart.totalprice
        #ม่อนว่าถูกมั้ย บรรทัด 5 
        #เราว่าถกนะ เดะไปดตรงเรียกใช้อีกที  น้องเราร้องไห้อย่ เลยเสียงดัง
        #โดนตีอ่ะดิ ใช่มะ 55 555 ดดนขัดใจ ไม่ให้รีโมททีวึ
        #โอเคคคค
        #บ๊ายบายคับ
    @property
    def amount(self):
        return self.__amount
    
    def process_payment(self):
        if self.payment_method == "credit_card":
            return self.process_credit_card_payment()
        elif self.payment_method == "cash_transfer":
            return self.process_cash_Transfer_payment()
        else:
            return "payment error!"

    def process_credit_card_payment(self):
        card_number = input("Enter credit card number: ")
        expiration_date = input("Enter expiration date (MM/YY): ")
        cvv = input("Enter CVV: ")
        # Logic to process credit card payment
        print(f"Paid {self.__amount} by credit card.")
        self.__paystatus = 'Completed'
        return self.__paystatus

    def process_cash_Transfer_payment(self):
        cash = float(input("Enter amount of cash received: "))
        if cash < self.__amount:
            print("Not enough cash provided.")
            self.__paystatus = "Failed"
            return self.__paystatus
        else:
            change = cash - self.__amount
            print(f"Paid ${self.__amount} by cash tranfer. Balance: ${change:.2f}")
            self.__paystatus = "Completed"
            return self.__paystatus
        
# payment_ui = PaymentUI("credit_card", 50.0)