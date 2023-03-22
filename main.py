from product import *
from product.cpu import CPU
from product.motherboard import Motherboard
from product.gpu import GPU
from ui import *
from ui.Build import Build
import glob


#
AMD_Ryzen_7800x3D = CPU("AMD Ryzen 7800x3D", "B650", "3", "16500") 
Intel_Corei9_12900ks_Spacial_Edition = CPU("Core i9-12900KS Special Edition","Core i9","3","28500")
#Mainboard
MSI_B650M_AII = Motherboard("AMD B650", "B650M-A II", "3" , "6590")
GIGABYTE_H510M_k = Motherboard("H510M-K","INTEL LGA1200","3","2150")

#GPU
RTX_4090 = GPU("GeForce RTX 4090 ", "Gaming X Trio", "3", "72,900")
XFX_Radeon_RX_7900_XTX = GPU("Radeon RX 7900 XT","RX 7900","3","37,980") 

myBuild = Build()

myBuild.addItem(AMD_Ryzen_7800x3D)
myBuild.addItem(MSI_B650M_AII)
myBuild.addItem(RTX_4090)
myBuild.view()
