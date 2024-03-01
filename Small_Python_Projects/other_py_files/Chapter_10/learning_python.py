#10-1 Learning Python

file_path = "C:\\Users\\User\\Code_Environment\\Python Work\\Chapter_10\\learning_python.txt"

# Print the file first by reading the entire thing.
with open(file_path) as file_object:
    contents = file_object.read()
    print(contents)

# Print the file by looping over the file
with open(file_path) as file_object:
    lines = file_object.readlines()
    for line in lines:
        print(line.strip())
# Print the file by storing the lines in a list and then working with them outside the with block.
with open(file_path) as file_object:
    lines = file_object.readlines()

for line in lines:
    print(line.strip().replace(".", "!"))
