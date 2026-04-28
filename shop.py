from classes import potion

def shop():
    print("You have entered the shop. You can buy the following potions.\n")
    print("A potion that increases your attack by 10 for the next fight. It costs 10 gold.\n")
    print("A potion that increases your health by 20 for the next fight. It costs 15 gold.\n")
    print("A potion that increases your speed by 5 for the next fight. It costs 12 gold.\n")
    print("A potion that increases your luck by 5 for the next fight. It costs  12 gold.\n")
    choice = input("Which potion would you like to buy? (attack, health, speed, luck)\n")
    choice = choice.lower().strip()
    if choice == "attack":
        p = potion("attack", 10)
    elif choice == "health":
        p = potion("health", 20)
    elif choice == "speed":
        p = potion("speed", 5)
    elif choice == "luck":
        p = potion("luck", 5)
    else:
        print("Invalid choice, please try again.")
        return shop()
    # Confirm the purchase to the player and return the potion object.
    print(f"You bought a {p.attackStat} potion (+{p.statBuff}).")
    return p
