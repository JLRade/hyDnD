
import random
import time
from rich import print
from rich.console import Console
console = Console()
def clear():
    # Clears the terminal screen
    console.clear()


from rich.table import Table
from rich.panel import Panel


def draw_fight_header(player, monster):
    # Create a table with no borders for a clean "HUD" look
    table = Table.grid(expand=True)
    table.add_column(justify="left", ratio=1)
    table.add_column(justify="right", ratio=1)

    # Player side (Left)
    player_ui = f"[bold cyan]{player.name}[/bold cyan]\n[bold red]HP: {player.healthStat}[/bold red]"

    # Monster side (Right)
    monster_ui = f"[bold magenta]{monster.name}[/bold magenta]\n[bold red]HP: {monster.healthStat}[/bold red]"

    table.add_row(player_ui, monster_ui)

    # Wrap it in a single panel so it looks like a game window
    console.print(
        Panel(table, title="[bold white]BATTLE[/bold white]", subtitle="[italic]Fight for your life![/italic]"))


potionUsed = False
endfight=False
from rich import print
def fight(player, monster):
    global potionUsed, endfight

    potionUsed = False
    endfight = False
    print(f"\nHello, {player.name}, you have entered a fight with a {monster.name}" )

    def playerTurn():
        time.sleep(2)
        clear()
        draw_fight_header(player, monster)
        global potionUsed, endfight
        print("\nIt's your turn, what will you do?")
        choice = input("Options: Fight, Rest, Use potion, or Run\n^__^:")
        choice = choice.lower().strip().replace(" ", "")
        # if monster dead end func

        if choice == "run" and player.foughtYet:
            endfight = True
        elif choice == "run" and not player.foughtYet:
            print("It' still your first fight, don't run")
            return playerTurn()

        elif choice == "fight":
            if random.random() <= player.weapon.accuracyStat:
                damage = player.strengthStat + player.weapon.attackStat
                monster.healthStat -= damage
                print(f"\nYou hit the {monster.name} for {damage} damage!")
                if monster.healthStat > 0:
                    draw_fight_header(player, monster)
                else:
                    monster.healthStat =0
                    draw_fight_header(player, monster)
            else:
                print("You missed!")
                time.sleep(2)
                print(f"\nPlayer health: {player.healthStat}\nMonster health: {monster.healthStat}\n")
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
                        player.attackStat += player.potions.pop("attack")
                        potionUsed = "attack"

                    case "health":
                        player.healthStat += player.potions.pop("health")
                        potionUsed = "health"
                    case "speed":
                        player.speedStat += player.potions.pop("speed")
                        potionUsed = "speed"
                    case "luck":
                        player.luckStat += player.potions.pop("luck")
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
            if potionUsed:
                match potionUsed:
                    case "attack":
                        player.attackStat-=10
                    case "health":
                        if player.healthStat > 100:
                            player.healthStat=100
                    case "speed":
                        player.speedStat -= 5
                    case "luck":
                        player.luckStat -= 5
            return "Ran"
        elif monster.healthStat > 0:
            return monsterTurn()
        else:
            if potionUsed:
                match potionUsed:
                    case "attack":
                        player.attackStat-=10
                    case "health":
                        player.healthStat -= 20
                    case "speed":
                        player.speedStat -= 5
                    case "luck":
                        player.luckStat -= 5
            print("[bold green]You won the fight![bold green]")
            global won
            won = True
            return won


    def monsterTurn():
        if random.random() <= monster.accuracyStat:
            player.healthStat -= monster.strengthStat
            print(f"\nThe {monster.name} has hit you for {monster.strengthStat} health!")
            time.sleep(2)
        else:
            print(f"\nThe {monster.name} has missed!")
            time.sleep(2)
        if player.healthStat > 0:
            draw_fight_header(player, monster)
            return playerTurn()  # <-- ADD RETURN HERE
        else:
            if potionUsed:
                match potionUsed:
                    case "attack":
                        player.attackStat-=10
                    case "health":
                        player.healthStat -= 20
                    case "speed":
                        player.speedStat -= 5
                    case "luck":
                        player.luckStat -= 5
            print("You lost the fight!")
            global won
            won = False
            return won


    if player.speedStat > monster.speedStat:
        return playerTurn()
    else:
        return monsterTurn()




