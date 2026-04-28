class hero:
    name = ""
    strengthStat = 0
    speedStat = 0
    luckStat = 0
    iqStat = 0
    healthStat = 100
    foughtYet= False
    money=0
    potions={}

class weapon:
    def __init__(self, attack, accuracy, rarity ):
        self.attackStat = attack
        self.accuracyStat = accuracy
        self.rarityStat = rarity


class potion:
    def __init__(self, stat, buff,):
        self.attackStat = stat
        self.statBuff = buff
        hero.potions[self.attackStat]=self.statBuff

    def __repr__(self):
        # Provide a readable representation so printing a potion shows its type and buff.
        return f"potion(stat={self.attackStat!r}, buff={self.statBuff!r})"

class monster:
    def __init__(self,name,strength,speed,health):
        self.name = name
        self.strengthStat = strength
        self.speedStat = speed
        self.healthStat = health
