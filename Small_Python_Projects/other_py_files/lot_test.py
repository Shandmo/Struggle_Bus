class Lottery_Analysis:

    def __init__(self, tickets=[])
        self.tickets = tickets
        self.counter = 1
        self.my_ticket = 1
    
    def pick_winner(self):
        winner = choice(tickets)
        if winner != my_ticket:
            choice(tickets)
            self.counter += 1
    
    def print_iterations(self):
        print(f"It took {self.counter} times for your ticket to get chosen!")