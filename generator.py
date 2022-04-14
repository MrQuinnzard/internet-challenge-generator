import casserole
import random
from colorama import Fore, Back, Style
import os
import sys
import plating

#list values

def generator():
  challenges = ["Blow out 10 candles in one breath","Suck someone's toes","Play Minecraft","Play Fortnite","Eat Mentos after drinking Diet Coke","Jump off a cliff","Make yourself throw up","Use a Quija Board","Subscribe to stampylonghead","Prank call an Indian tech support scammer","Give your computer a virus","Escape spawn on the oldest anarchy server in Minecraft","Make a TikTok","Browse 4chan","Watch a sports game","Drive a car","Eat a giant breakfast burrito from Burger King","Skydive","Paint a portrait of Tom Brady","Dress as the opposite gender",'Say "peenes" O-O',"Fix the Zero Point","Go to the bull riding concert"]


  locations = ["at school","in public","at walmart","in your bathroom","at the gym","in a dark alley","in a dumpster","at church","on an airplane","on a bus","at the club","in a bar"," ","at a funeral","in a hospital","in front of Tom Brady","in a graveyard","at a stadium","on a train","at a train station","at your grandparents' house","in the McDonalds ball pit","at a playground","in a hotel","on the Statue of Liberty","in New York City","at a police station","in court","in a desert","on a family-friendly Minecraft server","In a crossdressing chamber"]

  speciallocations = ["at VidCon","in Hell","on an active crime scene","at Quinnzard's House"]

  modifiers = ["while on a sugar rush","while kissing a picture of Tom Brady","in your underwear","while wearing a bikini","while crossdressing","while cancelling a YouTuber","during the Super Bowl","while violating social distancing guidelines","during the World Series","during the Stanley Cup Final","at 3AM","while ordering fast food","while chugging a 2 liter bottle of Mountain Dew Code Red"," ","whilst wearing'eth a ye olde knight costume","while your house is on fire","while eating a dangerous amount of beans","During the NBA Championship","while under arrest","while your grandma is in the room","While looting a base on the oldest anarchy server in Minecraft"]



  tiktokChallenges = ["copping a devious lick","holocaust roleplay","playing roblox scented con","touch my body challenge","banging my significant other",'( ͡° ͜ʖ ͡°) "bonding" with my step-sibling',"cooking with my tics","having a breakdown in front of my partner","convincing someone to bang me","bringing famous musicians back from the dead"]



  hashtags = ["#fyp","#gaming","#wholesome","#amogus","#memes","#pride","#blm","#adhd","#squidgame","#deviouslick","#fortnite"]



  fakeDisorderActions = ["cooking","having a breakdown","gaming","going to school","math class","eating","introducing"]



  fakeDisorders = ["with tourette's","with ADHD","with autism","with anorexia","with multiple personality disorder","my alters"]


  gachaCharacters = ["my oc","the bad girl","my mom","my rival","my best friend","the gacha disney character group","the bad boy"]



  gachaActions = ["has shreks with","reacts to","is in heat with","abuses","has a singing competition with","does the femboy challenge in front of"]



  gachaVideoTypes = [" | GLMM",""," | GLMV"]



  videoGames = ["Fortnite Chapter 3","Minecraft","Roblox Super Doomspire","Roblox Adopt Me","Cookie Clicker","BIT.TRIP FLUX","Geometry Dash","WorldBox","DOOM","Halo Infinite","Talking Ben","Yandere Simulator","Besiege","People Playground","Among Us","Skyrim","GTA V"]



  vgChallenges = ["Winning a Game of","Getting a Perfect Score in","Speedrunning","Beating","Winning a Tournament of","Finishing the campaign of","Playing","Watching the live event in"]

  vgModsMods = ["AMONG US","GIRLFRIEND","JENNY","PORN AND GORE","ITEMS PLUS","CASSEROLE","KAIZO","GUNS","MIDDLE AGES","TIME TRAVEL"]

  vgModsMod = random.choice(vgModsMods)

  vgMods = [("with the " + vgModsMod + " MOD..."),"Without Dying!","Without Taking Damage!","in less than 10 minutes!","at School!","but I can't say the letter E...","Without Damaging Enemies!"]



  howToTopics = ["How to change a diaper ","How to do math ","How to write a book ","How to deal with grief ","How to fall in love ","how to loop a dumb python thing "]



  howToModifiers = ["without getting covered in excrement","without getting arrested","in the modern day","while solving complex algebra","in Python 3.8","without being rejected"]





  vsauceCoreStrings = ["How to count past ","are connected to","Why we need","Do"]

  vsauceObjects = ["Communism","Guitar","Infinity","Chair","Among Us","The Fortnite Cube"]



  cringeActions = ["MADE BABIES WITH","KILLED","ASKED TO HAVE BABIES WITH","WANTS TO MAKE BABIES WITH","SLEPT WITH","DID THE CHARLIE CHARLIE CHALLENGE WITH","DID THE 24 HOUR CHALLENGE AT MCDONALDS WITH","FUCKING RAPED","MADE OUT WITH","IMPREGNATED","PLAYED SQUID GAME AGAINST","PLAYED SQUID GAME WITH"]

  firstPersons = ["I","SIRI","PENNYWISE","PEPPA PIG","THEGOLDNSHADOW","SATAN","JOE BIDEN","DONALD TRUMP","THE WHITE HOUSE","MRQUINNZARD X","THE CUBE QUEEN","THE ROCK","KEVIN THE FORTNITE CUBE"]

  secondPersons = ["ME","SIRI","PENNYWISE","PEPPA PIG","THEGOLDNSHADOW","SATAN","JOE BIDEN","DONALD TRUMP","THE WHITE HOUSE","MRQUINNZARD X","THE CUBE QUEEN","THE ROCK"]



  crngMods = ['AT 3AM',"IN FORTNITE","IN ROBLOX","IN MINECRAFT","WHILE ON THE RUN FROM JAIL","IN A DUMPSTER","WHILE OUR PARENTS ARE WATCHING...","AT MCDONALDS","FOR $2,147,483,648"]



  crngClaims = ["(NOT CLICKBAIT)","(COPS CALLED)","(GONE SEXUAL)","(GONE WRONG, SO VERY VERY WRONG)","(THIS SHOULDN'T EXIST...)","(WE DIED...)","(SOMEONE DIED...)"]

  prankFirstPeople = ["I","SIRI","PENNYWISE","PEPPA PIG","THEGOLDNSHADOW","SATAN","JOE BIDEN","DONALD TRUMP","THE WHITE HOUSE","MRQUINNZARD X","THE CUBE QUEEN","THE ROCK","KEVIN THE FORTNITE CUBE"]

  prankSecondPeople = ["ME","SIRI","PENNYWISE","PEPPA PIG","THEGOLDNSHADOW","SATAN","JOE BIDEN","DONALD TRUMP","THE WHITE HOUSE","MRQUINNZARD X","THE CUBE QUEEN","THE ROCK","A RANDOM STRANGER"]

  prankThirdPeople = ["ME","SIRI","PENNYWISE","PEPPA PIG","THEGOLDNSHADOW","SATAN","JOE BIDEN","DONALD TRUMP","THE WHITE HOUSE","MRQUINNZARD X","THE CUBE QUEEN","THE ROCK","RANDOM STRANGERS"]

  prankActions = ["PRANKED","POURED BLEACH IN THE MOUTH OF","COMMITTED ARSON AGAINST","HAD SEXUAL INTERCOURSE WITH THE MOTHER OF","PIEFACED","FUCKING KILLED"]

  prankClaims = ["(NOT CLICKBAIT)","(COPS CALLED)","(GONE SEXUAL)","(GONE WRONG, SO VERY VERY WRONG)","(THIS SHOULDN'T EXIST...)","(WE DIED...)","(SOMEONE DIED...)"]

  cookingTopics = ["Cooking", "How to Make","Making","Baking","Putting Together","Yesterday, I Asked You to Make","Attempting to please Gordon Ramsay with","Preparing","Food for Thought (or a cult ritual):","A Tutorial regarding the preparation of","Cooking Tutorial:"]

  cookingMods = ["a Vegan", "a Kosher", "a Low Carb","a perfectly normal","Cyanide-Infused","Your Mother's","Warm","a Platter of","a Keto","a Gluten-Free","a Tasty","a Sugar-Free","a Kid-Friendly"]

  cookingFoods = ["Cereal","Filet Mignon","Casserole","Vodka","Salad","Fruit Salad","Fruit Salad in a Life or Death situation","Smoothie","Tray of Cookies","Cake","Platter","Lamb for a Satanic Ritual","Burger","Pot of Human Flesh"]


  #condesation

  crngMod = random.choice(crngMods)
  crngClaim = random.choice(crngClaims)
  firstPerson = random.choice(firstPersons)
  secondPerson = random.choice(secondPersons)
  cringeAction = random.choice(cringeActions)
  vsauceObject = random.choice(vsauceObjects)
  vsauceObject2 = random.choice(vsauceObjects)
  vsauceCoreStr = random.choice(vsauceCoreStrings)
  howToModifier = random.choice(howToModifiers)
  howToTopic = random.choice(howToTopics)
  vgModifier = random.choice(vgMods)
  vgChallenge = random.choice(vgChallenges)
  videoGame = random.choice(videoGames)
  gachaVideoType = random.choice(gachaVideoTypes)
  gachaAction = random.choice(gachaActions)
  gachaCharacter = random.choice(gachaCharacters)
  gachaCharacter2 = random.choice(gachaCharacters)
  fakeDisorder = random.choice(fakeDisorders)
  fakeDisorderAction = random.choice    (fakeDisorderActions)
  hashtag = random.choice(hashtags)
  tiktokChallenge = random.choice(tiktokChallenges)
  modifier = random.choice(modifiers)
  normalLocation = random.choice(locations)
  specialLocationChoice = random.choice(speciallocations)
  specialLocation = Style.DIM + Back.RED + specialLocationChoice + Style.RESET_ALL
  prankFirstPerson = random.choice(prankFirstPeople)
  prankSecondPerson = random.choice(prankSecondPeople)
  prankThirdPerson = random.choice(prankThirdPeople)
  prankAction = random.choice(prankActions)
  prankClaim = random.choice(prankClaims)
  cookingTopic = random.choice(cookingTopics)
  cookingMod = random.choice(cookingMods)
  cookingFood = random.choice(cookingFoods)
  whatlocation =[normalLocation,normalLocation,normalLocation,normalLocation,normalLocation,normalLocation,normalLocation,normalLocation,normalLocation,specialLocation]

  location = random.choice(whatlocation)
  
  challenge = random.choice(challenges) 

  crngStr = (firstPerson + " " + cringeAction + " " + secondPerson + " " + crngMod + " " + crngClaim)

  howToStr = (howToTopic + howToModifier)

  prankStr = (prankFirstPerson + " AND " + prankSecondPerson + " " + prankAction + " " + prankThirdPerson + " " + prankClaim)

  cookingStr = (cookingTopic + " " + cookingMod + " " + cookingFood)

  #functions pertaining to flavor number 7
  if vsauceCoreStr == "How to count past ":
    vsauceStr = (vsauceCoreStr + vsauceObject)
  if vsauceCoreStr == "are connected to":
    vsauceStr = (vsauceObject + "s " + vsauceCoreStr + " " + vsauceObject2 + "s - Here's why.")
  if vsauceCoreStr == "Why we need":
    vsauceStr = (vsauceCoreStr + " " + vsauceObject + "s for " + vsauceObject2 + "s to Exist")
  if vsauceCoreStr == "Do":
    vsauceStr = (vsauceCoreStr + " " + vsauceObject + "s really exist? If so, how and why?")
  #intro message
  print(Style.DIM)
  print(Fore.BLUE + "internet challenge generator (version 6.0)")
  print("casserole v3.1 (three-bean 2)")
  print("tw: holocaust, eating disorders, police, sexuality")
  print(Fore.RED + "built (mainly) by quinnzard and dameon")
  print(Fore.GREEN + "currently running this program on " + os.name)
  print(Style.RESET_ALL)
  print("Select a category:")
  print("1: youtube")
  print("2: tiktok")
  print("3: other")
  print("4: casserole (all flavors/categories)")

  #add categories/challenge types
  category = input("choose a category and press ENTER")
  if category == "1":
      print()
      print("Flavors available for this category:")
      print("1: classic generation")
      print("2: video game challenge")
      print("3: vsauce")
      print("4: youtube kids (tw)")
      print("5: prank (tw)")
      print("6: cooking (NEW!)")
      challengeType = input("select a challenge type and press ENTER to generate...")
      if firstPerson == secondPerson and category == "1" and challengeType == "4":
        print()
        print(Fore.RED + "Uh Oh! It seems that both of the person randomizers produced the same result! Since some of the yt kids stuff cannot be done solo, unfortunately, we cannot successfully produce a quality title. Please re-roll to continue. (error code: 2)")
        crngStr = (Style.RESET_ALL)
      if challengeType == "1":
        print()
        print(Fore.YELLOW + challenge + ", " + location + ", " + modifier + ".")
      if challengeType == "2":
        print()
        print(Style.DIM + Fore.RED + vgChallenge + " " + videoGame + " " + vgModifier)
      if challengeType == "3":
        print(Fore.MAGENTA)
        print(vsauceStr)
      if challengeType == "4":
        print(Fore.RED)
        print(crngStr)
      if challengeType == "5":
        print(Fore.RED)
        print(prankStr)
      if challengeType == "6":
        print(cookingStr)
  if category == "2":
    print()
    print("Flavors available for this category:")
    print("1: tiktok")
    print("2: fake disorder cringe")
    challengeType = input("select a challenge type and press ENTER to generate...")
    if challengeType == "1":
      print(Fore.MAGENTA)
      print(tiktokChallenge + " " + location + " " + hashtag)
    if challengeType == "2":
      print(Fore.CYAN)
      print(fakeDisorderAction + " " + fakeDisorder + " " + hashtag)
  if category == "3":
    print()
    print("Flavors available for this category:")
    print("1: gacha cringe")
    print("2: tutorial")
    challengeType = input("select a challenge type and press ENTER to generate...")
    if challengeType == "1":
      print(Fore.LIGHTBLUE_EX)
      print(gachaCharacter + " " + gachaAction + " " + gachaCharacter2 + " " + gachaVideoType)
    if challengeType == "2":
      print(Fore.GREEN)
      print(howToStr)
  if category == "4": 
    casserole.casserole()

  if crngMod == "FOR $2,147,483,648" and category == "1" and challengeType == "4":
    sys.exit("OVERFLOW ERROR DETECTED, PROGRAM TERMINATED (error code: 1)")
  print(Style.RESET_ALL)
  plating_prompt = input("Generate thumbnail? y/n")
  if plating_prompt == "y":
    print()
    plating.generate()
    print()
    