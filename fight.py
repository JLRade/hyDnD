

def fight(player, monster):
    print(f"Hello, {player.name}, you have entered a fight with a {monster.name}" )
    def playerTurn():
        print("It's your turn, what will you do?")
        choice=input("Options: Fight, Rest, Use potion, or Run\n")
        choice=choice.lower().strip()
        #if monster dead end func
        if choice == "run" and player.foughtYet:
            pass
        else:
            print("It' still your first fight, don't run!")
            playerTurn()
    def monsterTurn():
        #if player dead end func
        pass
    if player.speedStat > monster.speedStat:
        playerTurn()
    else:
        monsterTurn()

