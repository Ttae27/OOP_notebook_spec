class Payment:
    def __init__(self, build):
        self.amount = build.totalPrice
        
    def paid_by_credit_card(self):
        # code to process credit card payment goes here
        card_number = input("card_number:")
        if len(card_number) != 13:
            print("Invalid Card Number, please recheck your Card Number")
        else:
            print(f"Paid ${self.amount} by credit card ({card_number})")

    def paid_by_cashtransfer(self):
        # code to process card transaction payment goes here
        cash = int(input("cash:"))
        if cash < self.amount:
            print("Not enough cash provided.")
        else:
            change = cash - self.amount
            print(f"Paid ${self.amount} by cash tranfer. Balance: ${change:.2f}")

    def use_coupon(self):
        coupon_check = input("Coupon? y/n : ")
        if coupon_check == "y":
            coupon_code = input("coupon: ")
            if coupon_code == "sugardaddy":
                discount = self.amount * 0.1
                self.amount -= discount
                print(f"Discount applied: ${discount:.2f}. New total: ${self.amount:.2f}")
            else:
                print("Invalid coupon code.")
        else:
            print("No Discount applied")
            
    def pay_status(self):
        pass

            