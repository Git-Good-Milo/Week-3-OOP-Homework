class Monsters():

    # Characterisitics
    def __init__(self, name, fur, cute_level, skills):
        self.name = name
        self.fur_type = fur
        self.skills = skills
        self.cuteness = cute_level

    # Behaviours - functions that belong to a class.
    # Methods -  functions that can only be used on this classes instance

    def scare(self, default_scare = ''):
        return 'Rawrrrr!' + default_scare

    def eat(self, default_food = 'Humans'):
        return default_food + '!?!?' + default_food + ' taste like A$$'

    def morph(self, transformation):
        return "It's Morphin time! " + '' + 'Swoosh! ' + transformation

    def sounds(self, special_sound):
        return 'Silent as a... ' + special_sound