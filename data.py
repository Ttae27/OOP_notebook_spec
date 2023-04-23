import sqlite3

#*import data class
from data_class.cooling import Cooling
from data_class.cpu import CPU
from data_class.gpu import GPU
from data_class.hdd import HDD
from data_class.monitor import Monitor
from data_class.motherboard import Motherboard
from data_class.pc_case import PC_Case
from data_class.psu import PSU
from data_class.ram import RAM
from data_class.ssd import SSD
from user.user import User


def get_product(cat: str) -> list:
    conn = sqlite3.connect('data/database.db')
    cursor = conn.cursor()
    #select all product from cat table
    item = cursor.execute(f"SELECT * FROM {cat}").fetchall()
    product_list = []
    #Select classs according to parameter cat
    match cat:
        case "cooling":
            class_cat = Cooling
        case "cpu":
            class_cat = CPU
        case "gpu":
            class_cat = GPU
        case "hdd":
            class_cat = HDD
        case "monitor":
            class_cat = Monitor
        case "motherboard":
            class_cat = Motherboard
        case "pc_case":
            class_cat = PC_Case
        case "psu":
            class_cat = PSU
        case "ram":
            class_cat = RAM
        case "ssd":
            class_cat = SSD
    #append object to product_list
    for i in range(len(item)):
        product_list.append(class_cat(*item[i]))

    return product_list

def delete_data(cat: str, product_id: int) -> list:
    conn = sqlite3.connect('data/database.db')
    cursor = conn.cursor()
    #delete product from table cat
    query = f"DELETE from {cat} WHERE id = {product_id}"
    cursor.execute(query)
    conn.commit()
    return get_product(cat)

def update_price_data(cat: str, product_id: int, new_price: int) -> list:
    conn = sqlite3.connect('data/database.db')
    cursor = conn.cursor()
    #update price of product in cat table
    query = f"UPDATE {cat} SET price = {new_price} WHERE id = {product_id}"
    cursor.execute(query)
    conn.commit()
    return get_product(cat)

def add_data(cat: str , product: tuple) -> list:
    conn = sqlite3.connect('data/database.db')
    cursor = conn.cursor()
    #add row to cat table
    query = f"INSERT INTO {cat} VALUES {product}"
    cursor.execute(query)
    conn.commit()
    return get_product(cat)

def get_user():
    conn = sqlite3.connect('data/database.db')
    cursor = conn.cursor()
    user = cursor.execute(f"SELECT rowid, * FROM user").fetchall()
    user_list = []
    for i in range(len(user)):
        user_list.append(User(*user[i]))
    return user_list

def sign_up(user_data: tuple):
    conn = sqlite3.connect('data/database.db')
    cursor = conn.cursor()
    #add row to user table
    query = f"INSERT INTO user VALUES {user_data}"
    cursor.execute(query)
    conn.commit()
    return get_user()

def update_user_data(user_id: int, user_data: str, new_data):
    conn = sqlite3.connect('data/database.db')
    cursor = conn.cursor()
    #update data of user in user table
    query = f"UPDATE user SET {user_data} = {new_data} WHERE rowid = {user_id}"
    cursor.execute(query)
    conn.commit()
    return get_user()

def delete_user(user_id: int):
    conn = sqlite3.connect('data/database.db')
    cursor = conn.cursor()
    #delete user from table user
    query = f"DELETE from user WHERE rowid = {user_id}"
    cursor.execute(query)
    conn.commit()
    return get_user()