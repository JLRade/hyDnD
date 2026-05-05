
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
        choice = choice.lower().strip().replace(" ", "")
        # if monster dead end func

        if choice == "run" and player.foughtYet:
            endfight = True
        elif choice == "run" and not player.foughtYet:
            print("It' still your first fight, don't run!")
            return playerTurn()

        elif choice == "fight":
            if random.random() <= player.weapon.accuracyStat:
                damage = player.strengthStat + player.weapon.attackStat
                monster.healthStat -= damage
                print(f"You hit the {monster.name} for {damage} damage!")
                if monster.healthStat > 0:
                    print(f"Player health: {player.healthStat}\nMonster health: {monster.healthStat}")
                else:
                    print(f"Player health: {player.healthStat}\nMonster health: 0")

            else:
                print("You missed!")
                time.sleep(2)
                print(f"Player health: {player.healthStat}\nMonster health: {monster.healthStat}")
        elif choice == "usepotion":
            if not player.potions:
                print("You have no potions to use!")
                return playerTurn()
            elif potionUsed == True:
                print("You have already used a potion this fight! Pick another action.")
                return playerTurn()
            else:
                potionChoice=input("What potion would you like to use?\n")
                potionChoice=potionChoice.lower().strip()
                match potionChoice:
                    case "attack":
                        player.attackStat += player.potions["attack"]
                        potionUsed = "attack"
                    case "health":
                        player.healthStat += player.potions["health"]
                        potionUsed = "health"
                    case "speed":
                        player.speedStat += player.potions["speed"]
                        potionUsed = "speed"
                    case "luck":
                        player.luckStat += player.potions["luck"]
                        potionUsed = "luck"

        elif choice == "rest":
            if player.healthStat > 75:
                player.healthStat =100
                print("You are now fully healed!")
                time.sleep(2)
            else:
                player.healthStat += 25
            print(f"You now have {player.healthStat} health")
            time.sleep(2)
        else:
            print("That is not a valid option. Please try again.")
            return playerTurn()
        if endfight == True:
            "You ran from the monster!"
            return "Ran"
        elif monster.healthStat > 0:
            return monsterTurn()
        else:
            print("You won the fight!")
            global won
            won = True
            return won

    def monsterTurn():
        if random.random() > monster.accuracyStat:
            player.healthStat -= monster.strengthStat
            print(f"The {monster.name} has hit you for {monster.strengthStat} health!")
            print(f"Player health: {player.healthStat}\nMonster health: {monster.healthStat}")
            time.sleep(2)
        else:
            print(f"The {monster.name} has missed!")
            time.sleep(2)
        if player.healthStat > 0:
            return playerTurn()  # <-- ADD RETURN HERE
        else:
            print("You lost the fight!")
            global won
            won = False
            return won


    if player.speedStat > monster.speedStat:
        return playerTurn()
    else:
        return monsterTurn()




