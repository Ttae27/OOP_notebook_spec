import tkinter as tk

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

    def signup(self):
        username = self.__username_entry.get()
        password = self.__password_entry.get()
        address = self.__address_entry.get()
        phone = self.__phone_entry.get()

        # Save user information to a file or database
        with open("users.txt", "a") as file:
            file.write(f"{username},{password},{address},{phone}\n")

        # Print success message
        print("Sign up successful!")
        
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
