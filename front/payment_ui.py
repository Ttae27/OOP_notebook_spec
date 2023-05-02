# from Payment_processing import PaymentProcessor
# import tkinter as tk

# class PaymentUI:
#     def __init__(self, payment_method, amount):
#         self.payment_processor = PaymentProcessor(payment_method)
#         self.amount = amount
        
#         self.window = tk.Tk()
#         self.window.title("Payment Processor")
        
#         self.payment_method_label = tk.Label(self.window, text="Payment Method:")
#         self.payment_method_label.grid(row=0, column=0, padx=5, pady=5, sticky="w")
        
#         self.payment_method_var = tk.StringVar()
#         self.payment_method_var.set(payment_method)
#         self.payment_method_options = ["credit_card", "transaction", "cash_transfer"]
#         self.payment_method_dropdown = tk.OptionMenu(self.window, self.payment_method_var, *self.payment_method_options)
#         self.payment_method_dropdown.grid(row=0, column=1, padx=5, pady=5, sticky="w")
        
#         self.amount_label = tk.Label(self.window, text=f"Amount: ${amount:.2f}")
#         self.amount_label.grid(row=1, column=0, padx=5, pady=5, sticky="w")
        
#         self.pay_button = tk.Button(self.window, text="Pay", command=self.process_payment)
#         self.pay_button.grid(row=2, column=0, padx=5, pady=5, sticky="w")
        
#         self.paystatus_label = tk.Label(self.window, text="")
#         self.paystatus_label.grid(row=2, column=1, padx=5, pady=5, sticky="w")
        
#         self.window.mainloop()
        
#     def process_payment(self):
#         payment_method = self.payment_method_var.get()
#         paystatus = self.payment_processor.process_payment(self.amount)
#         self.paystatus_label.config(text=paystatus)
    
import tkinter as tk

class PaymentUI:
    def __init__(self, parent):
        self.parent = parent
        parent.minsize(width = 400,height=400)
        
        # create widgets
        self.payment_type_var = tk.StringVar()
        self.payment_type_var.set("credit card")
        
        self.payment_type_label = tk.Label(parent, text="Payment Type:")
        self.payment_type_label.pack()
        
        self.payment_type_credit_card_radio = tk.Radiobutton(parent, text="Credit Card",
                                                             variable=self.payment_type_var,
                                                             value="credit card")
        self.payment_type_credit_card_radio.pack()
        
        self.payment_type_cash_transfer_radio = tk.Radiobutton(parent, text="Cash Transfer",
                                                               variable=self.payment_type_var,
                                                               value="cash transfer")
        self.payment_type_cash_transfer_radio.pack()
        
        self.payment_amount_label = tk.Label(parent, text="Payment Amount:")
        self.payment_amount_label.pack()
        
        self.payment_amount_entry = tk.Entry(parent)
        self.payment_amount_entry.pack()
        
        self.submit_button = tk.Button(parent, text="Submit", command=self.submit_payment)
        self.submit_button.pack()
    
    def submit_payment(self):
        payment_type = self.payment_type_var.get()
        payment_amount = self.payment_amount_entry.get()
        
        # Perform payment
        if payment_type == "credit card":
            print(f"Performing credit card payment of {payment_amount} dollars.")
        elif payment_type == "cash transfer":
            print(f"Performing cash transfer payment of {payment_amount} dollars.")
    
    
root = tk.Tk()
payment_ui = PaymentUI(root)
root.mainloop()