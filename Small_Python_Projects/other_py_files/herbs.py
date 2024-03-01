# Herbs in wow and their correlating crafts that i care about
herbs = {
    "Dreamfoil": ["Major Mana", "Greater Shadow Protection", "Greater Fire Protection"],
    "Fadeleaf": ["Greater Shadow Protection", "Lesser Inivisbility Potion"],
    "Gravemoss": "Greater Shadow Protection",
    "Khadgar's Whisker": ["Magic Resistance Potion", "Greater Mana Potion"],
    "Purple Lotus": ["Magic Resistance Potion", "Mana Oils"],
    "Wild Steelbloom": "Lesser Invisibility Potion",
    "Goldthorn": ["Greater Mana Potion", "Restorative Potion"]
}

def display_all_herbs():
    # Iterate through and print the herb name, and then print each thing it make.
    for key, value in herbs.items():
        # Check if the value of the herb is a list (Containg multiple values).
        if isinstance(value, list):
            # If the value is a list then iterate through and print each value.
            print(f"\n{key} can be used to make:")
            for value_item in value:
                print(f"-{value_item}")
        else:
            # If the value isn't a list than just print the singular value.
            print(f"\n{key} can be used to make:\n-{value}")

def display_herb(herb_name):
    try:
        msg = f"\n{herb_name.title()} can be used to make:"
        for herb in herbs[herb_name.title()]:
            msg = msg + (f"\n-{herb}")
        print(msg)
    except KeyError:
        print("Couldn't find an herb by the name.")

# Making the program interactive...
# Have a help menu that displays the possible options.
# have the options do the appropriate taks with the functions defined above.
Commands = ["get_herb","display_all","help","quit"]
print("Hello, welcome to herbs.py. Type \"help\" to see the menu.")
while True:
    user_input = input("> ")
    if user_input.lower() == "help":
        print("\nCommands:")
        for command in Commands:
            print(f"-{command}")
    elif user_input.lower() == "get_herb":
        while True:
            print("\nPlease enter the herb name, type \"done\" when you are done searching.")
            user_input = input("> ")
            display_herb(user_input)
    elif user_input.lower() == "quit":
        break
    elif user_input.lower() == "display_all":
        display_all_herbs()
    else:
        print("That is not a valid option. Use \"help\" to see the commands menu.")
