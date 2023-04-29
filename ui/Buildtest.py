# from user.account import Account
# from user.user import User
from fastapi import FastAPI
from typing import Optional
from Build import *
from payment_processor import PaymentProcessor
from payment import Payment
from Product import *
from user.account import Account
from user.user import User
#!debug only pls remove after
product = Product()
build = Build(product) #build a basket
acc = Account()

p = User("1","Pearwa","LOLO","aHah","0954160491")
p.sign_up()
p.get_customer()

m = User("2","Mon","Gaga","Ladkrabang","0974936541")
m.sign_up()
m.get_customer()

t = User("3","Tae","Eiei","Ladkrabang","0123589865")


print(p.get_customer())
print(m.get_customer())

print(p.username)


acc.add_account(p)
acc.add_account(m)
acc.add_account(t)
acc.sign_in("Pearwa","LOLO")
# print(acc.allaccount)
# print(acc.allaccount[0].username)
# print(acc.allaccount[0].username)
# print(acc.allaccount[1].username)
# print(acc.allaccount[2].password)
# print(acc.login("Pearwa","LOLO"))

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
pay = Payment(build,payment,acc)
print(pay)
print(pay.data_payment())
