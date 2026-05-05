# This game starts by importing the modules it needs.
# The `time` module pauses the story for effect, and `classes` provides the hero and weapon objects.
# Pillow is used later to open and display the dungeon image in a window.
import time
import random
from shop import shop
import classes as classes
from fight import fight
try:
    from PIL import Image
except ImportError:
    Image = None

IMAGE_PATH = "C:/Users/calebashultz/Downloads/Projects/hyDnD/oliversleeping.jpg"

# This file path points to the dungeon image that will be shown if Pillow is installed.
# It is fixed so the game always knows exactly where to find the picture.
# If the file is missing, the program prints a message instead of crashing.

# A hero object is created so the game has someone to play as.
# A weapon object is prepared later when the giant gives the player a sword.
# These objects come from the custom `classes` module.


# The player is asked for a name so the story can address them directly.
# That name is stored on the hero object.
# This makes the adventure feel personal.


player = classes.hero(input("Greetings, what is your name?\n"))


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
sword=classes.weapon(2,0.65,"common")
player.weapon=sword
time.sleep(2)
print("To start off, you will fight a basic monster to understand how to play.")
time.sleep(3)
print("Here's the rules: Whoever has more speed will go first. Your attack will be a composite of your strength stat and your weapon's attack stat")
print("The fight will go on until either you or the monster runs out of health.")
time.sleep(5)
print("Aside from attacking, you have three other options per turn. You can rest, use a potion, or run")
print("Resting allows you to heal 25 health, at the expense of a turn.")
time.sleep(5)
print("Using a potion isn't important right now, as you don't have any.")
print("Running allows you to escape from the monster. You can't run this first round")
time.sleep(5)
print("If you die, game over, no retries.")
print("But if you win, you will get some loot, which can get better depending on your luck stat.")
basicMonster=classes.monster("Gremlin", 4, 4, 13,0.25 )
time.sleep(4)
won = fight(player, basicMonster)
if won and won!="Ran":
    earnedGold= int(random.randint(1,3)) * player.luckStat
    print(f"You earned {earnedGold} gold")
    player.money+=earnedGold
    time.sleep(2)
    availablePoints+=basicMonster.strengthStat
    print(f"You have {availablePoints} points to spend now.")
elif won == "Ran":
    print(f"You ran from the monster!")
else:
    print("Game over")
    exit()
time.sleep(2)
print("You can now do one of four actions (type the number):\n1) Rest and fully heal \n2) Go to the shop")
print("4) Use points")
choice= ""
while not choice:
    try:
        choice=int(input("^__^:"))
    except ValueError:
        print("Invalid input. Please enter a number.")

newMonster=classes.monster("screenagers", 28, 5, 20,0.30 )
match choice:
    case 1:
        player.healthStat=100
    case 2:
        shop(player)
    case 3:
        while True:
            print("Which stat would you like to increase? When done type exit")
            choice=input("^__^:")
            choice=choice.lower().strip()
            remainingStats = ["strength", "speed", "luck", "iq"]
            if choice=="exit":
                break
            changeStat(choice)
time.sleep(2)
