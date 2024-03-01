# 9-14 Lottery
# Make a list or tuple containing a series of 10 numbers and five letters. Randomly select 4 numbers or letters from the list
# And print a message saying that any ticket matching these four numbers or letters wins a prize.

from random import choice

# Creating Tickets and empty list of prize winners.
Tickets = ['1', '2', '3', '4', 'b','c','a','d','e','f']
Winners = []

# Select your 4 winners from the list of tickets.
while len(Winners) != 4:
    winner = choice(Tickets)
    # Adding selection to list of Winners
    Winners.append(winner)
    # Removing previous selection
    Tickets.remove(winner)
else:
    w1 = Winners[0]
    w2 = Winners[1]
    w3 = Winners[2]
    w4 = Winners[3]
    print(f"If your ticket matches {w1}, {w2}, {w3} or {w4} then you have earned a prize!")

# Just for fun lets do it as a class
from random import choice

class Lottery():
    
    def __init__(self, tickets=[]):
        self.tickets = tickets
        self.Winners = []
    
    def pick_winners(self):
        while len(self.Winners) != 4:
            winner = choice(Tickets)
            self.Winners.append(winner)
            self.tickets.remove(winner)
    
    def display_winners(self):
        w1 = self.Winners[0]
        w2 = self.Winners[1]
        w3 = self.Winners[2]
        w4 = self.Winners[3]
        print(f"If your ticket matches {w1}, {w2}, {w3} or {w4} then you have earned a prize!")

# Now to Test it
Tickets = ['1', '2', '3', '4', 'b','c','a','d','e','f']
lot_1 = Lottery(Tickets)
lot_1.pick_winners()
lot_1.display_winners()

