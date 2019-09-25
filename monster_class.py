class Monsters():

    # Characterisitics
    def __init__(self, name, fur, cute_level, skills):
        self.name = name
        self.fur_type = fur
        self.skills = skills # optional list ['Strength', 'Poisonous', 'Mean']
        self.cuteness = cute_level

    # Behaviours - functions that belong to a class. Can
    # Methods -  functions that can only be used on this classes instance

    def scare(self):
        return 'Rawrrrr!'

    def eat(self):
        return 'Humans taste like A$$'

    def morph(self):
        return "It's Morphin time!"

    def sounds(self):
        return 'Silent as a mouse!'