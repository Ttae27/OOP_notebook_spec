from ui.Product import *
from ui.Build import Build
import glob
from user.user import User
from user.admin import Admin
from ui.Catalog import Catalog

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

catalog = Catalog(Por_sud_tae)
catalog.add_cpu(AMD_Ryzen_7800x3D)
catalog.add_cpu(Intel_Corei9_12900ks_Spacial_Edition)
catalog.add_motherboard(MSI_B650M_AII)
# catalog.add_motherboard(GIGABYTE_H510M_k)
catalog.add_gpu(RTX_4090)
# catalog.add_gpu(XFX_Radeon_RX_7900_XTX)
catalog.remove_cpu(Intel_Corei9_12900ks_Spacial_Edition)

myBuild = Build()
John_Doe_Eiei.addBuild(myBuild)

myBuild.add_item(catalog.get_item(AMD_Ryzen_7800x3D))
myBuild.add_item(catalog.get_item(MSI_B650M_AII))
myBuild.add_item(catalog.get_item(RTX_4090))
myBuild.view()

John_Doe_Eiei.build.view()
