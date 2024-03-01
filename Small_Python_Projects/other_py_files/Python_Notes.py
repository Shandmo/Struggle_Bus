def men_still_standing(cards):
    # generate teams
    TeamA = {k: 0 for k in range(1, 12)}
    TeamB = TeamA.copy()
    
    for card in cards:
        # parse card
        #deciding which team the card belongs to. Using a variable declaration followed by a conditional if else statement.
        team = TeamA if card[0] == "A" else TeamB
        #print(team)
        #print(card)
        player = int(card[1:-1])
        #what happens above is that card will equal "A4Y" for example.
        #card[1:-1] is reading "A4Y" starting at index 1 and stops before the last element (because of the -1)
        #so in our example we would start reading at "4" and stop at "4" because the -1 doesn't have us read the Y"
        #then we are passing the '4' to int() to make '4' a integer 4
        print ("This is the player:" + str(player))
        color = card[-1]
        #here card[-1] is reading only the last element of the string. In the example "A4Y" that means that only "Y"
        #is being read, and assigning the string 'y' to color
        #print(color)
        
        if player not in team:
        #checking to see if the integer variable player is still within the team, this eliminates integers that are outside
        #of the range 1-11, and prevents the program form trying to remove the same player twice.
            continue
        
        # record penalty
        #going back to the k: 0 for k in range(1,12), this in incrementing the 0 by 1 if yellow and incrementing by 2 if red.
        team[player] += 1 if color == "Y" else 2
        print("This is team[player]: " + str(team[player]))
        if team[player] >= 2:
            del team[player]
            
        if len(team) < 7:
            break
    
    return len(TeamA), len(TeamB)
#################################
Notes:
Useful Functions:
list.title()
list.append(element)
list.insert(0, element)
    parameter 1 = index location
    parameter 2 = element being inserted into list
del list[0]
    Useful if you know the index you want to delete.
list.pop()
    Useful if you want to do something with the value being removed from the top of the list.
list.remove()
    Useful if you do not know the index location of the value being removed.
list.sort()     list.sort(reverse=True)
    Sorts list alphabetetically.    Sorts list reverse-alphabetically.
list.sorted()
    Displays list as being sorted alphabetically, but does not change the list.
list.reverse()
    Reverses the order of the list, can use it again to change it back to its original places.
len(list)
    Returns an integer with the number of elements in a list.
range(1,5)      range(0, 11, 2)
    Will create a range from 1 up to but not including 5. [1, 2, 3, 4]
    The second will create a range from 0 up to but not including 11, and will count up  by 2 numbers instead of by 1. [0, 2, 4, 6, 8, 10]
list(range(1,5))
    Will create a list containing the numbers 1-4 [1, 2, 3, 4]
min(list)
    Will return the smallest integer in the list.
max(list)
    Will return the largest integer in the list.
sum(list)
    Will return the sum of all integers in the list.
string.lower()
    Returns string in all lowercase.
string.upper()
    Returns string in all uppercase.
List Comprehension:
squares = [value**2 for value in range(1, 11)]
    [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]or
If statements:
if only one condition needs to be true then an if-elif-else chain is appropriate.
if more than one condition needs to be true then make multiple if statements.
if you only want your code to execute if it passes one of the if-elif tests, then omit the else block. Python does not require this block.
Possible Ideas for the future:
Mile tracker for biking and running. Displays information based on a per week and per month basis.
Workout Tracker to display what I did on each particular day and whether or not it was an increase or decrease compared to the last workout of that type.
#################################
import random
def pick_team(players):
    #players = ['kevin', 'shandmo', 'sticky', 'doniel', 'tom', 'madi']
    team_one = []
    team_two = []
    if len(team_one) < 3:
        for player in players:
            x = random.choice(players)
            team_one.append(x)
            players.remove(x)
            #print('Team One now has: ' + x)
            team_two = players[:]
    return(team_one, team_two)
####################################
Pick_team version 2
#With this version I hope to add the ability to input player names
import random
def pick_team_two():
    players = []
    team_one = []
    team_two = []
    print('When you are done entering in player names type "do" and then type "done".')
    while True:
        player = raw_input('Input player name: ')
        if player == 'done':
            team_two = players[:]
            return(team_one, team_two)
            break
        elif player == 'do':
            if len(team_one) < 3:
                for player in players:
                    x = random.choice(players)
                    team_one.append(x)
                    players.remove(x)
                    
        else:
            players.append(player)
########################################
def Guest_Invite():
    guests = ['doniel', 'kevin', 'sticky']
    print("Inviting guests to dinner...\n")
    for guest in guests:
        print("Hello {}, you are invited to dinner!".format(guest.title()))
    
    print("\nSorry to hear you can't make it {}".format(guests[2].title()))
    del guests[-1]
    guests.append('tom')
    print("Re-inviting updated guest list...\n")
    for guest in guests:
        print("Hello {}, you are still invited to dinner!".format(guest.title()))
    
    print("Bigger table, more peeps!")
    print("Adding three additional guests...\n")
    guests.insert(0, 'first')
    guests.insert(2, 'middle')
    guests.append('final')
    
    for guest in guests:
        print("Hello {}, there are even more of you coming to dinner now!".format(guest.title()))
    print("\nSorry to inform all of you, but the bigger table isn't available only two of you will go.")
    print("Updating guest list again...\n")
    while len(guests) > 2:
        uninvited = guests.pop()
        print("Sorry {}, but we won't have room for you tonight.".format(uninvited.title()))
    
    for guest in guests:
        print("Hello {}, you're still on the list to come to dinner!".format(guest.title()))
    del guests[0]
    del guests[0]
    print("\nPrinting final empty list...\n" + str(guests))
    print("Function completed successfully!")
Guest_Invite()
###############################
Page 46 Seeing the World
def See_The_World():
    places = ['korea', 'belgium', 'switzerland', 'hawaii', 'germany']
    print("Printing list...")
    print(places)
    print("Printing sorted list...")
    print(sorted(places))
    print("Showing original list is unchanged...")
    print(places)
        
    places.reverse()
    print("Showing reversed list...")
    print(places)
    print("Changing back to original...")
    places.reverse()
    print(places)
    places.sort()
    print("Printed sort list...")
    print(places)
    places.sort(reverse=True)
    print("Printing reverse sorted list...")
    print(places)
See_The_World()
###############################
Page 78
conditional_tests.py
#testing for string equality and inequality.
game = 'wow'
if game == 'wow':
    print("{} is the best game!".format(game.upper()))
else:
    print("{}? What is that?".format(game))
#test using the lower() method
usernames = ['shandmo', 'lolkkok', 'madimook', 'doniel1k']
new_name = 'ShAnDmO'
for name in usernames:
    if name.lower() == 'lolkkok':
        print("{} is taken".format(name))
    elif name.lower() == 'shandmo':
        print("{} is taken".format(name))
    else:
        print("{} sucessfully created!".format(name))
#numerical test involving equality and inequality, >, <, >=, <=
age = 24
age_two = 30
if age > 23:
    print("success")
if age < 23:
    print("fail")
if age_two >= 29:
    print("success")
if age_two <= 29:
    print("fail")
#should evaluate to success, twice.
#Tests using and keyword
vehicle = 'Ford F-150'
color = 'red'
state = 'kentucky'
if vehicle == 'Ford F-150' and color == 'red' and state == 'kentucky':
    print("yes")
else:
    print("no")
#should evaluate to yes.
#Test whether item is in list
friends = ['kevin', 'madi', 'tom', 'doniel', 'zac']
if 'sticky' in friends:
    print('no way')
elif 'tom' in friends:
    print('yes way')
#should evaluate to 'yes way'
#test whether an item is not in a list
friends = ['kevin', 'madi', 'tom', 'doniel', 'zac']
if 'sticky' not in friends:
    print('lmfao')
else:
    print('what')
#should evaluate to 'lmfao'
###############################
Alien Colors 1
player = input("Enter your name: ")
alien_color = 'green'
if alien_color == 'green':
    print("{} just earned 5 points!".format(player))
Alien Colors 1.1
#Expects no output
alien_color = 'red'
if alien_color == 'green':
    print("You just earned 5 points!")
###############################
Alien Colors 2
#expects to run the else block
alien_color = 'yellow'
if alien_color == 'green':
    print('You earned 5 points!')
else:
    print('You earned 10 points!')
Alien Colors 2.1
#expect to run the if block
alien_color = 'green'
if alien_color == 'green':
    print('You earned 5 points!')
else:
    print('You earned 10 points!')
###############################
Alien Colors 3
#expects green
alien_color = 'green'
if alien_color == 'green':
    print('You earned 5 points!')
elif alien_color == 'yellow':
    print('You earned 10 points!')
elif alien_color == 'red':
    print('You earned 15 points!')
Alien Colors 3.1
#expects yellow
alien_color = 'yellow'
if alien_color == 'green':
    print('You earned 5 points!')
elif alien_color == 'yellow':
    print('You earned 10 points!')
elif alien_color == 'red':
    print('You earned 15 points!')
Alien Colors 3.2
#expects red
alien_color = 'red'
if alien_color == 'green':
    print('You earned 5 points!')
elif alien_color == 'yellow':
    print('You earned 10 points!')
elif alien_color == 'red':
    print('You earned 15 points!')
###############################
Stages of Life
ages = [age for age in range(0,66)]
for age in ages:
    if age < 2:
        print("baby")
    elif age >= 2 and age < 4:
        print("toddler")
    elif age >=4 and age < 13:
        print("kid")
    elif age >= 20 and age < 65:
        print("adult")
    else:
        print("elder")
###############################
Favorite fruit
def fav_fruit():
    fav_fruits = ['apple', 'orange', 'banana', 'blueberry', 'raspberry', 'kiwi']
    if 'blackberry' in fav_fruits:
        print('yay blackberries')
    if 'apple' in fav_fruits:
        print('yay apples')
    if 'banana' in fav_fruits:
        print('yay bananas')
fav_fruit()
###############################
games = ['wow','league','starcraft']
#Intially if statement is checking to see if list is empty.
#Using the name of a list as your if statement will cause Python to check to see if that list has at least one item in it. If it does then Python evaluates this state as True and executes the code below.
if games:
    for game in games:
        if game == 'wow':
            print("I play WoW!")
        else:
            print("I play {}.".format(game.title()))
else: #if list is empty the code below will execute.
    print("You have no games!")
################################
def get_soda():
    available_sodas = ['coke', 'sprite', 'canada dry']
    requested_sodas = ['coke', 'corona', 'fruit punch']
    for requested_soda in requested_sodas:
        if requested_soda in available_sodas:
            print('Adding {} to your order.'.format(requested_soda.title()))
        else:
            print('Sorry {} is not available at this location.'.format(requested_soda.title()))
    print('Code successfully finished!')
get_soda()
################################
Page 89 Hello Admin
def login_greeting():
    users = ['bob', 'sam', 'admin', 'shay', 'kevin']
    
    if users:
        for user in users:
            if user.lower() == 'admin':
                print("Hello Admin, would you like to see a status report?")
            else:
                print("Hello {}, when are you going to be the next admin?".format(user.title()))
    else:
        print("We need to find some users!")
login_greeting()
################################
Page 89 No Users
def login_greeting():
    users = []
    
    if users:
        for user in users:
            if user.lower() == 'admin':
                print("Hello Admin, would you like to see a status report?")
            else:
                print("Hello {}, when are you going to be the next admin?".format(user.title()))
    else:
        print("We need to find some users!")
login_greeting()
################################
Page 89 Checking Usernames
def check_username():
    current_users = ['bob', 'sam', 'admin', 'shay', 'kevin']
    new_users = []
    Max_Length = 5
    while len(new_users) < Max_Length:
        new_user = input("Enter desired username: ")
        new_users.append(new_user)  
    
    if new_users:
        for new_user in new_users:
            if new_user.lower() in current_users:
                print("{} is already a user! Try another name instead.".format(new_user.title()))
            else:
                print("{} username is available!".format(new_user.title()))
    else:
        print("Error, no users found!")
check_username()
################################
Page 89 Ordinal Numbers
numbers = [number for number in range(1,10)]
for number in numbers:
    if number == 1:
        print('1st')
    elif number == 2:
        print('2nd')
    elif number == 3:
        print('3rd')
    else:
        print(str(number) + "th")
################################
Create fake emails (First Dictionary Use)
def create_fake_emails():
import random
import string
chars = string.ascii_letters + string.digits + '!@#$%^&*()'
#The list names list will create a random email such as John96@gmail.com
names = ['Shandmo', 'Moore', 'BustMonkey', 'StruggleBus']
usernames_and_passwords = {}
for name in names:
    name_extra = ''.join(random.choice(string.digits))
    name_extra_two = ''.join(random.choice(string.digits))
    
    #Use the name and add two random digits
    username = name.lower() + name_extra + name_extra_two + '@gmail.com'
    #create a password with any character from chars that is 8 characters in length
    password = ''.join(random.choice(chars) for i in range(8))
    #Add the key : value pair to the dictionary
    usernames_and_passwords[username] = password
################################
