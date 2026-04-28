import tkinter as tk
from tkinter import ttk, messagebox
import time
import classes
try:
    from PIL import Image, ImageTk
except Exception:
    Image = None
    ImageTk = None

IMAGE_PATH = "C:/Users/Jitesh/Desktop/HyCourse/hyDnD/oliversleeping.jpg"

# Create hero and temporary objects (mirror of main.py setup)
oliver = classes.hero()
player = None

# Stats configuration
availablePoints = 20
remainingStats = ["strength", "speed", "luck", "iq"]
statAttributes = {
    "strength": "strengthStat",
    "speed": "speedStat",
    "luck": "luckStat",
    "iq": "iqStat",
}

# Tkinter setup
root = tk.Tk()
root.title("hyDnD — GUI")
root.geometry("900x700")

# Main frames
top_frame = ttk.Frame(root)
top_frame.pack(fill="x", padx=8, pady=6)

middle_frame = ttk.Frame(root)
middle_frame.pack(fill="both", expand=True, padx=8, pady=6)

bottom_frame = ttk.Frame(root)
bottom_frame.pack(fill="x", padx=8, pady=6)

# Output text area
output = tk.Text(middle_frame, wrap="word", state="disabled", width=100)
output.pack(fill="both", expand=True)

# Helper to write to the output area
def write(text):
    output.config(state="normal")
    output.insert("end", text + "\n")
    output.see("end")
    output.config(state="disabled")

# Name entry UI
name_label = ttk.Label(top_frame, text="Enter your name:")
name_label.pack(side="left")
name_var = tk.StringVar()
name_entry = ttk.Entry(top_frame, textvariable=name_var)
name_entry.pack(side="left", padx=6)

start_button = ttk.Button(top_frame, text="Start", command=lambda: start_game())
start_button.pack(side="left", padx=6)

# Image display window variable
image_label = None
image_tk = None

# Stat buttons container
stat_buttons_frame = ttk.Frame(bottom_frame)
stat_buttons_frame.pack(side="left", padx=6)

# Global state for GUI
state = {
    "player": None,
    "availablePoints": availablePoints,
    "remainingStats": remainingStats.copy(),
}

# Create stat buttons dynamically
stat_buttons = {}

def create_stat_buttons():
    for widget in stat_buttons_frame.winfo_children():
        widget.destroy()
    ttk.Label(stat_buttons_frame, text="Choose a stat to increase:").pack(anchor="w")
    for stat in state["remainingStats"]:
        b = ttk.Button(stat_buttons_frame, text=stat.capitalize(), command=lambda s=stat: on_choose_stat(s))
        b.pack(fill="x", pady=2)
        stat_buttons[stat] = b

# Ask for points via a small dialog
def ask_points(stat):
    prompt = tk.Toplevel(root)
    prompt.title(f"Allocate points to {stat}")
    ttk.Label(prompt, text=f"How many points would you like to put into {stat}?").pack(padx=10, pady=10)
    points_var = tk.StringVar()
    entry = ttk.Entry(prompt, textvariable=points_var)
    entry.pack(padx=10, pady=6)
    entry.focus()

    def on_ok():
        s = points_var.get().strip()
        try:
            points = int(s)
        except ValueError:
            messagebox.showerror("Invalid number", "Enter a valid whole number for stats.")
            return
        if points < 0:
            messagebox.showerror("Invalid number", "You cannot use negative points.")
            return
        if points > state["availablePoints"]:
            messagebox.showerror("Not enough points", f"You only have {state['availablePoints']} points left.")
            return
        # apply
        stat_attr = statAttributes[stat]
        setattr(state["player"], stat_attr, getattr(state["player"], stat_attr) + points)
        state["availablePoints"] -= points
        # remove stat
        if stat in state["remainingStats"]:
            state["remainingStats"].remove(stat)
        write(f"Added {points} to {stat}. You have {state['availablePoints']} points left.")
        prompt.destroy()
        refresh_after_allocation()

    ok = ttk.Button(prompt, text="OK", command=on_ok)
    ok.pack(side="left", padx=10, pady=10)
    cancel = ttk.Button(prompt, text="Cancel", command=prompt.destroy)
    cancel.pack(side="right", padx=10, pady=10)

def on_choose_stat(stat):
    if state["availablePoints"] == 0:
        messagebox.showinfo("No points", "You don't have any points left.")
        return
    ask_points(stat)

def refresh_after_allocation():
    # recreate stat buttons
    create_stat_buttons()
    # if done or no points left, finish
    if state["availablePoints"] == 0:
        finish_allocation()
    elif not state["remainingStats"]:
        finish_allocation()

def finish_allocation():
    write("You don't have any points left or all stats chosen. You are ready to adventure into the dungeon.")
    # give a sword like in main.py
    state["player"].weapon = classes.weapon(2, 0.65, "common")
    write("Oliver gives you a sword (attack 2, accuracy 0.65, rarity common).")
    # show final stats summary
    write("Final player stats:")
    write(f"Strength: {state['player'].strengthStat}")
    write(f"Speed: {state['player'].speedStat}")
    write(f"Luck: {state['player'].luckStat}")
    write(f"IQ: {state['player'].iqStat}")
    write(f"Health: {state['player'].healthStat}")
    # show a basic monster summary and a note about fight/shop
    basicMonster = classes.monster("Gremlin", 4, 4, 13)
    write(f"You will face a {basicMonster.name} next (strength {basicMonster.strengthStat}, speed {basicMonster.speedStat}, health {basicMonster.healthStat}).")
    write("The fight/shop parts are not automated in this GUI version; integrate `fight()` and `shop()` when ready.")

# Start game flow when name submitted
def start_game():
    name = name_var.get().strip()
    if not name:
        messagebox.showerror("Enter name", "Please enter your name to start.")
        return
    # initialize player
    state["player"] = classes.hero()
    state["player"].name = name
    write(f"Hello, {name}, you have just entered the Dungeon. You can hear a giant snore.")
    # small pause simulated with root.after
    root.after(500, lambda: write_ascii_and_image())
    # disable start controls
    name_entry.config(state="disabled")
    start_button.config(state="disabled")

def write_ascii_and_image():
    ascii_block = '''
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
'''
    write(ascii_block)
    write(f"Oliver hears your footsteps and wakes up. He sees you and says: Hello {state['player'].name}.")
    # show image in a new window if Pillow available
    if Image is None or ImageTk is None:
        write("Pillow is not installed or not available; skipping image display.")
    else:
        try:
            img = Image.open(IMAGE_PATH)
            img.thumbnail((400, 400))
            img_win = tk.Toplevel(root)
            img_win.title("Dungeon image")
            global image_tk
            image_tk = ImageTk.PhotoImage(img)
            lbl = ttk.Label(img_win, image=image_tk)
            lbl.pack()
        except FileNotFoundError:
            write(f"Image not found at: {IMAGE_PATH}")
        except Exception as e:
            write(f"Could not open image: {e}")
    write("I am a benevolent giant. You have four stats, and you have 20 points to spend however you like.")
    write("Choose a stat from the buttons below and allocate points.")
    create_stat_buttons()

# Initialize UI with a short welcome
write("Welcome to hyDnD (GUI). Enter your name to begin.")

root.mainloop()

