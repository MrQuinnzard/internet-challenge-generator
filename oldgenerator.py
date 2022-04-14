import random
import os
from colorama import Fore, Back, Style

def generate(): 
  challenges = ["Blow out 10 candles in one breath","Suck someone's toes","Play Minecraft","Play Fortnite","Eat Mentos after drinking Diet Coke","Jump off a cliff","Make yourself throw up","Use a Quija Board","Subscribe to stampylonghead","Prank call an Indian tech support scammer","Give your computer a virus","Escape spawn on the oldest anarchy server in Minecraft","Make a TikTok","Browse 4chan","Watch a sports game","Drive a car","Eat a giant breakfast burrito from Burger King","Skydive","Paint a portrait of Tom Brady","Dress as the opposite gender"]

  challenge = random.choice(challenges) 

  locations = ["at school","in public","at walmart","in your bathroom","at the gym","in a dark alley","in a dumpster","at church","on an airplane","on a bus","at the club","in a bar"," ","at a funeral","in a hospital","in front of Tom Brady","in a graveyard","at a stadium","on a train","at a train station","at your grandparents' house","in the McDonalds ball pit","at a playground","in a hotel","on the Statue of Liberty","in New York City","at a police station","in court","in a desert","on a family-friendly Minecraft server","In a crossdressing chamber"]

  location = random.choice(locations)

  modifiers = ["while on a sugar rush","while kissing a picture of Tom Brady","in your underwear","while wearing a bikini","while crossdressing","while cancelling a YouTuber","during the Super Bowl","while violating social distancing guidelines","during the World Series","during the Stanley Cup Final","at 3AM","while ordering fast food","while chugging a 2 liter bottle of Mountain Dew Code Red"," ","whilst wearing'eth a ye olde knight costume","while your house is on fire","while eating a dangerous amount of beans","During the NBA Championship","while under arrest","while your grandma is in the room","While looting a base on the oldest anarchy server in Minecraft"]

  modifier = random.choice(modifiers)

  creator = "Made by MrQuinnzard | youtube.com/channel/MrQuinnzardX"

  empty =" "
  print("currently running on: " + os.name)
  input1 = input("\n\n--Stupid internet challenge generator v1.0 | press ENTER to generate-- \n\n")

  if input1 == "32708":
    print("Wish Quinnzard a happy birthday!")
  else:
    print(Fore.BLUE + challenge)
    print(location)
    print(modifier)

  print(empty)
  print(empty)
  print(Fore.RED + 'Made by MrQuinnzard')
  print(empty)


