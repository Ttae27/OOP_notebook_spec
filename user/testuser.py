from user.account import Account
from user.user import User
from fastapi import FastAPI
from typing import Optional
# kuy=Account("Pearwa","LOLO","aHah","0954160491")
# kuy=Account("Mon","Kaka","jojo","0214587896")

app = FastAPI()

p = User("Pearwa","LOLO","aHah","0954160491")
p.sign_up()
p.get_customer()

m = User("Mon","Gaga","Ladkrabang","0974936541")
m.sign_up()
m.get_customer()

t = User("Tae","Eiei","Ladkrabang","0123589865")

eiei =2

print(p.get_customer())
print(m.get_customer())

print(p.username)
acc = Account()


acc.add_account(p)
acc.add_account(m)
acc.add_account(t)
print(acc.allaccount)
print(acc.allaccount[0].username)
print(acc.allaccount[0].username)
print(acc.allaccount[1].username)
print(acc.allaccount[2].password)
print(acc.login("Pearwa","LOLO"))

# def namefunction():
#     pass



@app.get('/sign_up')
def get_user():
    lst = []
    for i in range(len(acc.allaccount)):
        lst.append({'id':i,'username': acc.allaccount[i].username,'password':acc.allaccount[i].password,'delivery_address':acc.allaccount[i].delivery_address,'phone':acc.allaccount[i].phone})

    return lst

@app.post('/sign_up')
def sign_up(username, password, delivery_address, phone):
    acc.add_account(User(username, password, delivery_address, phone))
    return {'sign up': "Successfully sign up"}

@app.post('/login')
def sign_in(username, password):
    if acc.login(username,password) == "Success":
        return {'sign in': "Successfully to sign in"}
    else:
        return {'sign in': "Failed to sign in"}

# print("___________________________________")
# print(t.sign_in("Pearwa","LOLO",acc.allaccount))

# print(acc.allaccount)

# macc = Account(p)
# pacc = Account(m)

# print(macc.listuser())
# print(pacc.listuser())



# print(u.get_customer())

# mutiacc = Account(u)


# uu = u.get_account("Pearwa","LOLO")

# print(kuy.get_acc())
# print(u.sign_in())
# print(u.get_account())
# print(uu)