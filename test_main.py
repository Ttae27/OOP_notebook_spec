from ui.Product import *
from ui.Build import Build
import glob
from user.user import User
from user.admin import Admin
from ui.Catalog import Catalog

#
AMD_Ryzen_7800x3D = CPU("AMD_Ryzen_7800x3D", "B650", 3, 16500) 
Intel_Corei9_12900ks_Spacial_Edition = CPU("Intel_Corei9_12900ks_Spacial_Edition","Core i9",3, 28500)
#Mainboard
MSI_B650M_AII = Motherboard("MSI_B650M_AII", "B650M-A II", 3 , 6590)
GIGABYTE_H510M_k = Motherboard("GIGABYTE_H510M_k","INTEL LGA1200",3, 2150)

#GPU
RTX_4090 = GPU("RTX_4090", "Gaming X Trio", 3, 72900)
XFX_Radeon_RX_7900_XTX = GPU("XFX_Radeon_RX_7900_XTX", "RX 7900",3, 37980) 

catalog = Catalog()
catalog.add(AMD_Ryzen_7800x3D)
catalog.add(Intel_Corei9_12900ks_Spacial_Edition)

catalog.add(MSI_B650M_AII)
catalog.add(GIGABYTE_H510M_k)

catalog.add(RTX_4090)
catalog.add(XFX_Radeon_RX_7900_XTX)
# print(catalog.product_list)
print(catalog.get_product_list_type("CPU"))
# print(catalog.get_item("RTX_4090")._price)
# catalog.update(RTX_4090, any, 300)
# print(catalog.get_item("RTX_4090")._price)
# catalog.remove(Intel_Corei9_12900ks_Spacial_Edition, Intel_Corei9_12900ks_Spacial_Edition.type)

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
# #!!test
# catalog.remove("AMD_Ryzen_7800x3D","CPU")


# print(add_item("AMD_Ryzen_7800x3D", "CPU"))
# print(add_item("Intel_Corei9_12900ks_Spacial_Edition", "CPU"))
# John_Doe_Eiei.build.view()
