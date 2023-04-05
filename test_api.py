from ui.Product import *
from ui.Build import Build
import glob
from user.user import User
from user.admin import Admin
from ui.Catalog import Catalog
from fastapi import FastAPI
from typing import Optional


app = FastAPI()


John_Doe_Eiei = User()
Por_sud_tae = Admin("Agogfox")
#
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

# @app.get("/pc-spec/catalog")
# async def show_catalog(type="CPU"):
#     return {"Catalog" : catalog.catalog[type]}

# @app.put("/pc-spec/catalog")
# async def edit_data(item, type):
#     count = 0
#     for items in catalog.catalog[type]:
#         if items.model == item:
#             return {"Edit" : catalog.catalog[type][count]}
#         count += 1
#     return {"Edit" : "Fail to Edit!"}


