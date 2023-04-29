import tkinter as tk
import requests

class LoginGUI:
    def __init__(self, master):
        self.__master = master
        master.title("Login")

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

        # Create login button
        self.__login_button = tk.Button(master, text="Login", command=self.login)
        self.__login_button.pack()

        self.__status_label = tk.Label(master, text='')
        self.__status_label.pack()

    def login(self):
        username = self.__username_entry.get()
        password = self.__password_entry.get()

        credential = {'username': username, 'password': password}
        response = requests.post('http://localhost:8000/signin', json=credential)
        data = response.json()
        self.__status_label.config(text=f"{data}")

# Create GUI window
root = tk.Tk()
login_gui = LoginGUI(root)
root.mainloop()
