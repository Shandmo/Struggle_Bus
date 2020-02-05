""" My first attempt at the WOW POKEMON BATTLE """
from random import randint, choice
import os
import time
global fight_timer

class Boss():
    def __init__(self):
        names = ['Ragnaros', 'General Angerforge','B0SS0FALLB0SSES0']
        self.name = choice(names)
        self.health = 300
        self.attack = 85
        self.defence = 85
        self.life = True
    
    def dialogue(self):
        if self.name == "Ragnaros":
            print("By fire be purged!")
        elif self.name == "General Angerforge":
            print("You're back for the trinket AGAIN?")
        elif self.name == "B0SS0FALLB0SSES0":
            print("Prepare for the sMacKerY DacKerY!")



class Player():
    
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.max_health = 100
        self.attack = 100
        self.defence = 100
        self.weapon = 0
        self.weaponName = "Worn Battleaxe"
        self.life = True

    def health_check(self):
        if self.health >= self.max_health:
            self.health = self.max_health
            return False
        else:
            return True


########################### Variables ####################################
def intro():
    print("Welcome to the slimiest")
    time.sleep(1)
    print("the slaTTiest")
    time.sleep(1)
    print("The most InSanE iN ThE MemBraNe game you'll ever play.")

# variables
error_message = ""
Still_alive = True


################# Actually Starting the game ##########
intro()
player = Player('shandmo')
boss = Boss()
print(f"You enter a the large structure and you are faced against your first enemy... {boss.name}")
time.sleep(5)
boss.dialogue()
### Combat Loop ###
""" Currently trying to figure out how the combat turn-based style is going to be written. """
