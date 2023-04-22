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


def get_product(cat: str) -> list:
    conn = sqlite3.connect('data/database.db')
    cursor = conn.cursor()
    item = cursor.execute(f"SELECT * FROM {cat}").fetchall()
    product_list = []
    
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

    for i in range(len(item)):
        product_list.append(class_cat(*item[i]))

    return product_list

def delete_data(cat, product_id):
    conn = sqlite3.connect('data/database.db')
    cursor = conn.cursor()
    query = f"DELETE from {cat} WHERE id = {product_id}"
    cursor.execute(query)
    conn.commit()

def update_price_data(cat, product_id, new_price):
    conn = sqlite3.connect('data/database.db')
    cursor = conn.cursor()
    query = f"UPDATE {cat} SET price = {new_price} WHERE id = {product_id}"
    cursor.execute(query)
    conn.commit()

def add_data(cat , product):
    conn = sqlite3.connect('data/database.db')
    cursor = conn.cursor()
    product = tuple(product.values())
    query = f"INSERT INTO {cat} VALUES {product}"
    cursor.execute(query)

def convert_to_class(cat, product):
        if cat == "case":
            return PC_Case(**product)
        elif cat == "cooling":
            return Cooling(**product)
        elif cat == "cpu":
            return CPU(**product)
        elif cat == "gpu":
            return GPU(**product)
        elif cat == "hdd":
            return HDD(**product)
        elif cat == "monitor":
            return Monitor(**product)
        elif cat == "motherboard":
            return Motherboard(**product)
        elif cat == "psu":
            return PSU(**product)
        elif cat == "ram":
            return RAM(**product)
        elif cat == "ssd":
            return SSD(**product)
        else:
            return None
