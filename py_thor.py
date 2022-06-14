def pythor():
  import random
  import os
  from colorama import Fore, Back, Style
  v = 1
  while v == 1:
    rtrnAndRvngCharList = ["The Great Devourer","Pythor","Lord Garmadon","Captain Soto","Techno-Wu","Kryptor","The Overlord","Master Chen","Clouse","Morro","Nadakhan","The Quiet One","Mr. E","The Stone Army","Samukai"]
    rtrnAndRvngChar = random.choice(rtrnAndRvngCharList)
    newJitzuTypes = ["Drill","Rod","Steel","Time","Sneak","Sword","Dew","Warp","Fang","Droid","Quake","Flame","Cold","Zap","Djinn","Gun","Sun","Moon","Tea","Storm","Kill","Sea"]
    newJitzuAdjs = ["Forbidden","Dark","Ancient","Oni","Dragon","Serpentine","Super","Forgotten","Master","Deadly","Infernal","Golden"]
    jitzufu = ["jitzu","-Fu","jitzufu","wondo"]
    newJitzu = (random.choice(newJitzuAdjs) + " " + random.choice(newJitzuTypes) + random.choice(jitzufu))
    collectibleTypes = ("Weapons","Blades","Staff","Masks","Mech","Dragons","Sports Cars","Scroll","Scrolls")
    collectibleType = random.choice(collectibleTypes)
    collectibleAdjs = ["Golden","Techno","Oni","Time","Elemental","Djinn","Aero","Cursed","Ghostly","Dragon","Doom","Death","Dark","Corruption","Elder"]
    collectibleAdj = random.choice(collectibleAdjs)
    collectible = (collectibleAdj + " " + collectibleType)
    villainGoalAdjList = ["Golden","Serpent","Dragon","Oni","Airjitzu","Spinjitzu","Burning","Freezing","Quake","Electric","Wave","Dark","Time","Djinn","Techno","Mountain","Curse","Ghost","Ultimate","Elemental"]
    villainGoalAdj = random.choice(villainGoalAdjList)
    villainGoalNounList = ["Master","Lord","Arbiter","Sorcerer","King","Destroyer"]
    villainGoalNoun = random.choice(villainGoalNounList)
    villainGoal = (villainGoalAdj + " " + villainGoalNoun)
    
    def title():
      nouns4BlankApostropheD = ["Wreck","Crystallize","Djinn","Ice","Slice","Ninja","Possess","Wish","Warp"]
      noun4BAD = random.choice(nouns4BlankApostropheD)
      blkAposD = (noun4BAD + "'d")
      ninjaColors = ["Red","Blue","Teal","Green","White","Black","Gold","Pink","Brown","Fire","Ice","Water","Lightning","Earth","Energy","Titanium","Wind"]
      ninjaColor = random.choice(ninjaColors)
      legacyOTBlankNinja = ("Legacy of the " + ninjaColor + " Ninja")
      characterList = ["Kai","Jay","Zane","Cole","Lloyd","Nya","Wu","Garmadon","Pythor","The Great Devourer","Dareth","The Overlord","Clouse","Skylor","Master Chen","Morro","Nadakhan","The Quiet One","Meowthra","Sensei Yang","La-Loyd"]
      charForBlkApostropheSLeg = random.choice(characterList)
      blkAposSLeg = (charForBlkApostropheSLeg + "'s Legacy")
      blkAposSTeas = (charForBlkApostropheSLeg + "'s Teas")
      blkAposSRvng = (rtrnAndRvngChar + "'s Revenge")
      eventList = ["Tournament","Gauntlet","Festival","War","Battle","Game","Tomb","Hands","Fall of","Curse"]
      blkOfBlkEvnt = random.choice(eventList)
      eventTopicList = ["Elements","Spinjitzu","Time","Darkness","Brown","Wind","Fire","Ice","Water","Storms","Evil","Secrets","Green"]
      blkOfBlkEvntTopic = random.choice(eventTopicList)
      blkOfBlk = (blkOfBlkEvnt + " of " + blkOfBlkEvntTopic)
      riseOfBlkList = [charForBlkApostropheSLeg, ("The " + ninjaColor + " Ninja")]
      riseOfBlk = ("Rise of " + random.choice(riseOfBlkList))
      blkBoundList = ["Re","Hell","Star","Moon",(blkOfBlkEvntTopic + " in"),"War"]
      blkBoundFiller = random.choice(blkBoundList)
      blkBound = (blkBoundFiller + "bound")
      scrtLgndOrWtvrTfTheNewTngsHave = ["Secret","Secrets","Legend","Mystery","Return"]
      iHateTheGoddamnRandomModule = [collectible,newJitzu]
      BlkOfTheBlk = (random.choice(scrtLgndOrWtvrTfTheNewTngsHave) + " of the " + random.choice(iHateTheGoddamnRandomModule))
      seasonTitleTypes = [blkAposD,legacyOTBlankNinja,blkAposSLeg,blkAposSRvng,blkOfBlk,blkAposSTeas,riseOfBlk,blkBound,BlkOfTheBlk]
      title = random.choice(seasonTitleTypes)
      print("Ninjago Season " + str(random.randint(16,1000)) + ": " + title)
    def synopsis():
      newVilAdjs = ["Dark","Time","Infernal","Platinum","Crystal","Skeleton","Serpentine","Black","Crimson","Azure","Chartreuse","All-Consuming","Nindroid","Stone","Tech","Corrupted"]
      newVilAdj = random.choice(newVilAdjs)
      newVilNouns = ["Master","Mafia","Lord","Army","Gang","Sorcerer","Boss","King","Swordsman","Samurai","Ninja"]
      newVilNoun = random.choice(newVilNouns)
      newVil = (newVilAdj + " " + newVilNoun)
      ninja = ("Lloyd","Kai","Jay","Zane","Cole","Nya","Dareth","La-Loyd")
      focusNinja = random.choice(ninja)

      saveNinjago = (rtrnAndRvngChar + " has returned, and this time with a new accomplice: the " + newVil + ". Luckily, " + focusNinja + " and the gang have learned a new power: " + newJitzu + ". Together, they will find the " + collectible + ", and use this new force to defeat the evil and save Ninjago once again.")
      stopVil = (focusNinja + " and the ninja must stop " + rtrnAndRvngChar + " from collecting the " + collectible + " and becoming the " + villainGoal + ".")
      synopses = [saveNinjago, stopVil]
      synopsis = random.choice(synopses)
      print(synopsis)
    def episode_list():
      for u in (1,2,3,4,5,6,7,8,9):
        adjs =   ["Cursed","Evil","Golden","Crystal","Dark","Djinn","Grand","Great","Titanium","Masked","Ghostly"]
        adj = random.choice(adjs)
        shopList = ["Tea","Pawn","Weapon","Clothing","Game","Garden","Drug","Corner"]
        shop = random.choice(shopList)
        nouns = ["Teapot",(shop + " Shop"),"City","Blade","Sword","Mask","Staff","Corpse","Tomb","Curse","Snake","Fortress","War","Battle","Tournament","World","Game","Field",newJitzu,collectible]
        noun = random.choice(nouns)
        nouns2 = ["Wu","Stiix","Djinnjago","Ninjago","New Ninjago City","The Digiverse","The Underworld","The First Spinjitzu Master","The Curse World","Doom","The Djinn","Love","War","Masks","Battle"]
        noun2 = random.choice(nouns2)
        suffixList = ["-bound","-struck"," Time"," Fight"," Mountain"," Point"]
        suffix = random.choice(suffixList)
        characterList = ["Kai","Jay","Zane","Cole","Lloyd","Nya","Wu","Garmadon","Pythor","The Great Devourer","Dareth","The Overlord","Clouse","Skylor","Master Chen","Morro","Nadakhan","The Quiet One","Meowthra","Sensei Yang"]
        char = random.choice(characterList)
        charsBlk = (char + "'s " + noun)
        tBlkBlkOBlk = ("The " + adj + " " + noun + " of " + noun2)
        snglList = [adj,noun,noun2]
        sngl = random.choice(snglList)
        cmpdSngl = (noun + suffix)
        BlkOBlk = (noun + " of " + noun2)
        episodeTypes = [tBlkBlkOBlk,sngl,cmpdSngl,BlkOBlk,charsBlk]
        episodeType = random.choice(episodeTypes)
        print(str(u) + ". " + episodeType)
      finEpList = [("10. Battle For the " + collectible),("10. " + rtrnAndRvngChar + "'s Final Attack"),("10. The True Power of " + newJitzu),("10. Attack of the " + villainGoal),("10. The " + villainGoal)]
      print(random.choice(finEpList))
    print(Back.MAGENTA + Fore.BLUE + ".p" + Fore.LIGHTYELLOW_EX + "y" + Fore.BLACK + "_thor v2.1.1")
    print("2022 MrQuinnzard/Casserole team")
    print(Style.RESET_ALL)
    title()
    print()
    synopsis()
    print()
    print("Episodes:")  
    episode_list()
    print()
    proceed = input("ENTER/RETURN to continue, type 'exit' to exit")
    if proceed == "exit":
      break
    else:
      if os.name == "nt":
        os.system("cls")
      else:
        os.system("clear")
      continue