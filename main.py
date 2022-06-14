#casserole collection menu
#oh god it's happening
import insultGenerator
import os
import icg
from colorama import Fore, Back, Style
import py_thor
import sys
x = 1

print("The Casserole Collection v1.0")
print("by MrQuinnzard/The Casserole Team")
print()
input("Press ENTER to start")

def menu():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")
    
    print("Main Menu")
    print("Choose a generator:")
    print()
    print(Fore.YELLOW + "Internet Challenge Generator v6.0 (1)")
    print(Fore.MAGENTA + ".py_thor v2.1 (2)")
    print(Fore.RED + "Insult Generator (3)")
    print(Fore.LIGHTGREEN_EX + "EXIT (4)")
    print(Style.RESET_ALL)
    selection = input("Input the number of the generator you want to run.")
    if selection == "1":
        icg.internetChallengeGenerator()
    if selection == "2":
        if os.name == "nt":
            os.system("cls")
        else:
            os.system("clear")
        py_thor.pythor()
    if selection == "3":
        if os.name == "nt":
            os.system("cls")
        else:
            os.system("clear")
        insultGenerator.run()
    if selection == "4":
        sys.exit()

while x == 1:
    menu()


