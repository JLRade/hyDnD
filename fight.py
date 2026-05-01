
import random
import time
potionUsed = False
endfight=False
def fight(player, monster):
    global potionUsed, endfight
    potionUsed = False
    endfight = False
    print(f"Hello, {player.name}, you have entered a fight with a {monster.name}" )

    def playerTurn():
        global potionUsed, endfight
        print("It's your turn, what will you do?")
        choice = input("Options: Fight, Rest, Use potion, or Run\n")
        choice = choice.lower().strip()
        # if monster dead end func

        if choice == "run" and player.foughtYet:
            endfight = True
        elif choice == "run" and not player.foughtYet:
            print("It' still your first fight, don't run!")
            playerTurn()
            return None
        elif choice == "fight":
            if random.random() <= player.weapon.accuracyStat:
                damage = player.strengthStat + player.weapon.attackStat
                monster.healthStat -= damage
                print(f"You hit the {monster.name} for {damage} damage!")
            else:
                print("You missed!")
                time.sleep(2)
        elif choice == "usepotion":
            if not player.potions:
                print("You have no potions to use!")
                playerTurn()
            elif potionUsed == True:
                print("You have already used a potion this fight! Pick another action.")
                playerTurn()
            else:
                potionChoice=input("What potion would you like to use?\n")
                potionChoice=potionChoice.lower().strip()
                if potionChoice == "attack":
                    player.attackStat += player.potions["attack"]
                    potionUsed = "attack"
                elif potionChoice == "health":
                    player.healthStat += player.potions["health"]
                    potionUsed = "health"
                elif potionChoice == "speed":
                    player.speedStat += player.potions["speed"]
                    potionUsed = "speed"
                elif potionChoice == "luck":
                    player.luckStat += player.potions["luck"]
                    potionUsed = "luck"
        elif choice == "rest":
            if player.healthStat > 75:
                player.healthStat =100
            else:
                player.healthStat += 25
            print(f"You now have {player.healthStat} health")
        if endfight == True:
            return False
        elif monster.healthStat != 0:
            monsterTurn()
        else:
            print("You won the fight!")
            return won


    def monsterTurn():
        global endfight
        # if player dead end func
        pass

    if player.speedStat > monster.speedStat:
        playerTurn()
    else:
        monsterTurn()
    if monster.healthStat == 0:
        won = True
        return won
    elif player.healthStat == 0:
        won = False
        return won

