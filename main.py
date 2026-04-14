#import os
import time
import classes as classes

try:
    from PIL import Image
except ImportError:
    Image = None

IMAGE_PATH = "C:/Users/Jitesh/Desktop/HyCourse/hyDnD/oliversleeping.jpg"

#creation of a hero and weapon
oliver = classes.hero()
#sword = classes.weapon()

#print(oliver.healthStat)
tempName = input("Greetings, what is your name?\n")

player = classes.hero()
player.name = tempName

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


print(f"Oliver hears your footsteps and wakes up.\n He ses you and says: Hello {player.name}.")
#Keep this if here it is an suprise
if Image is None:
    print("Pillow is not installed. Run: pip install pillow")
else:
    try:
        with Image.open(IMAGE_PATH) as dungeonImage:
            dungeonImage.show()
    except FileNotFoundError:
        print(f"Image not found at: {IMAGE_PATH}")
print( "I am a benevolent giant. You have four stats, and you have 20 points to spend however you like. You can distribute these points however you like. The stats are strength, speed, luck, and iq. Which stat would you like to increase first?")
selectedStat= input("^__^:")
selectedStat = selectedStat.lower()
availablePoints=20

def changeStat(stat):
    global availablePoints
    if stat == "strength":
        print("How many points would you like to put into strength?")
        points = int(input("^__^:"))
        player.strengthStat += points
        availablePoints-=points
    elif stat == "speed":
        print("How many points would you like to put into speed?")
        points = int(input("^__^:"))
        player.speedStat += points
        availablePoints -= points
    elif stat == "luck":
        print("How many points would you like to put into luck?")
        points = int(input("^__^:"))
        player.luckStat += points
        availablePoints -= points
    elif stat == "iq":
        print("How many points would you like to put into iq?")
        points = int(input("^__^:"))
        player.iqStat += points
        availablePoints -= points
    else:
        print("That is not a valid stat. Please choose strength, speed, luck, or iq.")
        newStat = input("^__^:")
        newStat = newStat.lower()
        changeStat(newStat)
while availablePoints > 0:
    changeStat(selectedStat)
    print(f"You have {availablePoints}.")
    selectedStat = input("What stat would you like to increase next?")
else:
    print("You don't have any points left. You are ready to adventure into the dungeon. Oliver says: I will give you a weapon to help you on your journey. He gives you a sword.")
sword=classes.weapon()
