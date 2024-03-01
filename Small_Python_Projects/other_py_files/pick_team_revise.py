import random

def pick_team_two():
    players = []
    team_one = []
    team_two = []
    print("3v3 or 4v4? Enter 3 or 4: ")
    MAX = int(input()) #Sets the max amount of players for the teams.

    print("Input player names: ")       #Recieve input for players.
    while len(players) != (MAX * 2):
        player = input()
        players.append(player)

    for player in players:          #Fill team_one
        x = random.choice(players)
        team_one.append(x)
        players.remove(x)
        if len(team_one) == MAX:
            while len(team_two) != MAX:     #Fill team_two
                for player in players:
                    x = random.choice(players)
                    team_two.append(x)
                    players.remove(x)
#print neat output so they don't have to read a python list
    print("Blue Team has chosen: ")
    for member in team_one:
        print("\t" + member.title())
    print("Red side has chosen: ")
    for member in team_two:
        print("\t" + member.title())

pick_team_two()