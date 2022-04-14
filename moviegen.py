# internet movie generator v1.1.0
# module for internet challenge generator v6
# code by quinn

import random
import colorama
from colorama import Fore, Back, Style

def createMovie():
  sequelNumber = random.randint(2,1000)
  moviestudionames = ["Marble","Warren Brothers","Casserole","BC","Daydream","Lamination","Voxar","Sanic","Polarmint","Tigerdoor","New Brine"]
  moviestudiosurnames = ["Studios","Productions","Animation","Entertainment","Films","Cinema","Corporation"]
  moviestudioname = random.choice(moviestudionames)
  moviestudiosurname = random.choice(moviestudiosurnames)
  moviestudio = (str(moviestudioname) + " " + (str(moviestudiosurname)))
  showMovieStudio = ["y","n"]
  showsMovieStudio = random.choice(showMovieStudio)
  if showsMovieStudio == "y":
    print(moviestudio, " Presents")
  adjs=["Distasteful","Sexy","Evil","Comedic","Vengeful","The Great","Space","Epic","Susan Wojicki's","Nexus"]
  adj = random.choice(adjs)
  shouldHaveAdjectives = ["y","n"]
  hasAdjective = random.choice(shouldHaveAdjectives)
  mainTitles = ["Stepbro","Fred","Gunfight","Flux","Police Box","Amazon Fufillment Center","Avengers","War","Space","Fight","Brawl","Foundation"]
  mainTitle = random.choice(mainTitles)
  subtitles = [": Endgame",": The Movie",": Zero Point",": Worlds Collide",": Origins"," of the Stars",": The Force Awakens",": Flipped",": Cubed",(" " + str(sequelNumber)),": A Star Wars Story"]
  subtitle = random.choice(subtitles)
  canHaveSubtitle = ["y","n"]
  hasSubtitle = random.choice(canHaveSubtitle)
  
  if hasAdjective == "y" and hasSubtitle == "y":
    movie = (adj + " " + mainTitle + subtitle)
  if hasAdjective == "n" and hasSubtitle == "n":
    movie = (mainTitle)
  if hasAdjective == "y" and hasSubtitle == "n":
    movie = (adj + " " + mainTitle)
  if hasAdjective == "n" and hasSubtitle == "y":
    movie = (mainTitle + subtitle)
  boiledPotatoScore = random.randint(0, 100)
  print(movie)
  print("Created by", (moviestudio))
  if boiledPotatoScore >= 80:
    print(Fore.GREEN)
  if 20 < boiledPotatoScore < 80:
    print(Fore.YELLOW)
  if boiledPotatoScore <= 20:
    print(Fore.RED)
  print("Boiled Potatoes score: " + str(boiledPotatoScore))

  print(Style.RESET_ALL)
  moviePrice = random.randint(1, 30)
  print("Buy now for $" + str(moviePrice) + " on CasseroleMovies")


