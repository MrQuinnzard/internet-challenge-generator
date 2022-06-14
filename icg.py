def internetChallengeGenerator():
  import os 
  os.system("pip install colorama")
  import generator
  import casserole
  import sys
  import random
  import colorama
  from colorama import Fore, Back, Style
  import adgen
  import time
  import moviegen
  import oldgenerator
  import plating

  os.system("clr")
  os.system("cls")
  os.system("clear")

  def showAdvertisement():
        os.system("clr")
        os.system("clear")
        os.system("cls")
        adgen.generateAd()
        print("Ad will be skippable in:")
        adgen.advert_timer()
        input("press ENTER to skip ad")
        os.system("clr")
        os.system("cls")
        os.system("clear")

  #license agreement
  print("-- LICENSE AGREEMENT --")
  print()
  print("The program you are running was created by the Casserole Team. This code is open-source, however, you must credit us when you use the code from the main program and/or the other modules. This code also may not be used for any illegal or unethical activities. Violating these terms will result in possible legal action.")
  print("If you do not agree to this, type 'n' and the program will terminate automatically. Otherwise, type 'y' to proceed.")
  print()
  agreement = input("Do you agree? Type your choice and press ENTER (y/n)")
  if agreement == "y":
    os.system("clr")
    os.system("clear")
    os.system("cls")
  if agreement == "n":
    sys.exit("License agreement not agreed to. Program terminated.")

  y = 1

  while y == 1:
    os.system("clr")
    os.system("clear")
    os.system("cls")
    print(Fore.BLUE + "INTERNET CHALLENGE GENERATOR - VERSION 6.01")
    print(Fore.LIGHTYELLOW_EX + "(c) 2022 Casserole Team")
    print(Style.RESET_ALL)
    adgen.generateAd()
    print()
    print("Proceed To Generator (1)")
    print("View Patch Notes (2)")
    print("Grab Bag/Quick Mode (generates 10 Casseroles and exits) (3)")
    print("Exit (4)")
    print("Credits (5)")
    menu = input("Choose an option.")
    if menu == "1":
      os.system("clr")
      os.system("clear")
      os.system("cls")
      print("Choose a version:")
      print("Stable (v6.0.0600-release) (1)")
      print("Classic (v1.0.0) (2)")
      print("Movie Generator (v1.1) (3)")
      generatorversion = input("Choose and option and click ENTER to continue")
      if generatorversion == '1':
        for x in range (2147483648):
          if x == 2147483648:
            sys.exit("WARNING: OVERFLOW ERROR, " +
            "RESTART TO CONTINUE (error code: 1)")
          generator.generator()
          print(Style.RESET_ALL)
          continue_prompt = input("Generate another challenge and/or thumbnail? Press Y to generate new challenge, or any other key to return to the menu.")
          if continue_prompt == "y":
            os.system("clr")
            os.system("clear")
            os.system("cls")
            continue
          else:
            break
          if continue_prompt == "y":
            os.system("clr")
            os.system("clear")
            os.system("cls")
          else:
            break
      if generatorversion == "2":
        for x in range (65536):
          if x == (65536):
            print("Overflow error, restart to continue")
          os.system("clr")
          os.system("clear")
          os.system("cls")
          oldgenerator.generate()
          continueprompt = input("We made v1.0 loopable. Press y to generate again.")
          if continueprompt == "y":
            continue
          else:
            break
            print(Style.RESET_ALL)
            continue_prompt = input("Generate another challenge? Press Y to generate new challenge, or any other key to return to the menu.")
            if continue_prompt == "y":
              os.system("clr")
              os.system("clear")
              os.system("cls")
              continue
            else:
              break
      if generatorversion == "3":
        for x in range (2147483648):
            if x == 2147483648:
              sys.exit("WARNING: OVERFLOW ERROR, " +
              "RESTART TO CONTINUE (error code: 1)")
            else:
              moviegen.createMovie()
              continueMovie = input("Continue generating? (y/any button + enter)")
            if continueMovie == "y":
              os.system("clr")
              os.system("clear")
              os.system("cls")
              continue
            else:
              break
    if menu == "2":
      print()
      print("Version 6.01 Patch Notes")
      print("- added to casserole collection")
      print("- bug fixes")
      print("- movie generator may be removed by 6.1")
      print()
      input("Press enter to continue...")
      os.system("clr")
      os.system("clear")
      os.system("cls")
      continue
    if menu == "3":
      print()
      for x in range (10):
        casserole.casserole()
        print()
      input("press enter to return to menu")
      os.system("clr")
      os.system("clear")
      os.system("cls")
      continue
    if menu == "ad":
      showAdvertisement()
      continue
    if menu == "4":
      y == 0
      break
    if menu == "5":
      os.system("clr")
      os.system("clear")
      os.system("cls")
      print("Internet Challenge Generator")
      print("Version 6.0")
      print("Casserole Version 3.1")
      print("Shell Version 2.1")
      print()
      print("--- Development Team ---")
      print("Quinn Jones")
      print("Dameon Gray")
      print()
      print("--- Testing ---")
      print("Rylee Bolte")
      print("Kyle Walz")
      print("The Solar Farm")
      print("4th Hour Odyssey 2021-22")
      print()
      print("--- Special Thanks ---")
      print("nkrs200")
      print("Lisa Rohrer")
      print("Josiah Ewers")
      print()
      input("Press ENTER to continue")
      continue
    else:
      continue

  #loop



