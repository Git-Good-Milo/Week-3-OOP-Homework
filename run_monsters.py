from monster_class import *

# First Monster
my_monster1 = Monsters('Werewolf Steve', 'Soft fur', 'none whatsoever', ['Fast', 'Terrifying'])

# Characteristics
print(my_monster1.name)
print(my_monster1.fur_type)
print(my_monster1.skills) # optional list ['Strength', 'Poisonous', 'Mean']
print(my_monster1.cuteness)

# Methods

print(my_monster1.scare())
print(my_monster1.eat())
print(my_monster1.morph())
print(my_monster1.sounds())

# Second Monster

my_monster2 = Monsters('Donald Dracula', 'None', 'cute once apon a time', ['Fast', 'Handsome'])

# Characteristics
print('////////////////////////////////////////////////////////')
print(my_monster2.name)
print(my_monster2.fur_type)
print(my_monster2.skills) # optional list ['Strength', 'Poisonous', 'Mean']
print(my_monster2.cuteness)

# Methods

print(my_monster2.scare())
print(my_monster2.eat())
print(my_monster2.morph())
print(my_monster2.sounds())

# Third Monster

my_monster3 = Monsters('Big Foot Angus', 'Softest fur', 'to die for', ['excellent cook', 'Sensitive soul'])

# Characteristics
print('////////////////////////////////////////////////////////')
print(my_monster3.name)
print(my_monster3.fur_type)
print(my_monster3.skills) # optional list ['Strength', 'Poisonous', 'Mean']
print(my_monster3.cuteness)

# Methods

print(my_monster3.scare())
print(my_monster3.eat())
print(my_monster3.morph())
print(my_monster3.sounds())

