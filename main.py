from ui.Product import *
from ui.Build import Build
import glob
from user.user import User
from user.admin import Admin
from ui.Catalog import Catalog

# John_Doe_Eiei = User()
# Por_sud_tae = Admin("Agogfox")
# #
# AMD_Ryzen_7800x3D = CPU("AMD_Ryzen_7800x3D", "B650", "3", "16500") 
# Intel_Corei9_12900ks_Spacial_Edition = CPU("Intel_Corei9_12900ks_Spacial_Edition","Core i9","3","28500")
# #Mainboard
# MSI_B650M_AII = Motherboard("MSI_B650M_AII", "B650M-A II", "3" , "6590")
# GIGABYTE_H510M_k = Motherboard("GIGABYTE_H510M_k","INTEL LGA1200","3","2150")

# #GPU
# RTX_4090 = GPU("RTX_4090", "Gaming X Trio", "3", "72900")
# XFX_Radeon_RX_7900_XTX = GPU("XFX_Radeon_RX_7900_XTX", "RX 7900","3","37980") 

# catalog = Catalog()
# catalog.add(AMD_Ryzen_7800x3D, AMD_Ryzen_7800x3D.type)
# catalog.add(Intel_Corei9_12900ks_Spacial_Edition, Intel_Corei9_12900ks_Spacial_Edition.type)

# catalog.add(MSI_B650M_AII, MSI_B650M_AII.type)
# catalog.add(GIGABYTE_H510M_k, GIGABYTE_H510M_k.type)

# catalog.add(RTX_4090, RTX_4090.type)
# catalog.add(XFX_Radeon_RX_7900_XTX, XFX_Radeon_RX_7900_XTX.type)
# catalog.remove(Intel_Corei9_12900ks_Spacial_Edition, Intel_Corei9_12900ks_Spacial_Edition.type)
# print(catalog.list("CPU"))
# print(catalog.catalog)
# print(catalog.get_item(AMD_Ryzen_7800x3D))
# print(RTX_4090)

# myBuild = Build()
# John_Doe_Eiei.addBuild(myBuild)

# John_Doe_Eiei.build.add_item(catalog.get_item(AMD_Ryzen_7800x3D))
# John_Doe_Eiei.build.add_item(catalog.get_item(MSI_B650M_AII))
# John_Doe_Eiei.build.add_item(catalog.get_item(RTX_4090))

# def add_item(item, type):
#     for i in catalog.catalog[type]:
#         if i.model == item:
#             John_Doe_Eiei.build.add_item(catalog.get_item(i))
#             return {"Data": "Successfully add!"}
#     return {"Data": "Fail to add!"}

# print(add_item("AMD_Ryzen_7800x3D", "CPU"))
# print(add_item("Intel_Corei9_12900ks_Spacial_Edition", "CPU"))
# John_Doe_Eiei.build.view()

cat = Catalog(Product())


