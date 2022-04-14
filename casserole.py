import random
import sys
import os
import generator
import colorama
from colorama import Fore, Back, Style

#v6

def casserole():
  challenges = ["Blow out 10 candles in one breath","Suck someone's toes","Play Minecraft","Play Fortnite","Eat Mentos after drinking Diet Coke","Jump off a cliff","Make yourself throw up","Use a Quija Board","Subscribe to stampylonghead","Prank call an Indian tech support scammer","Give your computer a virus","Escape spawn on the oldest anarchy server in Minecraft","Make a TikTok","Browse 4chan","Watch a sports game","Drive a car","Eat a giant breakfast burrito from Burger King","Skydive","Paint a portrait of Tom Brady","Dress as the opposite gender"]

  challenge = random.choice(challenges) 

  locations = ["at school","in public","at walmart","in your bathroom","at the gym","in a dark alley","in a dumpster","at church","on an airplane","on a bus","at the club","in a bar"," ","at a funeral","in a hospital","in front of Tom Brady","in a graveyard","at a stadium","on a train","at a train station","at your grandparents' house","in the McDonalds ball pit","at a playground","in a hotel","on the Statue of Liberty","in New York City","at a police station","in court","in a desert","on a family-friendly Minecraft server","In a crossdressing chamber"]

  location = random.choice(locations)

  speciallocations = ["at VidCon","in Hell","on an active crime scene","at Quinnzard's House"]

  speciallocationChoice = random.choice(speciallocations)

  speciallocation = Back.RED + speciallocationChoice + Style.RESET_ALL

  modifiers = ["while on a sugar rush","while kissing a picture of Tom Brady","in your underwear","while wearing a bikini","while crossdressing","while cancelling a YouTuber","during the Super Bowl","while violating social distancing guidelines","during the World Series","during the Stanley Cup Final","at 3AM","while ordering fast food","while chugging a 2 liter bottle of Mountain Dew Code Red"," ","whilst wearing'eth a ye olde knight costume","while your house is on fire","while eating a dangerous amount of beans","During the NBA Championship","while under arrest","while your grandma is in the room","While looting a base on the oldest anarchy server in Minecraft"]

  modifier = random.choice(modifiers)

  tiktokChallenges = ["copping a devious lick","holocaust roleplay","playing roblox scented con","touch my body challenge","banging my gf",'( ͡° ͜ʖ ͡°) "bonding" with my stepbro',"cooking with my tics","having a breakdown in front of my gf","convincing someone to bang me","bringing famous musicians back from the dead"]

  tiktokChallenge = random.choice(tiktokChallenges)

  hashtags = ["#fyp","#gaming","#wholesome","#amogus","#memes","#pride","#blm","#adhd"]

  hashtag = random.choice(hashtags)

  fakeDisorderActions = ["cooking","having a breakdown","gaming","going to school","math class","eating"]

  fakeDisorderAction = random.choice(fakeDisorderActions)

  fakeDisorders = ["with tourette's","with ADHD","with autism","with anorexia","with multiple personality disorder"]

  fakeDisorder = random.choice(fakeDisorders)

  gachaCharacters = ["my oc","the bad girl","my mom","my rival","my best friend","the gacha disney character group"]

  gachaCharacter = random.choice(gachaCharacters)

  gachaCharacter2 = random.choice(gachaCharacters)

  gachaActions = ["has shreks with","reacts to","is in estrus with","abuses","has a singing competition with","does the femboy challenge in front of"]

  gachaAction = random.choice(gachaActions)

  gachaVideoTypes = [" | GLMM",""," | GLMV"]

  gachaVideoType = random.choice(gachaVideoTypes)

  videoGames = ["Fortnite Chapter 3","Minecraft","Roblox Super Doomspire","Roblox Adopt Me","Cookie Clicker","BIT.TRIP FLUX","Geometry Dash","WorldBox","DOOM","Halo Infinite","Talking Ben","Yandere Simulator","Besiege","People Playground","Among Us","Skyrim","GTA V"]

  videoGame = random.choice(videoGames)

  vgChallenges = ["Winning a Game of","Getting a Perfect Score in","Speedrunning","Beating","Winning a Tournament of","Finishing the campaign of","Playing"]

  vgChallenge = random.choice(vgChallenges)

  vgModsMods = ["AMONG US","GIRLFRIEND","JENNY","PORN AND GORE","ITEMS PLUS","CASSEROLE","KAIZO","GUNS","MIDDLE AGES","TIME TRAVEL"]

  vgModsMod = random.choice(vgModsMods)

  vgMods = [("with the " + vgModsMod + " MOD..."),"Without Dying!","Without Taking Damage!","in less than 10 minutes!","at School!","but I can't say the letter E...","Without Damaging Enemies!"]

  vgModifier = random.choice(vgMods)

  howToTopics = ["How to change a diaper ","How to do math ","How to write a book ","How to deal with grief ","How to fall in love "]

  howToTopic = random.choice(howToTopics)

  howToModifiers = ["without getting covered in excrement","without getting arrested","in the modern day","while solving complex algebra","in Python 3.8","without being rejected"]

  howToModifier = random.choice(howToModifiers)

  howToStr = (howToTopic + howToModifier)

  vsauceCoreStrings = ["How to count past ","are connected to","Why we need","Do"]

  vsauceObjects = ["Communism","Guitar","Infinity","Chair","Among Us"]

  vsauceObject = random.choice(vsauceObjects)

  vsauceObject2 = random.choice(vsauceObjects)

  vsauceCoreStr = random.choice(vsauceCoreStrings)

  cringeActions = ["MADE BABIES WITH","KILLED","ASKED TO HAVE BABIES WITH","WANTS TO MAKE BABIES WITH","SLEPT WITH","DID THE CHARLIE CHARLIE CHALLENGE WITH","DID THE 24 HOUR CHALLENGE AT MCDONALDS WITH","FUCKING RAPED","MADE OUT WITH","IMPREGNATED","PLAYED SQUID GAME AGAINST","PLAYED SQUID GAME WITH"]

  firstPersons = ["ME","SIRI","PENNYWISE","PEPPA PIG","THEGOLDNSHADOW","SATAN","JOE BIDEN","DONALD TRUMP","THE WHITE HOUSE","MRQUINNZARD X","THE CUBE QUEEN","THE ROCK"]

  secondPersons = ["ME","SIRI","PENNYWISE","PEPPA PIG","THEGOLDNSHADOW","SATAN","JOE BIDEN","DONALD TRUMP","THE WHITE HOUSE","MRQUINNZARD X","THE CUBE QUEEN","THE ROCK"]

  firstPerson = random.choice(firstPersons)

  secondPerson = random.choice(secondPersons)

  cringeAction = random.choice(cringeActions)

  crngMods = ['AT 3AM',"IN FORTNITE","IN ROBLOX","IN MINECRAFT","WHILE ON THE RUN FROM JAIL","IN A DUMPSTER","WHILE OUR MOMS ARE WATCHING...","AT MCDONALDS","FOR $2,147,483,648"]

  crngMod = random.choice(crngMods)

  crngClaims = ["(NOT CLICKBAIT)","(COPS CALLED)","(GONE SEXUAL)","(GONE WRONG, SO VERY VERY WRONG)","(THIS SHOULDN'T EXIST...)","(WE DIED...)","(SOMEONE DIED...)"]
  
  crngClaim = random.choice(crngClaims)

  crngStr = (firstPerson + " " + cringeAction + " " + secondPerson + " " + crngMod + " " + crngClaim)

  #functions pertaining to flavor number 7
  if vsauceCoreStr == "How to count past ":
    vsauceStr = (vsauceCoreStr + vsauceObject)
  if vsauceCoreStr == "are connected to":
    vsauceStr = (vsauceObject + "s " + vsauceCoreStr + " " + vsauceObject2 + "s - Here's why.")
  if vsauceCoreStr == "Why we need":
    vsauceStr = (vsauceCoreStr + " " + vsauceObject + "s for " + vsauceObject2 + "s to Exist")
  if vsauceCoreStr == "Do":
    vsauceStr = (vsauceCoreStr + " " + vsauceObject + "s really exist? If so, how and why?")

  #define "casserole"
  casseroleActions = [cringeAction,tiktokChallenge,challenge,vsauceCoreStr,howToTopic,vgChallenge,gachaAction]
  casseroleModifiers = [modifier,crngMod,howToModifier,vgModifier,fakeDisorder]
  casseroleLocations = [location,location,location,location,location,location,location,location,location,speciallocation]
  casseroleEnds = [crngClaim,gachaVideoType,hashtag]
  casserolePersonsAndThings = [firstPerson,secondPerson,gachaCharacter,gachaCharacter2,vsauceObject,vsauceObject2,videoGame]
  casseroleAction = random.choice(casseroleActions)
  casseroleLocation = random.choice(casseroleLocations)
  casseroleEnd = random.choice(casseroleEnds)
  casserolePersonOrThing = random.choice(casserolePersonsAndThings)
  anotherCasserolePersonOrThing = random.choice(casserolePersonsAndThings)
  casseroleModifier = random.choice(casseroleModifiers)
  locationchoice  = ["y","n"]
  locationOrNot = random.choice(locationchoice)
  modchoice = ["y","n"]
  modOrNot = random.choice(modchoice)

  #cooking up the casserole
  if casseroleAction == (vsauceCoreStr) and vsauceCoreStr == "How to count past ":
    finishedCasserole = (casseroleAction + casserolePersonOrThing + " " + casseroleEnd)
  if casseroleAction == (vsauceCoreStr) and vsauceCoreStr == "are connected to":
    finishedCasserole = (casserolePersonOrThing + " " + casseroleAction + " " + anotherCasserolePersonOrThing + " s- here's how")
  if casseroleAction == (vsauceCoreStr) and vsauceCoreStr == "Why we need":
    finishedCasserole = (casseroleAction + " " + casserolePersonOrThing + " for " + anotherCasserolePersonOrThing + " to exist")
  if casseroleAction == (vsauceCoreStr) and vsauceCoreStr == "Do":
    finishedCasserole = (casseroleAction + " " + casserolePersonOrThing + "s really exist? if so, how?")
  if casseroleAction == tiktokChallenge:
    finishedCasserole = (casseroleAction + " " + casseroleLocation + " " + casseroleEnd)
  if casseroleAction == cringeAction:
    finishedCasserole = (casserolePersonOrThing + " " + casseroleAction + " " + anotherCasserolePersonOrThing + " " + casseroleModifier + " " + casseroleEnd)
  if casseroleAction == (challenge):
    finishedCasserole = (casseroleAction + " " + casseroleModifier + " " + casseroleLocation + " " + casseroleEnd)
  if casseroleAction == (howToTopic) and locationOrNot == "y":
    finishedCasserole = (casseroleAction + " " + casseroleLocation + " " + casseroleModifier + " " + casseroleEnd)
  if casseroleAction == (howToTopic) and locationOrNot == "n":
    finishedCasserole = (casseroleAction + " " + casseroleModifier + " " + casseroleEnd)
  if casseroleAction == (vgChallenge):
    finishedCasserole = (casseroleAction + " " + casserolePersonOrThing + " " + casseroleModifier + " " + casseroleEnd)
  if casseroleAction == (gachaAction) and modOrNot == "y":
    finishedCasserole = (casserolePersonOrThing + " " + casseroleAction + " " + anotherCasserolePersonOrThing + " " + casseroleModifier)
  if casseroleAction == (gachaAction) and modOrNot == "n":
    finishedCasserole = (casserolePersonOrThing + " " + casseroleAction + " " + anotherCasserolePersonOrThing)
  print(finishedCasserole)    

