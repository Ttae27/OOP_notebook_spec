import tkinter as tk

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

    def login(self):
        username = self.__username_entry.get()
        password = self.__password_entry.get()

        # Check if username and password are correct
        if username == "my_username" and password == "my_password":
            print("Login successful!")
        else:
            print("Invalid username or password.")

# Create GUI window
root = tk.Tk()
login_gui = LoginGUI(root)
root.mainloop()
