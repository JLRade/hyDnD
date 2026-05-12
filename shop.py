from classes import potion
from classes import weapon
import time
from main import clear
def shop(player):
    clear()
    print("You have entered the shop. You can buy the following things:\n")
    time.sleep(1.5)
    print("A potion that increases your attack by 10 for the next fight. It costs 10 gold.\n")
    time.sleep(1.5)
    print("A potion that increases your health by 20 for the next fight. It costs 15 gold.\n")
    time.sleep(1.5)
    print("A potion that increases your speed by 5 for the next fight. It costs 12 gold.\n")
    time.sleep(1.5)
    print("A potion that increases your luck by 5 for the next fight. It costs  12 gold.\n")
    time.sleep(1.5)
    print("A sword that has a better attack and accuracy. It costs 20 gold.\n")
    time.sleep(1.5)
    print("If you don't want to buy a potion or weapon, you can also type 'exit' to exit the shop\n")
    choice = input("Which potion would you like to buy? (attack, health, speed, luck, sword)\n^__^:")
    choice = choice.lower().strip()
    if choice == "attack":
        if player.money >= 10:
            p = potion("attack", 10, player)
        else:
            print("You don't have enough gold to buy this potion. Pick another potion or exit\n")
            time.sleep(2)
            return shop(player)
    elif choice == "health":
        if player.money >= 15:
            p = potion("health", 20, player)
        else:
            print("You don't have enough gold to buy this potion. Pick another potion or exit\n")
            time.sleep(2)
            return shop(player)
    elif choice == "speed":
        if player.money >= 12:
            p = potion("speed", 5, player)
        else:
            print("You don't have enough gold to buy this. Choose another option or exit\n")
            time.sleep(2)
            return shop(player)
    elif choice == "luck":
        if player.money >= 12:
            p = potion("luck", 5,player)
        else:
            print("You don't have enough gold to buy this potion. Pick another potion or exit\n")
            time.sleep(2)
            return shop(player)
    elif choice == "sword":
        price=20
        chosenAttack=6
        chosenAcc=0.7
        print("You can either buy the sword with base stats or upgrade it")
        time.sleep(2)
        print("These are the base stats: attack: 6, accuracy, 70%, price: 20.")
        time.sleep(2)
        while True:
            price=20
            print("Do you want to upgrade? y/n")
            choice=(input("^__^:"))
            if choice == "y":
                while True:
                    print("What attack value would you like? You can choose higher or lower.\n Each extra attack you choose is an extra 2 gold")
                    try:
                        chosenAttack=int(input("^__^:"))
                        break
                    except ValueError:
                        print("Please enter a valid number")
                        continue
                while True:
                    print("What accuracy value would you like? You can choose higher or lower.\n Each 1% extra accuracy is 1 more gold")
                    try:
                        chosenAcc=int(input("^__^:"))
                        if chosenAcc > 100:
                            print("Please enter a valid number: has to be less than 100")
                        chosenAcc/=100
                        break
                    except ValueError:
                        print("Please enter a valid number")
                        continue
                price+=(chosenAttack-6)*2
                price+=(chosenAcc*100)-70
                price=int(price)
                if price<0:
                    price=5
                print(f"Your weapon price is {price}")
                time.sleep(2)
                print("Confirm buy? y/n")
                choice=(input("^__^:"))
                if choice == "y":
                    break
                else:
                    continue


            elif choice == "n":
                break
            else:
                print("Invalid choice, please try again.")
                continue

        if player.money >= price:
            newSword = weapon(chosenAttack, chosenAcc, "rare")
            player.weapon= newSword
            player.money -= price
            print("You bought an sword.")
            print(f"Sword Stats - Attack: {newSword.attackStat}, Accuracy: {int(newSword.accuracyStat*100)}%, Rarity: {newSword.rarityStat}")
            p=False
        else:
            print("You don't have enough gold to buy this sword. Pick another item or exit\n")
            time.sleep(2)
            return shop(player)

    elif choice == "exit":
        print("You have exited the shop")
        return False
    else:
        print("Invalid choice, please try again.")
        return shop(player)
    # Confirm the purchase to the player and return the potion object.
    if p:
        if p.attackStat== "attack":
            print(f"You bought an {p.attackStat} potion (+{p.statBuff}).")
        else:
            print(f"You bought a {p.attackStat} potion (+{p.statBuff}).")
        return p
    else:
        return None
