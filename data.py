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

#connect to database
conn = sqlite3.connect('data/database.db')
cursor = conn.cursor()

#create cooling list
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
item = cursor.execute("SELECT * FROM gpu").fetchall()
gpu_list = []
for i in range(len(item)):
    gpu_list.append(GPU(*item[i]))

#create hdd list
item = cursor.execute("SELECT * FROM hdd").fetchall()
hdd_list = []
for i in range(len(item)):
    hdd_list.append(HDD(*item[i]))

#create monitor list
item = cursor.execute("SELECT * FROM monitor").fetchall()
monitor_list = []
for i in range(len(item)):
    monitor_list.append(Monitor(*item[i]))

#create montherboard list
item = cursor.execute("SELECT * FROM motherboard").fetchall()
motherboard_list = []
for i in range(len(item)):
    motherboard_list.append(Motherboard(*item[i]))

#create pc_case list
item = cursor.execute("SELECT * FROM pc_case").fetchall()
pc_case_list = []
for i in range(len(item)):
    pc_case_list.append(PC_Case(*item[i]))

#create psu list
item = cursor.execute("SELECT * FROM psu").fetchall()
psu_list = []
for i in range(len(item)):
    psu_list.append(PSU(*item[i]))

#create ram list
item = cursor.execute("SELECT * FROM ram").fetchall()
ram_list = []
for i in range(len(item)):
    ram_list.append(RAM(*item[i]))

#create ssd list
item = cursor.execute("SELECT * FROM ssd").fetchall()
ssd_list = []
for i in range(len(item)):
    ssd_list.append(SSD(*item[i]))

def get_list(cat):
    match cat:
        case "cooling":
            return cooling_list
        
        case "cpu":
            return cpu_list
        
        case "gpu":
            return gpu_list
        
        case "hdd":
            return hdd_list
        
        case "monitor":
            return monitor_list
        
        case "motherboard":
            return motherboard_list
        
        case "pc_case":
            return pc_case_list
        
        case "psu":
            return psu_list
        
        case "ram":
            return ram_list
        
        case "ssd":
            return ssd_list
        
        case _:
            return "Invalid category"
