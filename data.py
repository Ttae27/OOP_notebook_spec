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

# def delete_product(cat, product_id):
#     conn = sqlite3.connect('data/database.db')
#     cursor = conn.cursor()

print(get_product('cpu'))