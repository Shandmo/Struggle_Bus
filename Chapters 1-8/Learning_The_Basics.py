
def men_still_standing(cards):
    # generate teams
    A = {k: 0 for k in range(1, 12)}
    B = A.copy()
    
    for card in cards:
        # parse card
        team = A if card[0] == "A" else B
        player = int(card[1:-1])
        color = card[-1]
        
        if player not in team:
            continue
        
        # record penalty
        team[player] += 1 if color == "Y" else 2
        
        if team[player] >= 2:
            del team[player]
        
        if len(team) < 7:
            break
    
    return len(A), len(B)llist

def men_still_standing(cards):
    #Create the teams
    A = {k: 0 for k in range(1,12)}
    B = A.copy()

    for card in cards:
        #parse the card
        #make team = variable A or variable B depending on what value index value 0 of card holds.
        team = A if card[0] == "A" else B
        player = int(card[1:-1])
        color = card[-1]

        if player not in team:
            continue
        # Penalty tracking
        team[player] += 1 if color == "Y" else 2
        #2 yellows are required to remove a player or 1 red is required.
        
        if team[player] >= 2:
            del team[player]

        if len(team) < 7:
            break

    return len(A), len(B)
men_still_standing(["A4R", "A6R", "A8R", "A10R", "A11R"])
A = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0, 10: 0, 11: 0}
B = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0, 10: 0, 11: 0}

Card = 'A4Y'
The list changes when player 4 recieves a yellow card.
TeamA before any changes:
{1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0, 10: 0, 11: 0}
TeamA after play 4 recieves a yellow card.
{1: 0, 2: 0, 3: 0, 4: 1, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0, 10: 0, 11: 0}
		     ^^^
When player 4 recieves a red card, or 2 yellows.
{1: 0, 2: 0, 3: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0, 10: 0, 11: 0}


def men_still_standing(cards):

	TeamA = {k: 0 for k in range(1,12)}
	TeamB = TeamA.copy()

	for card in cards:
	#determine what team the card belongs to.	
		team = TeamA if card[0] == "A" else TeamB
	#determine what player the card belongs to.
		player = int(card[1:-1]
	#determine what color the card is.
		color = card[-1]

		if player not in team:
			continue
		
		team[player] += 1 if color == "Y" else 2
		
		if team[player] >= 2:
			del team[player]

		if len(team) < 7:
			break
	return len(TeamA), len(TeamB)
		


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
	#Useful if you know the index you want to delete.
list.pop()
	#Useful if you want to do something with the value being removed from the top of the list.
list.remove()
	#Useful if you do not know the index location of the value being removed.
list.sort()		list.sort(reverse=True)
	#Sorts list alphabetetically.	Sorts list reverse-alphabetically.
list.sorted()
	#Displays list as being sorted alphabetically, but does not change the list.
list.reverse()
	#Reverses the order of the list, can use it again to change it back to its original places.
len(list)
	#Returns an integer with the number of elements in a list.
range(1,5)		range(0, 11, 2)
	#Will create a range from 1 up to but not including 5. [1, 2, 3, 4]
#The second will create a range from 0 up to but not including 11, and will count up  by 2 numbers instead of by 1. [0, 2, 4, 6, 8, 10]
list(range(1,5))
	#Will create a list containing the numbers 1-4 [1, 2, 3, 4]
min(list)
	#Will return the smallest integer in the list.
max(list)
	#Will return the largest integer in the list.
sum(list)
	#Will return the sum of all integers in the list.
string.lower()
	#Returns string in all lowercase.
string.upper()
	#Returns string in all uppercase.
dictionary_name.get('key', <opt> 'No value assigned')
#Used to get the value of the key passed in parameter one, if key is not found then 'No value assigned' is returned. *If there is a chance that 	the dictionary key you are looking for does not exist, use the get() function over using bracket notation.

dictionary_name.items()
#This method will return a list of key value pairs. This piece of code is typical when trying to access all the key, value pairs for looping.
	for key, value in dictionary_name.items():
		##Code Block ##

dictionary_name.keys()
#Will only return the keys in the dictionary as a list. Useful when the values of the dictionary are not required. This is the default behavior when looping through keys. The code below operates the same with or without keys().
	for name in dictionary_name:
#This line is used if you want to explicity check for a key in the list of keys. We check if 'shandmo' is a key inside the best_people dictionary.
	if 'shandmo' in best_people.keys():
###Using sorted() to loop through dictionaries.
	for name in sorted(best_people.keys()):
#Will sort the keys in alphabetical order before iterating through the dictionary.

dictionary_name.values()
#Essentially does for values what keys() does for keys in a dictionary. Returns all values in a dictionary as a list.

set()
#Set is a collection in which each item must be unique.
	for set(best_people.values()):
#When set() is wrapped around a list that contains duplicate items, it will identify the unique items in the list and a build a set from those items.
#sets can be built directly using {}, Unlilke dictionaries sets do not have key: value pairs and do not retain items in any specific order.

input()
#The function takes one parameter. The prompt, which is text that will be printed to the user, so the user understands what to reply with. input() takes anything that the user responds with as a string.

int()
#useful when you want to get only a string from something like the input() function. This is "hardcasting" a variable so that it will only be interpreted as an integer.




List Comprehension:
squares = [value**2 for value in range(1, 11)]
	[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]or

If statements:
if only one condition needs to be true then an if-elif-else chain is appropriate.
if more than one condition needs to be true then make multiple if statements.
if you only want your code to execute if it passes one of the if-elif tests, then omit the else block. Python does not require this block.

Using the Modulo Operator (Modulus)
	This operator is useful when trying to determine if a number is even or odd.
if number % 2 == 0:
	print("The number {} is even.".format(number))
else:
	print("The number {} is odd.".format(number))

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
Page 99 Person
#Use dictionary to store info about a person, include first, last, age, and city. Print each piece of info stored in dictionary.
person = {'first_name': 'Kevin', 'last_name': 'Campbell', 'age': 23, 'city': 'Fort Hood'}
#for loop iterating over every value in person using the items() method.
for key, value in person.items():
	print("{}".format(value))

#create email for person
email = person['last_name'] + "." + person['first_name'] + str(person['age']) + '@easymail.com'
print("{}, your new email has been created for you: {}".format(person['first_name'].title(), email))


################################
Page 99 Favorite Numbers
#use dictionary to store people's favorites numbers, use numbers as the values and names as the keys. Print each person's name and their favorite number.
favorite_numbers = {
	'shandmo': 'green', 
	'kevin': 'red', 
	'madi': 'blue', 
	'BustMonkey': 'black',
	'moore':'purple'
	}

for key, value in favorite_numbers.items():
	print("{} favorite color is {}!".format(key.title(), value.title())

################################
Page 99 Glossary
#create a dictionary that contains 5 programming words and their definitions, print the key and their corresponding value.
glossary = {
	'keyword': 'Reserved words in Python, I cannot use them as variable or function names or as any other identfier',
	'variable': 'Variables are essentially labels for values. The values can change over the course of the program and the label can move from one value to another or removed altogether.',
	'function': 'Functions are pieces of code that perform a specific task.',
	'method': 'A method is different from a function, it is an instance of a class.',
	'loop': 'A loop is a powerful way to iterate over something multiple times. The most popular loops are For and While loops.'
	}

for key, value in glossary.items():
	print("{} - {}".format(key.title(), value))

################################
Page 105 Rivers
#3 rivers, loop through each one with a sentence. Then print each key and then print separately each value.
rivers = {
	'amazon river': 'brazil',
	'yangtze river': 'china',
	'mekong river': 'southeast asia'
	}

for key, value in rivers.items():
	print("The {} flows through {}.".format(key.title(), value.title()))

for key in rivers:
	print(key)

for value in rivers.values():
	print(value)

################################
Page 105 Polling
#Make a list of people who should take the favorite languages poll, add some into the list that have already taken it. Loop through the list and invite those who haven't taken it to take it, and thank all the others who have already.

favorite_languages = {
	'jen': 'python',
	'sarah': 'c',
	'edward': 'ruby',
	'phil': 'python'
	}

people = ['tom', 'john', 'allen', 'sarah', 'edward']

for person in people:
	if person in favorite_languages.keys():
		print("Thank you {} for taking the poll!".format(person.title()))
	else:
		print("Hello {}, you should take our favorite languages poll!".format(person.title()))

################################

words = "Make a list of people who should take the favorite languages poll, add some into the list that have already taken it. Loop through the list and invite those who haven't taken it to take it, and thank all the others who have already."

list_of_words = words.split()

for word in list_of_words[:5]:
	print(word)

print("The total number of words in our list is {}.".format(len(list_of_words)))
	
################################
#List in a dictionary
def whoami():
	
	character = {
		'class': 'hunter',
		'armor': 'mail',
		'pets': ['cat', 'bear', 'boar', 'raptor']
		}
	
	print("You are playing a {} that wears {} and has the following pets... ".format(character['class'].title(),character['armor']))
	
	for pet in character['pets']:
		print(pet.title())

whoami()

#Lists inside dictionaries are useful anytime you want to have multiple values associated with one key.

################################
#Nested Dictionaries
def user_dump():
users = {
	'lolkkok': {
		'first': 'kevin',
		'last': 'campbell',
		'location': 'fort hood',
		},
	'shandmo': {
		'first': 'shay',
		'last': 'barnes',
		'location': 'fort gordon',
		}
	}
	
	for username, user_info in users.items():
		print("Username: {}".format(username.title()))
		full_name = "{} {}".format(user_info['first'].title(),user_info['last'].title())
		print("\tName: " + full_name)
		print("\tLocation: " + user_info['location'].title() + "\n")

#Just to satisfy my own curiousity users.items() will output this...
#dict_items(
[('lolkkok', {'location': 'fort hood', 'first': 'kevin', 'last': 'campbell'}), ('shandmo', {'location': 'fort gordon', 'first': 'shay', 'last': 'barnes'})]
#)
#Here the keys 'lolkkok' and 'shandmo' have a dictionary as their value, which  contains their first name, last name and location.

user_dump()

################################
Page 112 People
#Create a dictionary representing different people, store all three in a list called people. Loop through your list of people and print all of what you know about each person.

#Working on this one currently.
people = [
	'Person One' = { 
		'first_name' 'Kevin',
		'last_name': 'Campbell',
		'age': 21, 
		'city': 'Fort Hood'
		}
	'Person Two': {
		'first_name': 'Shay',
		'last_name': 'Barnes',
		'age': 23,
		'city': 'Fort Gordon'
		},
	'Person Three': {
		'first_name': 'Jodi',
		'last_name': 'Moore',
		'age': 24,
		'city': 'Fort Gordon'
		} 
	]

#for loop iterating over every value in person using the items() method.
for key, value in person.items():
	print("{}".format(value))

#create email for person
email = person['last_name'] + "." + person['first_name'] + str(person['age']) + '@easymail.com'
print("{}, your new email has been created for you: {}".format(person['first_name'].title(), email))

################################
7-1 Page 117 Rental Car
#prompt user for what kind of car they want. print a msg about the car.
def rental_car():
	car = input("What kind of rental car would you like?")
	print("Let me see if I can find you a {}.".format(car.title()))

rental_car()

################################
7-2 Page 117 Restaurant Seating
#ask the user how many people in their group. If the answer is more than eight, print msg saying they have a wait. else report table is ready
def rest_seat():
	group_size = int(input("How many people are in your dinner group this evening?"))
	if group_size >= 8:
		print("There will be a 35 minute wait for your table.")
	else:
		print("Your table is available now.")

rest_seat()

################################
7-3 Page 117 Multiples of Ten

def multi_of_ten():
	number = int(input("Hello, please give me a number."))
	
	if number % 10 == 0:
		print("The number {} is divisible by 10.".format(number))
	else:
		print("The number {} is not divisible by 10.".format(number))

multi_of_ten()
	
################################
7-4 Pizza Toppings Page 123
#write loop that prompts user to enter a series of pizza toppings, until they quit. as each is being entered, print msg that topping is added to pizza.

while True:
	topping = input("What topping would you like on your pizza?")	
	print("{} will be added to your pizza".format(topping.title()))
	

################################
7-5 Movie Tickets Page 123
#movie ticket price varies on age. write loop which ask users their age, then tell them cost of ticket. under 3 = 0, 3-12 = 10, over 12 = 15
while True:
	age = int(input("How old are you?"))
	if age < 3:
		print("Your ticket is free.")
	elif age >= 3 and age <= 12:
		print("Your ticket is $10.")
	elif age > 12:
		print("Your ticket is $15.")

################################
7-6 Three Exits Page 124
#write version of 7-4 that also, uses a conditional test in a while statement to stop loop, use an active variable (flag) to control loop, use break statement to exit loop when user enters 'quit' value.
active = True
while active == True:
	toppings = set()	
	topping = input("What topping would you like on your pizza?\n Enter quit when you are done.")
	
	if topping.lower() == 'pineapple':
		print("Disgusting! No pizza for you!")
		active = False
	elif topping == 'quit':
		break
	else:
		toppings.add(topping)
		print("{} will be added to your pizza.".format(topping.title()))
		continue

################################
7-7 Infinity Page 124
#write loop that never ends, and run it.
num = 1
while num < 2:
	print(num)

################################
7-8 Deli Page 127
#make a list named sandwich_orders, fill it with names of sandwiches. make an empty list named finished_sandwiches. Loop thru the list of sandwich orders and print msg for each order. As each sammich is made, move it to the list of finished sandwiches. after all are made, print a msg listed each sandwich that was made.

def deli():
	sandwich_orders = ['Turkey', 'Ham and Cheese', 'Reuben', 'BLT']
	finished_sandwiches = []
	
	while sandwich_orders:
		for order in sandwich_orders:
			made_order = sandwich_orders.pop()
			finished_sandwiches.append(made_order)
			print("I made your {} sandwich.".format(made_order))
	
	for sandwich in finished_sandwiches:
		print("{} sandwich was made.".format(sandwich))

deli()

################################
7-9 No Pastrami Page 127
#use the list sandwich_orders. make sure the sandwich 'pastrami' appears in list three times. Add code near beginning of program to print a message saying the deli has run out of pastrami, then use loop to remove all occurences of pastrami from orders. 

def deli():
	sandwich_orders = ['turkey','pastrami', 'ham and cheese', 'pastrami',  'reuben', 'pastrami', 'BLT']
	finished_sandwiches = []
	
	while sandwich_orders:			#while orders not empty
		for order in sandwich_orders:
			if order == 'pastrami':
				print("We have run out of pastrami.")
				while order in sandwich_orders:			#remove all pastrami
					sandwich_orders.remove(order)
			else:
				made_order = sandwich_orders.pop()
				finished_sandwiches.append(made_order)
				print("I made your {} sandwich.".format(made_order))
	
	for sandwich in finished_sandwiches:
		print("{} sandwich was made.".format(sandwich.title()))

deli()

################################
7-10 Dream Vacation Page 127
#Write program, polls users about dream vacation. Include code block that prints the results of the poll.

def dream_vacation():
	poll_results = {}
	poll_status = True
	
	while poll_status:
		print("What is your name?")
		name = input()
		print("Hello {}, what is your dream vacation location?".format(name.title()))
		location = input()
		poll_results[name] = location
		print("Would you like anyone else to answer this poll? Type yes/no")
		answer = input()
	
		if answer.lower() == 'no':
			poll_status = False
		elif answer.lower() == 'yes':
			continue
		else:
			print("Error, please type \'yes\' or \'no\'")
	print("The poll is in!")
	for key, value in poll_results.items():
		print("{} wants to visit {}.".format(key.title(),value.title()))

################################
8-1 Message Page 131
#write function called display_message() that prints one sentence telling everyone what you are learning about in this chapter.

def display_message(name):
	print("Hello {}, I am learning about functions in this chapter.".format(name.title()))

################################
8-2 Favorite Book Page 131
#Write function called favorite_book(), that accepts on parameter, title. function should print msg.

def favorite_book(title,author):
	print("My favorite book is {} by {}.".format(title.title(),author.title()))

################################
8-3 T-Shirt Page 137
#write function called make_shirt() that accepts size and text of msg that should be printed on the shirt. Function should print a sentence summarizing the size of the shirt and the msg printed on it. Call function using positional and keyword arguements.

def make_shirt(size, message):
	print("The you want to make will be a size {}, and say \"{}\" on the front of the shirt.".format(size,message))

#call with positional arguements
make_shirt('medium', 'YUH BOI SHANDMO')
#call with keyword arguements
make_shirt(message = 'YUH BOI SHANDMO', size = 'medium')

################################
8-4 Large Shirts Page 137
#modify make_shirt() so that shirts are large by default with a message that reads I love Python. Make a large shirt and a medium shirt with the default message, and a shirt of any size with a different message.

def make_shirt(size='large', message='I love Python'):
	print("The you want to make will be a size {}, and say \"{}\" on the front of the shirt.".format(size,message))

#make a large shirt and medium shirt with default message
make_shirt()
make_shirt('medium')
#make shirt of any size with different message
make_shirt('small','BIG BOI SHANDMO')

################################
8-5 Cities Page 137
#write function called describe_city() that accepts name of city and country. the function should print sentence. Give the parameter for country a default value. Call function for three different cities, at least one which is not default country.

def describe_city(city_name,country_name='United States'):
	print("{} is in {}.".format(city_name.title(),country_name.title()))

describe_city('Houston')
describe_city('Atlanta')
describe_city('Seoul','Korea')

################################
8-6 City Names Page 142
#Write a function called city_country() that takes in the name of a city and its country. function should return something like "Santiago, Chile"

def city_country(city,country):
	msg = "{}, {}".format(city.title(),country.title())
	return msg

################################
8-7 Album Page 142
#write a function called make_album() that builds dictionary. the funciton should take in artist name and a title, return a dict containing these two pieces of info. Use funct to make three diff dicts. print each return value to show they are storing correctly.
#Use None to add an optional parameter to make_album() that allows you to store the number fo songs on an album. if the call line includes a value for the number of songs, add to dict.

def make_album(name,title,songs=None):
	album = {'name': name, 'title': title}
	if songs:
		album = {'name': name, 'title': title, 'songs': songs}
	return album

make_album('shandmo', 'undertaker', 9)
make_album('YURBOI','YUNGBLOOD', 12)
make_album('chief beef', 'Almighty Function')


################################
8-8 User Albums Page 142
# start with ex 8-7, write a while loop that allows user to enter an album's artist and title. call make_album() with the user's input and print the dict that should be created.

def make_album(name='',title='',songs=None):
	while True:
		print("What is your name?")
		name = input("> ")
		if name == 'q':
			break
		print("What is the title of your album?")
		title = input("> ")
		if name == 'q':
			break
		album = {'name': name, 'title': title}
		
		print("Number of songs in your album?")
		songs = input("> ")
		if songs:
			if songs == 'q':
				break
			else:
				album = {'name': name, 'title': title, 'songs': songs}
		return album

################################
Modify a list in a function
#make a list of my classes that aren't max level. Iterate over that and as each one is leveled to max level, add them to a different list for max levels.
characters = ['hunter', 'mage', 'warrior', 'paladin']

def char_levels(characters):
	max_levels = ['warlock', 'shaman']
	while characters:
		current_character = characters.pop()
		max_levels.append(current_character)
	return max_levels

#returned list = ['warlock', 'shaman', 'paladin', 'warrior', 'mage', 'hunter']
################################
8-9 Messages Page 146
#make list containing series of text msgs. pass the list to a funct called show_messages(), print each msg
text_messages = ["hi", "hello", "it's me", "the boi shandmo"]

def show_messages(messages):
    for message in messages:
        print("The message said \"{}\".".format(message))

################################
8-10 Sending Messages Page 146
#Start with copy of 8-9. write funt called send_messages(), print each text message and move each msg to a new list called sent_msgs as its
#printed. After calling the funct, print both lists to make sure the msgs were moved correctly.

text_messages = ["hi", "hello", "it's me", "the boi shandmo"]

def send_messages(messages):
    sent_messages = []
    while messages:
        current_message = messages.pop()
        print("Sending the message: \"{}\"".format(current_message))
        sent_messages.append(current_message)
    # print both lists. sent_msgs should have all the messages, and messages should be empty now.
    print("Sent messages: {}".format(sent_messages))
    print("Remaining messages:".format(messages)) 

send_messages(text_messages)
################################
8-11 Archived Messages Page 146
#Start with 8-10. Call the function send_messages() with a copy of the list of messages. After calling the function print both of your 
#lists to show that original has retained its messages
#The point of this exercise is to show a use case of how to prevent functions from modifying a list you passed to it.

def show_messages(messages):
    for message in messages:
        print("The message says \"{}\".".format(message))

def send_messages(messages):
    sent_messages = []
    while messages:
        current_message = messages.pop()
        print("Sending the message: \"{}\"".format(current_message))
        sent_messages.append(current_message)
    # print both lists. sent_msgs should have all the messages, and messages should be empty now.
    print("Sent messages: {}".format(sent_messages))
    print("Remaining messages:".format(messages))


text_messages = ["hi", "hello", "it's me", "the boi shandmo"]
#Using slice notation to send a copy of the list to the send_messages function.
send_messages(text_messages[:])
show_messages(text_messages)

################################









		












































