from classes import potion
import time
def shop(player):
    print("You have entered the shop. You can buy the following potions:\n")
    print("A potion that increases your attack by 10 for the next fight. It costs 10 gold.\n")
    print("A potion that increases your health by 20 for the next fight. It costs 15 gold.\n")
    print("A potion that increases your speed by 5 for the next fight. It costs 12 gold.\n")
    print("A potion that increases your luck by 5 for the next fight. It costs  12 gold.\n")
    print("If you don't want to buy a potion, you can also type 'exit' to exit the shop\n")
    choice = input("Which potion would you like to buy? (attack, health, speed, luck)\n")
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
            print("You don't have enough gold to buy this potion. Pick another potion or exit\n")
            time.sleep(2)
            return shop(player)
    elif choice == "luck":
        if player.money >= 12:
            p = potion("luck", 5,player)
        else:
            print("You don't have enough gold to buy this potion. Pick another potion or exit\n")
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
