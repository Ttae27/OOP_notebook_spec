from data import get_user, add_user, update_user_data, del_user

class Account:
    def __init__(self):
        self.__allaccount = get_user()
        self.__current_user = None

    def sign_up(self, user_data: tuple) -> dict:
        if add_user(user_data) == True:
            self.__allaccount = get_user()
            return {'Notify': 'Successfully sign up'}
        elif add_user(user_data) == False:
            return {'Notify': 'This username has been used'}
    
    def sign_in(self, username: str, password: str) -> dict:
        self.__allaccount = get_user()
        for account in self.__allaccount:
            if account.username == username:
                if account.auth(username, password):
                    self.__current_user = account
                    return {"Status": "log in successfully"}
                else:
                    return {"Status": "Incorrect password. Please try again."}

        return {"Status": "User does not exist. Do you want to sign up?"}

    def update_user(self, user_id: int, type: str, new_data) -> dict:
        if update_user_data(user_id, type, new_data):
            self.__allaccount = get_user()
            return {"Status": "update data successfully"}

        return {"Status": "Fail to update data"}

    def delete_user(self, user_id: int):
        if del_user(user_id):
            self.__allaccount = get_user()
            return {"Status": "delete successfully"}

        return {"Status": "Fail to delete user"}

    @property
    def allaccount(self):
        return self.__allaccount

    @property
    def current_user(self):
        return self.__current_user