# Workout Logger

file_path = "C:\\Users\\User\\Documents\\Workout_Log.txt"
msg = ("Type \"quit\" to quit, \"clear\" to clear, \"read\" to display file contents, \"add\" to add an entry or \"help\" to see this message again.")
    
with open(file_path, 'a') as f:
    print(msg)
    while True:
        line = input("> ")
        if line == "quit":
            print("Goodbye youngster.")
            break
        elif line == "help":
            print(msg)
        elif line == "add":
            f.close()
            with open(file_path, 'a') as f:
                print("Enter Today's Date, format dd Apr yy")
                date = input(">> ")
                f.write(date + "\n")
                print("format is exercise: SetsxReps:weight")
                scheme = input(">> ")
                f.write(scheme + "\n")
                print("Entry added successfully.")
        elif line == "read":
            f.close()
            with open(file_path, 'r+') as f:
                section = f.readlines()
                for section in lines:
                    print(section.strip())
        elif line == "clear":
            f.close()
            with open(file_path, 'r+') as f:
                f.truncate(0)
                print("Cleared successfully.")
        else:
            print("That's isn't an option, type \"help\" for the menu.")
                 


