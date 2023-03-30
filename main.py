from ui.Build import *
from ui.Catalog import *
from ui.Product import *
from user.user import *
from user.account import *
from user.admin import *
from user.information import *


def checkout():
    print(f"This is your build.")
    myBuild.view()
    print(f"Total price is {myBuild.totalPrice}")
    while True:
        user_input = input("Do you confirm your order? (y/n)\n")
        if user_input.lower() == "y":
            print("Proceed to payment") #!need to call payment function
            return True
        
        elif user_input.lower() == "n":
            print("Checkout cancel")
            return False
        
        else:
            print("invalid input. Please enter 'y' or 'n'.")

John_Doe_Eiei = User()
#
AMD_Ryzen_7800x3D = CPU("AMD_Ryzen_7800x3D", "B650", "3", "16500") 
Intel_Corei9_12900ks_Spacial_Edition = CPU("Core_i9-12900KS_Special_Edition","Core i9","3","28500")
#Main-board
MSI_B650M_AII = Motherboard("MSI_B650M_AII", "B650M-A II", "3" , "6590")
GIGABYTE_H510M_k = Motherboard("GIGABYTE_H510M_k","INTEL LGA1200","3","2150")

#GPU
RTX_4090 = GPU("RTX_4090", "Gaming X Trio", "3", "72900")
XFX_Radeon_RX_7900_XTX = GPU("XFX_Radeon_RX_7900_XTX", "RX 7900","3","37980") 

catalog = Catalog()
catalog.add_cpu(AMD_Ryzen_7800x3D)
catalog.add_cpu(Intel_Corei9_12900ks_Spacial_Edition)
catalog.add_motherboard(MSI_B650M_AII)
catalog.add_motherboard(GIGABYTE_H510M_k)
catalog.add_gpu(RTX_4090)
catalog.add_gpu(XFX_Radeon_RX_7900_XTX)

myBuild = Build()
John_Doe_Eiei.addBuild(myBuild)

myBuild.add_item(catalog.get_item(AMD_Ryzen_7800x3D))
myBuild.add_item(catalog.get_item(MSI_B650M_AII))
myBuild.add_item(catalog.get_item(RTX_4090))
myBuild.view()

John_Doe_Eiei.build.view()

checkout()