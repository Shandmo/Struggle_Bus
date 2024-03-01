# 10-5 Programming Poll
file_path = "C:\\Users\\User\\Code_Environment\\Python Work\\Chapter_10\\programming_polls.txt"
flag = True
welcome_msg = ("Type \"quit\" to quit.")
print(welcome_msg)
with open(file_path, 'a') as f:
    while flag == True:
        print("Why do you like programming?")
        reason = input()
        if reason.lower() == "quit":
            flag = False
        else:
            f.write(reason + "\n")

