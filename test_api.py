from ui.Product import *
from ui.Build import Build
import glob
from user.user import User
from user.admin import Admin
from ui.Catalog import Catalog
from fastapi import FastAPI
from typing import Optional
from compare import Compare


app = FastAPI()


John_Doe_Eiei = User()
Por_sud_tae = Admin("Agogfox")
#CPU
AMD_Ryzen_7800x3D = CPU("AMD_Ryzen_7800x3D", "B650", "3", "16500") 
Intel_Corei9_12900ks_Spacial_Edition = CPU("Core_i9-12900KS_Special_Edition","Core i9","3","28500")
#Mainboard
MSI_B650M_AII = Motherboard("MSI_B650M_AII", "B650M-A II", "3" , "6590")
GIGABYTE_H510M_k = Motherboard("GIGABYTE_H510M_k","INTEL LGA1200","3","2150")

#GPU
RTX_4090 = GPU("RTX_4090", "Gaming X Trio", "3", "72900")
XFX_Radeon_RX_7900_XTX = GPU("XFX_Radeon_RX_7900_XTX", "RX 7900","3","37980") 

catalog = Catalog()
catalog.add(AMD_Ryzen_7800x3D, AMD_Ryzen_7800x3D.type)
catalog.add(Intel_Corei9_12900ks_Spacial_Edition, Intel_Corei9_12900ks_Spacial_Edition.type)

catalog.add(MSI_B650M_AII, MSI_B650M_AII.type)
catalog.add(GIGABYTE_H510M_k, GIGABYTE_H510M_k.type)

catalog.add(RTX_4090, RTX_4090.type)
catalog.add(XFX_Radeon_RX_7900_XTX, XFX_Radeon_RX_7900_XTX.type)

my_build = Build()
John_Doe_Eiei.addBuild(my_build)

compare = Compare()

@app.get("/")
async def root():
    return {"Notebook": "Spec"}

@app.get("/pc-spec")
async def show_build():
    return {"Data": my_build}

@app.post("/pc-spec")
async def add_item(item, type):
    if type in catalog.catalog.keys():
        for i in catalog.catalog[type]:
            if i.model == item:
                my_build.add_item(catalog.get_item(i))
                return {"Data": "Successfully add!"}
    return {"Data": "Fail to add!"}

@app.delete("/pc-spec")
async def remove_item(item, type):
    if type in catalog.catalog.keys():
        for i in catalog.catalog[type]:
            if i.model == item:
                my_build.remove_item(catalog.get_item(i))
                return {"Data": "Successfully remove!"}
    return {"Data": "Fail to remove!"}

@app.get("/compare")
async def show_compare_item():
    spec_1, spec_2 = compare.compare_spec()
    return {"Spec_1": spec_1, "Spec_2": spec_2}

@app.post("/compare")
async def add_to_compare(item, type, i):
    # if type in catalog.catalog.keys():
    for j in catalog.catalog:
        if j.model == item:
            compare.add_item(j, i)
            return {"Data": "Successfully add!"}
    return {"Data": "Fail to add!"}

@app.delete("/pc-spec")
async def remove_data(item,type):
    count = 0
    for items in catalog.catalog[type]:
        if items.model == item:
            catalog.catalog[type][count] = {}
            return {"Edit" : catalog.catalog[type]}
        count += 1
    return {"Edit" : "Fail to Edit!"}

@app.delete("/del-product")
async def rm_product(item, type):
    catalog.remove(item, type)
    return {"remove": "remove success", "catalog" : catalog.catalog}

@app.put("/add-product")
async def add_product(item, type):
    catalog.add(item, type)
    return {"add" : "add success", "catalog" : catalog.catalog}

@app.post("/update-product")
async def update_product(item, new_warranty=None, new_price=None):
    catalog.update(item, new_warranty, new_price)
    return {"update" : "update success", "catalog" : catalog.catalog}
