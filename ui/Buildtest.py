# from user.account import Account
# from user.user import User
from fastapi import FastAPI
from typing import Optional
from Build import *
from Payment_processing import PaymentProcessor
from Payment_test import Payment
#!debug only pls remove after
product = Product()
build = Build(product) #build a basket

build.add_to_build('cpu', 6)#add product to basket
build.add_to_build('gpu', 11)
# build.add_to_build('gpu', 12)
build.add_to_build('ram',37)
build.remove_from_build(6)
build.cal_price(build.build)
# print(build.totalprice)

print("-----------Build Cart----------")

print(build.build) #return list of products that we add
print('cpu price is ' + str(build.build[0].price))
print('gpu price is ' + str(build.build[1].price))
# print(build.total_price(build.build))
# print(build.totalprice)



# build.total_price(build.build)
# print(build.totalprice)

payment = PaymentProcessor("credit_card",build)
# print(payment.amount)
print("-----------Payment Proceesing----------")
print(payment.process_payment())
print(payment.amount)
print(payment.paystatus)

print("-----------Payment Data----------")
print(Payment(build.totalprice,"1",payment.paystatus))
print(Payment(build.totalprice,"1",payment.paystatus).data_payment)