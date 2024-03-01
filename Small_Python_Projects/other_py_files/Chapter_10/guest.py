# 10-3 Guest
file_path = "C:\\Users\\User\\Code_Environment\\Python Work\\Chapter_10\\guest_names.txt"

def write_to_file(file_path):
    print("What is your name?")
    name = input()
    with open(file_path, "a") as f:
        f.write(name + "\n")

write_to_file(file_path)
