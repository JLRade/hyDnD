class hero:
    name = ""
    strengthStat = 0
    speedStat = 0
    luckStat = 0
    iqStat = 0
    healthStat = 100
    foughtYet= False

class weapon:
    attackStat = 2
    accuracy = 65
    rarity = "rare"

class monster:
    def __init__(self,name,strength,speed,health):
        self.name = name
        self.strengthStat = strength
        self.speedStat = speed
        self.healthStat = health
