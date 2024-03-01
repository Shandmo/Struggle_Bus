# 9-15 Lottery Analysis
""" Lottery analysis that will determine how many times until your ticket matches the winning ticket."""
""" Ticket example looks like ['d', 'a', '9' 'e'] """
""" The possible numbers are 1-10, and the possible letters are a-e """
 
from random import choice
 
""" Create the winning ticket """
def select_winning_ticket(possibilities):
    winning_ticket = []
    while len(winning_ticket) < 4:
        random_item = choice(possibilities)
        # Check that the random item isn't already in the winning ticket. AKA no duplicates.
        if random_item not in winning_ticket:
            winning_ticket.append(random_item)
   
    return winning_ticket
 
""" Create your ticket """
def create_random_ticket(possibilities):
    my_ticket = []
    while len(my_ticket) < 4:
        random_item = choice(possibilities)
        # Again checking that the random item hasn't been chosen previously.
        if random_item not in my_ticket:
            my_ticket.append(random_item)
    return my_ticket
 
""" Function to check if your ticket is one of the winning tickets """
def check_ticket(winning_ticket, my_ticket):
    #Check to make sure each position and letter/number matches the winning ticket.
    if my_ticket[0] not in winning_ticket[0]:
        return False
    if my_ticket[1] not in winning_ticket[1]:
        return False
    if my_ticket[2] not in winning_ticket[2]:
        return False
    if my_ticket[3] not in winning_ticket[3]:
        return False
 
    return True
 
game_over = False
possibilities = ['1','2','3','4','5','6','7','8','9','10','a','b','c','d','e']
iterations = 0
max_attempts = 1_000_000
 
# Create Winning Ticket
winning_ticket = select_winning_ticket(possibilities)
 
while not game_over:
    # Create your ticket, keep randomly making your ticket until it matches the winning ticket.
    my_ticket = create_random_ticket(possibilities)
    game_over = check_ticket(winning_ticket, my_ticket)
    iterations += 1
    if plays >= max_attempts:
        break
 
if game_over:
    print("A match has been found.")
    print(f"The winning ticket is: {winning_ticket}")
    print(f"Your ticket is: {my_ticket}")
    print(f"It took {iterations} times for your ticket to be chosen!")
else:
    print(f"No match was found after {iterations} times.")