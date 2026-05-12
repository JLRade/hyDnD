# This game starts by importing the modules it needs.
# The `time` module pauses the story for effect, and `classes` provides the hero and weapon objects.
# Pillow is used later to open and display the dungeon image in a window.
import time
import random
from shop import shop
import classes as classes
from fight import fight
from rich import print
from rich.console import Console
try:
    from PIL import Image
except ImportError:
    Image = None
class GameError(Exception):
    """Base class for all game errors"""
    pass
class codeError(GameError):
    pass
IMAGE_PATH = "/Users/calebashultz/Downloads/Projects/hyDnD/oliversleeping.jpg"
console = Console()
# This file path points to the dungeon image that will be shown if Pillow is installed.
# It is fixed so the game always knows exactly where to find the picture.
# If the file is missing, the program prints a message instead of crashing.

# A hero object is created so the game has someone to play as.
# A weapon object is prepared later when the giant gives the player a sword.
# These objects come from the custom `classes` module.
#this cleans up the terminal whenever needed
def clear():
    # Clears the terminal screen
    console.clear()

# The player is asked for a name so the story can address them directly.
# That name is stored on the hero object.
# This makes the adventure feel personal.

clear()
player = classes.hero(input("Greetings, what is your name?\n^__^:"))


# The game welcomes the player and sets the scene.
# A short pause gives the opening dialogue more dramatic timing.
# The large text block below is just for atmosphere.
print(f'Hello, {player.name}, you have just entered the Dungeon. You can hear a giant snore.')
time.sleep(2)
print("""
                                 ................................  ..........ooo    .. ......             ..ooooooooooooooooo..       ..... 
   .                             ..........     ...................oooooo.......  ... ..........            .oooooooooooooooo......  .......
  .      .                       .......     .  ............................... .... ........      ....      .oooooooooooooooooooo..........
        oo..                    ......    ........................ ...  ..       .............   .....        .oooooooooooooooooooooooo.....
       .o..                     ...     ...................... ...  ..........                 ......         .oooooooooooooo.  ..oooooooooo
      .oo.                            ...............ooo...... ........   ....                                 ...ooooooooooo.  ...ooooooooo
   .  ....                         ..................oo.................  .....                                .........oooo.      .oooooooo
   . . .o.                       ..................ooooo..............oo..  ...                               ......   .....       .oooooooo
     . ..                       ..................oooooooooo..............                                    ...........          .oooooooo
...                             ..................oooooooooo...............                                    ..........          ....ooooo
ooo...                          ..................oooooooooo................                                                       .........
ooooooooo..         .................................oooooo.................                               ...                              
ooooooooooo.      ....................................oooo...................                                ..oooo....ooooooooooo..........
                  ....................................ooo....................                                     ..oooooooooooooooooooooooo
                  ....... ...................................................                                         ..oooooooooooooooooooo
                   ..... ....................................................                                              ..ooooooooooooooo
                     ...............................................oooooooo.                                      .......     ...oooooo....
............. ..       .............................................oooooooo..                                     ...........      ..ooo...
....          ..o..               ...................................oooooooo.                                    ................       ..o
            ..ooooo.      ...........................................ooooooo..                                    ..................        
          ...oooooooo............oooooooooo...................................           ..                       ....................      
        ..........ooooooo.............oooooooo.............................  ....         ......                  .....................     
       ...       .....oooooo............ooooooooo........................      ...               ..               .....................     
        ..          .....oooooooo........oooooooooo......................       ....                             .......................    
         ......oooo..   ......oooooooo.....oooooooooooo........ooooooo......     .....                           .................          
       .....ooooooooo.      ......ooooooooooooooooooooooo.......oooooo........    .....                         ................            
   ....ooo.ooooooooooo...  ...........oooooooooooooooooooooo.....ooooo..........  ......                        ................            
..........ooooooooooooooooooooo..........oooooooooooooooooooo...oooooooooo........ ......                      ...............              
........ooooooooooooooooooooooooo......  ....ooooooooooooooooooooooooo..oooo....oo. ......                     .............                
......oooooooooooooooooooooooooooo....oo.  ......ooooooooooooooooooooo.....oo....oo......o                    .............                 
.....ooooooooooooooooooooooooooooooo...oo.. ...........oooooooooooooo.......ooo...oo.....o                    .............                 
....oooooo...oooooooooooooooooooooooo..oooo.......oo........oooooooo.... ....oo...oo. ....                   ............                  .
..ooooooooo....oooooooooooooooooooooooo..oooo......oooo.......ooooooo..    .ooo...oo  ..o.                   ..........                  ...
.ooooooooooo.....oooooooooooooooooooooooo.ooooo......ooooo.......ooooo.   .oooo .o.. .ooo...                 .........                   ...
.oooooooooooo.....oooooooooooooooooooooooooooooo.......ooooooo.....oooo..ooooo......oooooooo....            .........                  .....
 .oooooooooooo.....oooooooooooooooooooooooooooooo.....oooooooooooo...ooooooooo.oooooooooooooooo.            ........                   .... 


""")


# Oliver reacts to the player entering the dungeon.
# The code below tries to open the image with Pillow if it is available.
# If Pillow is not installed or the image is missing, the program prints a friendly message instead.
print(f"Oliver hears your footsteps and wakes up.\n He ses you and says: Hello {player.name}.")
#Keep this if here it is a suprise
if Image is None:
    print("Pillow is not installed. Run: pip install pillow")
else:
    try:
        with Image.open(IMAGE_PATH) as dungeonImage:
            dungeonImage.show()
    except FileNotFoundError:
        print(f"Image not found at: {IMAGE_PATH}")
# The giant now explains the stat allocation part of the game.
# The player has 20 points to divide among four stats.
# The loop later keeps asking until every stat has been chosen.
print("I am a benevolent giant. You have four stats, and you have 20 points to spend however you like.")
availablePoints = 20
remainingStats = ["strength", "speed", "luck", "iq"]
statAttributes = {
    "strength": "strengthStat",
    "speed": "speedStat",
    "luck": "luckStat",
    "iq": "iqStat",
}


def changeStat(stat):
    # This function updates one chosen stat for the player.
    # It checks whether the stat is still available, then asks how many points to add.
    # If the input is valid, it updates the hero and removes that stat from the menu.
    global availablePoints
    stat = stat.strip().lower()

    if stat not in remainingStats:

        print(f"That is not a valid choice. Pick from: {', '.join(remainingStats)}")
        return False

    print(f"How many points would you like to put into {stat}?")
    try:
        points = int(input("^__^:"))
    except ValueError:
        print("Enter a valid whole number for stats.")
        return False

    if points < 0:
        print("You cannot use negative points.")
        return False

    if points > availablePoints:
        print(f"You only have {availablePoints} points left.")
        return False

    statAttribute = statAttributes[stat]
    setattr(player, statAttribute, getattr(player, statAttribute) + points)
    availablePoints -= points
    remainingStats.remove(stat)
    return True


while remainingStats:
    if availablePoints == 0:
        print("You don't have any points left...")
        break

    # 1. Determine which stat to change
    if len(remainingStats) == 1:
        selectedStat = remainingStats[0]
    else:
        selectedStat = input(f"Choose a stat to increase ({', '.join(remainingStats)}):\n^__^:")

    # 2. Call the function once and check the result
    if changeStat(selectedStat):
        print(f"You have {availablePoints} points left.")

else:
    # This message appears if the player chooses all remaining stats before the loop ends.
    # It tells the player they still have unused points.
    # The game then moves on to creating the weapon.
    print(f"All stats were chosen. You still have {availablePoints} points left for later.")
clear()
sword=classes.weapon(2,0.65,"common")
player.weapon=sword
if player.name != "admin":
    print("You have been given a basic sword that has an attack stat of two, but it has a 65% accuracy.")
    time.sleep(2)
    print("To start off, you will fight a basic monster to understand how to play.")
    time.sleep(3)
    print("Here's the rules: Whoever has more speed will go first. Your attack will be a composite of your strength stat and your weapon's attack stat")
    time.sleep(5)
    print("Aside from attacking, you have three other options per turn. You can rest, use a potion, or run")
    print("Resting allows you to heal 25 health, at the expense of a turn.")
    time.sleep(5)
    print("Running allows you to escape from the monster. You can't run this first round")
    time.sleep(5)
    print("If you die, game over, no retries.")
    print("But if you win, you will get some loot, which can get better depending on your luck stat.")
basicMonster=classes.monster("Gremlin", 4, 4, 13,0.25 )
time.sleep(4)
clear()
won = fight(player, basicMonster)
player.foughtYet= True
def rewards(won, mult, monster):

    global availablePoints
    if won and won!="Ran":
        earnedGold= int(random.randint(1,mult)) * player.luckStat
        print(f"You earned {earnedGold} gold")
        player.money+=earnedGold
        time.sleep(2)
        availablePoints+=monster.speedStat
        print(f"You have {availablePoints} points to spend now.")
    elif won == "Ran":
        print(f"[bold yellow]You ran from the monster![/bold yellow]")
    else:
        print("[bold red]Game over[/bold red]")
        exit()
rewards(won, 3, basicMonster)
time.sleep(2)
def afterFight():
    global remainingStats
    print("You can now do one of four actions (type the number):\n1) Rest and fully heal \n2) Go to the shop")
    print("3) Use points")
    choice= ""
    while not choice:
        try:
            choice=int(input("^__^:"))
        except ValueError:
            print("Invalid input. Please enter a number.")


    match choice:
        case 1:
            player.healthStat=100
            print("Fully healed!")
        case 2:
            shop(player)
        case 3:
            while True:
                if availablePoints == 0:
                    print("You don't have any points left.")
                    break
                print("Which stat would you like to increase? When done type exit")
                choice=input("^__^:")
                choice=choice.lower().strip()
                remainingStats = ["strength", "speed", "luck", "iq"]
                if choice=="exit":
                    break
                changeStat(choice)
clear()
afterFight()
time.sleep(2)
monsters = [
    classes.monster("Goblin", 15, 5, 18, 0.35),
    classes.monster("screenager", 28, 7, 22, 0.40),
    classes.monster("Troll", 35, 9, 35, 0.50)
]
clear()
print("Which monster do you want to fight?\n Your options are a goblin, a screenager, or troll")
monsterChoice = input("^__^:").lower()

# 2. Search your list for a match
selected_monster = None

for m in monsters:
    if m.name.lower() == monsterChoice:
        selected_monster = m
        break

# 3. Check if we actually found one
if selected_monster:
    print(f"You chose to fight the {selected_monster.name}!")
    # Now you can use selected_monster.hp, etc.
else:
    print("That monster doesn't exist!")
if selected_monster.name == "Goblin":
    mult = 3
elif selected_monster.name == "screenager":
    mult = 4
else:
    mult = 6
print(f"You will now enter your second fight against a {selected_monster.name}. This will be challenging!")
won = fight(player, selected_monster)
rewards(won, mult, selected_monster)
time.sleep(3)
clear()
afterFight()
time.sleep(2)
print("Now it is time for your last fight against the boss of this game. This will be insanely hard.\n If you lose this fight, you can try again.")
print("You will be fully healed before this fight")
player.healthStat=100
boss = classes.monster("PYTHON", 40, 10, 65, 0.67 )
time.sleep(3)
while True:
    finalWon = fight(player, boss)
    if finalWon:
        print("[bold green]You won the game![/bold green]")
        time.sleep(2)
        raise codeError("By defeating the boss Python, you have broken the code!")
    else:
        while True:
            print("You lost. Try again? y/n")
            choice = input("^__^:").lower().strip()
            time.sleep(2)
            match choice:
                case "y":
                    player.healthStat=100
                    break
                case "n":
                    print("Wow, you're either an incredible coward or you just don't care about this game. \nEither way, bye!")
                    time.sleep(3)
                    print("[bold red]Game over[/bold red]")
                    exit()
                case _:
                    print("Invalid input. try again.")
                    continue
