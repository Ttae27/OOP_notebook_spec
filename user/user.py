class User:
  def __init__(self,username,password,account):
    self.__username = username
    self.__password = password
    self.__account = account.acc
    self.datauser = []
  

  def get_account(self):
      return self.__account

  def sign_in(self):
      count = 0
      id_user = 0
      for user in self.__account:
            if user[0] == self.__username:
                  if self.__username == user[0] and self.__password == user[1]:
                        return f"Login succesed : {self.__username}"
                  else:
                        return "Error"
      return self.__username
#     return "Test a:% s b:% s" % (self.a, self.b) 

  def sign_up(self,username, password):
      pass
    
