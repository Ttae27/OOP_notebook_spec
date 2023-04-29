import tkinter as tk
import requests

class SignupGUI:
    def __init__(self, master):
        self.__master = master
        master.title("Sign Up")

        # Create username label and entry
        self.__username_label = tk.Label(master, text="Username:")
        self.__username_label.pack()
        self.__username_entry = tk.Entry(master)
        self.__username_entry.pack()

        # Create password label and entry
        self.__password_label = tk.Label(master, text="Password:")
        self.__password_label.pack()
        self.__password_entry = tk.Entry(master, show="*")
        self.__password_entry.pack()

        # Create address label and entry
        self.__address_label = tk.Label(master, text="Address:")
        self.__address_label.pack()
        self.__address_entry = tk.Entry(master)
        self.__address_entry.pack()

        # Create phone label and entry
        self.__phone_label = tk.Label(master, text="Phone:")
        self.__phone_label.pack()
        self.__phone_entry = tk.Entry(master)
        self.__phone_entry.pack()

        # Create sign up button
        self.__signup_button = tk.Button(master, text="Sign Up", command=self.signup)
        self.__signup_button.pack()

        self.__status_label = tk.Label(master, text='')
        self.__status_label.pack()

    def signup(self):
        username = self.__username_entry.get()
        password = self.__password_entry.get()
        address = self.__address_entry.get()
        phone = self.__phone_entry.get()

        user_data = {'username': username, 'password': password, 'delivery_address': address, 'phone': phone}
        response = requests.post('http://localhost:8000/signup', json=user_data)
        data = response.json()
        self.__status_label.config(text=f"{data}")
        
    @property
    def  username_entry(self):
        return  self.__username_entry
    
    @property
    def password_entry(self):
        return self.__password_entry
    
    @property
    def address_entry(self):
        return self.__address_entry
    
    @property
    def phone_entry(self):
        return self.__phone_entry

# Create GUI window
root = tk.Tk()
signup_gui = SignupGUI(root)
root.mainloop()
