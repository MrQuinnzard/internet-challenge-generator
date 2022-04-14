import colorama
import random

def generate():
  mainObjects = ("A picture of your face","A badly greenscreened Tom Hanks","Steve","A Creeper","Horny Discord logo","Gacha character","Your IP address and bank information","SIS VS BRO","People Playground human")
  mainObject = random.choice(mainObjects)
  bgs = ("Charles O'Rear - Bliss","Minecraft base","beans","a Mario level","Geometry Dash","Your House","TABS Gameplay")
  bg = random.choice(bgs)
  overlays = ("A mind blown emoji","Random arrows/circles","The video title","Red text saying '3AM' with the creepster font","(NOT CLICKBAIT)","*COPS CALLED*","(channel logo)","blurred image","question marks","robtop","sad mario")
  overlay = random.choice(overlays)
  overlays2 = ("A mind blown emoji","Random arrows/circles","The video title","Red text saying '3AM' with the creepster font","(NOT CLICKBAIT)","*COPS CALLED*","(channel logo)","blurred image","question marks","robtop","sad mario")
  overlay2 = random.choice(overlays)

  print("Main Picture: " + mainObject)
  print("Background: " + bg)
  print("Overlay: " + overlay + " and " + overlay2)