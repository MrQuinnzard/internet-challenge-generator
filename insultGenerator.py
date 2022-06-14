# Insult Generator 1.0
# 2022 MrQuinnzard/Casserole Team
def run():
    import random
    import os
    opSys = os.name
    if opSys == "nt":
        clearCmd = "cls"
        opSysStr = "Windows"
    else:
        clearCmd = "clear"
        opSysStr = "Unix-based system"

    z = 1
    def generateInsult():
        w = 1
        while w == 1:
            word1List = ["GRANNY","FUCK","SHIT","PISS","RUG","DRUG","WEED","TRUMPET","LADY","BUTT","ASS","BITCH","CUNT","DOG","PANT","FOOT","TREE","FART","DONKEY","HOE","QUEER","RETARD","COKE","DUMB","MONKEY","MOUTH","SON OF A","KIDDY","JACOB","FURRY","FUR","METH","NECKBEARD","EGG","WIFE","HUSBAND","TOILET","BOWL"]
            word1 = random.choice(word1List)
            word2List = ["GRANNY","FUCK","SHIT","PISS","RUG","DRUG","WEED","TRUMPET","LADY","BUTT","ASS","BITCH","CUNT","DOG","FOOT","TREE","FART","DONKEY","HOE","PIRATE","MUNCHER","EATER","MONKEY","FUCKER","MONKEY","DEALER","KISSER","MOUTH","BREATHER","SNORTER","SNIFFER","DIDDLER","BABY","ADDICT","BEATER","BOWL","HAIR"]
            word2 = random.choice(word2List)
            insult = (word1 + " " + word2)
            if word1 == word2:
                w = 1
                continue
            else:
                print(insult)
                w = 0

    while z == 1:
        os.system(clearCmd)
        print("Insult Generator 1.0 (" + opSysStr + ")")
        print("Created by Quinnzard")
        generateInsult()
        proceed = input("press enter, or type 'exit' to exit")
        if proceed == "exit":
            break
        else:
            continue
