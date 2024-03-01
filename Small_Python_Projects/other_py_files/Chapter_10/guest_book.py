# 10-4 Guest Book
file_path = "C:\\Users\\User\\Code_Environment\\Python Work\\Chapter_10\\guest_book.txt"
flag = True
welcome_msg = ("Type \"quit\" to quit.")
print(welcome_msg)
with open(file_path, 'a') as f:
    while flag == True:
        print("Hello, what is your name?")
        name = input()
        if name == "quit":
            flag = False
        else:
            print(f"Thank you for staying with us {name.title()}, we hope you enjoy your time here.")
            f.write(name + "\n")