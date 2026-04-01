import classes as classes
oliver = classes.hero()

sword = classes.weapon()

oliver.health_stat -= 2

oliver.strength_stat+=sword.strength_buff

print(oliver.health_stat)
print(sword.strength_buff)