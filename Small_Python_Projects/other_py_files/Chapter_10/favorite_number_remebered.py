# 10-12 Favorite Number Remembered
# Prompt for the user's favorite number, store the number in a file.
# Write a program that reads this value and prints a message "I know your favorite number! It's __."

import json

def greet_user():
    username = input("What is your name?\n>  ")
    filename = "C:\\Users\\User\\Code Environment\\Python Work\\Read_Write\\" + username + ".json"
    # Check if user exists
    try:
        # If they do exist, open the file and load their Key:Value pair.
        with open(filename) as f:
            datastore = json.load(f)
            # Greet the user with their stored username and number.
            for k,v in datastore.items():
                print(f"Welcome back {k.title()}, we remember your favorite number to be {v}.")
    except FileNotFoundError:
        # If they do not exist, ask for their favorite number
        # Then store this information by calling the store_new_user funct
        fav_num = input("What is your favorite number?\n> ")
        store_new_user(username, fav_num, filename)
        print(f"Hello {username.title()}, we will remember your favorite number.")

def store_new_user(username, fav_num, filename):
    with open(filename, 'w') as f:
        # Create a dictionary to store the username and their favorite number.
        profile_dict = {username:fav_num}
        json.dump(profile_dict, f)
        
