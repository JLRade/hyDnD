class hero:
    def __init__(self, name):
        self.name = name
        self.strengthStat = 0
        self.speedStat = 0
        self.luckStat = 0
        self.iqStat = 0
        self.healthStat =100
        self.foughtYet= False
        self.money=0

        self.weapon = None
    potions = {}

class weapon:
    def __init__(self, attack, accuracy, rarity ):
        self.attackStat = attack
        self.accuracyStat = accuracy
        self.rarityStat = rarity


class potion:
    def __init__(self, stat, buff,player):
        self.attackStat = stat
        self.statBuff = buff
        player.potions[self.attackStat]=self.statBuff

    def __repr__(self):
        # Provide a readable representation so printing a potion shows its type and buff.
        return f"potion(stat={self.attackStat!r}, buff={self.statBuff!r})"

class monster:
    def __init__(self,name,strength,speed,health,accuracy):
        self.name = name
        self.strengthStat = strength
        self.speedStat = speed
        self.healthStat = health
        self.accuracyStat = accuracy
