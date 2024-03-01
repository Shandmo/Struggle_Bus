from random import randint,choice
 
 """ Demonstrating using Python Standard Library imports"""
#Using randint to get a random number from 1 to 6.
randint(1,6)
#Using choice to make a choice from a tuple or list and choose one of the elements randomly.
players = ['beef','shama','dots','classycat','xythur',]
choice(players)

# 9-13 Dice
# Make a class Die with on attrib called sides, which has a default value of 6.
# create a method that rolls the dice and prints a random number between 1 and the number of sides the die has. 
# Make yours 6 sided and roll 10 times.

from random import randint

""" Represent a die that can be rolled """

class Die():

    def __init__(self, sides=6):
        # Initialize the die.
        self.sides = sides

    def roll_die(self):
        #Return a number between 1 and the number of sides.
        return(randint(1, self.sides))

# Make a six-sided die and roll it 10 times, display the results.
six_sider = Die()
rolls = []
for roll_num in range(10):
    roll = six_sider.roll_die()
    rolls.append(roll)
print("10 rolls of your six-sided die.")
print(rolls)

# Make a ten-sided die and 20-sided die and roll each 10 times.
ten_sider = Die(10)
twenty_sider = Die(20)
rolls = []
for roll_num in range(10):
    roll = ten_sider.roll_die()
    rolls.append(roll)
print("10 rolls of your ten-sided die.")
print(rolls)
rolls = []
for roll_num in range(10):
    roll = twenty_sider.roll_die()
    rolls.append(roll)
print("20 rolls of your twenty-sided die.")
print(rolls)