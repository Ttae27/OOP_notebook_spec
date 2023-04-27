from data import *
class User:
  def __init__(self,username,password,delivery_address,phone):
    self.__id = 0
    self.__username = username
    self.__password = password
    self.__delivery_address = delivery_address
    self.__phone = phone
    self.__datauser = []
  
  def sign_up(self, user_data: tuple):
    return add_data(user_data)
  
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