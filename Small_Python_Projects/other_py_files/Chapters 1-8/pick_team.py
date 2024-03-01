import random

def pick_team_two():
    players = []
    team_one = []
    team_two = []
    print('When you are done entering in player names type "do" and then type "done".')

    while True:
        player = input('Input player name: ')
        if player.lower() == 'done':
            team_two = players[:]
            return(team_one, team_two)
            break

        elif player.lower() == 'do':
            if len(team_one) < 4:
                for player in players:
                    x = random.choice(players)
                    team_one.append(x)
                    players.remove(x)
                    
        else:
            players.append(player)
            
pick_team_two()