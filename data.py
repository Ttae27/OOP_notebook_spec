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
import sqlite3
#connect to database
conn = sqlite3.connect('data/database.db')
cursor = conn.cursor()

#create case list
item = cursor.execute("SELECT * FROM pc_case").fetchall()
case_list = []
for i in range(len(item)):
    case_list.append(Case(*item[i]))

#create case list
item = cursor.execute("SELECT * FROM cooling").fetchall()
cooling_list = []
for i in range(len(item)):
    cooling_list.append(Cooling(*item[i]))

#create cpu list
item = cursor.execute("SELECT * FROM cpu").fetchall()
cpu_list = []
for i in range(len(item)):
    cpu_list.append(CPU(*item[i]))

#create gpu list
# gpu_list = []
# for i in range(len(item)):
#     gpu_list.append(GPU(*item[i]))

# case_list = []
# for i in range(len(item)):
#     case_list.append(Case(*item[i]))

# case_list = []
# for i in range(len(item)):
#     case_list.append(Case(*item[i]))

# case_list = []
# for i in range(len(item)):
#     case_list.append(Case(*item[i]))

# case_list = []
# for i in range(len(item)):
#     case_list.append(Case(*item[i]))

# case_list = []
# for i in range(len(item)):
#     case_list.append(Case(*item[i]))

# case_list = []
# for i in range(len(item)):
#     case_list.append(Case(*item[i]))

def get_list(cat):
    if cat == "case":
        return case_list
    elif cat == "cooling":
        return cooling_list
    elif cat == "cpu":
        return cpu_list
    elif cat == "gpu":
        pass
        #todo continue until end