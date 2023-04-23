# from account import Account
class User:
  def __init__(self,id, username,password,delivery_address,phone):
    self.__id = id
    self.__username = username
    self.__password = password
    self.__delivery_address = delivery_address
    self.__phone = phone
    self.__datauser = []
#     self.account = acc
  
  def sign_up(self):
    self.__datauser.append(self.__username)
    self.__datauser.append(self.__password)    
    self.__datauser.append(self.__delivery_address)
    self.__datauser.append(self.__phone)
  
#   @property
  def get_customer(self):
      return self.__datauser

  def sign_in(self,username,password,account):
    count = 0
    id_user = 0
    for user in account:
          if user[0] == username:
                if username == user[0] and password == user[1]:
                      return f"Login succesed : {username}"
                else:
                      return "Error"
    return "Error"
  
  #getter and setter
  @property
  def username(self):
      return self.__username

  @property
  def password(self):
      return self.__password

  @property
  def phone(self):
      return self.__phone
  @property
  def delivery_address(self):
      return self.__delivery_address
  
