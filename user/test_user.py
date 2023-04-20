from account import Account
from user import User
kuy=Account()
u = User("Pearwa","LOLO",kuy)
# uu = u.get_account("Pearwa","LOLO")

print(u.sign_in())
print(u.get_account())
# print(uu)