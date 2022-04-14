# ad generator v1.0 (beta)
# part of internet challenge generator version 5.0
# all code written by quinn jones

import os
os.system("pip install colorama")
import colorama
from colorama import Fore, Back, Style
import random
import time

def generateAd():
  thingsYouNeed = ["Do you need foundation repair?","Are you bad at grammar?","Are you bored?","Does nobody like you?","Tired of all the ads?","Do you need something to watch?",'Do you have a... "hair issue"?',"Do you have an issue with your lawn?","Wanna get revenge?","Do you like kids and/or animals?","Did you drop the soap?"]
  areYouBlank = random.choice(thingsYouNeed)
  productList = ["Grammarly can help!","Then get HOH SIS on the job!","Then watch MrQuinnzard X, retard!","Then watch this tutorial on how to be an influencer!","Well, assimilating into the hivemind may be just for you!","Get Stopify GOLD(TM).","Go to casserolemovies.com.","Well, get the new Lawnmower Prime!","Arson.","Go to jail.","Get Cyanox."]
  product = random.choice(productList)
  offerList = ["Try it now for $1.99!","And the best part? It's free!","Only $10.99/mo!","(note: your conciousness may be destroyed in the process)","Download it now and use code CASSEROLE for 10k Silver and an uber-mega-epic champion crystal.","Just select Beta Features on the main menu, and then Movie Generator.","100% no pain guarantee!","It's the best solution.","You deserve it.","End your suffering today."]
  offer = random.choice(offerList)
  advert = (areYouBlank + " " + product + " " + offer)
  print(Fore.YELLOW + advert)
  print(Style.RESET_ALL)

def advert_timer():
  # define the countdown func.
  def countdown(t):
      
      while t:
          mins, secs = divmod(t, 60)
          timer = '{:02d}:{:02d}'.format(mins, secs)
          print(timer, end="\r")
          time.sleep(1)
          t -= 1
        
      
    
    
  # input time in seconds
  t = 15
    
  # function call
  countdown(int(t))