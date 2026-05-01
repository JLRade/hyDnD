class hero:
    def __init__(self, name):
        self.name = name
        self.strengthStat = 5
        self.speedStat = 5
        self.luckStat = 5
        self.iqStat = 5
        self.healthStat =100
        self.foughtYet= False
        self.money=0
        self.potions={}
        self.weapon = None

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
