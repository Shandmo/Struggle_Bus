# 10-8 Cats and Dogs
# Make two files, store at three names of cats in the first file and three names of dogs in the second file.
# Write a program that tries to read these files and print the contents of the file to the screen.
# Wrap your code in a try-except block to catch the FileNotFound error, and print a friendly message if the file is missing.
# Move one of the files to a different location to test that the except block is properly working.

cat_file = "C:\\Users\\User\\Code Environment\\Python Work\\Read_Write\\cats.txt"
dog_file = "C:\\Users\\User\\Code Environment\\Python Work\\Read_Write\\dogs.txt"
print("Hello, welcome to Cats and Dogs!")   

def read_file(*file_names):
    for file_name in file_names:        
        # Open, read, and print the names in the dogs file.
        file_name = "C:\\Users\\User\\Code Environment\\Python Work\\Read_Write\\" + str(file_name) + ".txt"
        try:
            with open(file_name, 'r') as f:
                contents = f.readlines()
                print(f"\nFrom {file_name}:")
                for line in contents:
                    print(line.strip())        
        except FileNotFoundError:
            #pass
            print(f"{file_name}.txt could not be found.")

# 10-9
# Modify the except block in 10-8 to fail silently if either file is missing.
# The execute block would be modified to contain python's pass statement.

read_file("cats","dogs","struggle")

""" Output
From C:\Users\User\Code Environment\Python Work\Read_Write\cats.txt:
cat_name1
cat_name2
cat_name3

From C:\Users\User\Code Environment\Python Work\Read_Write\dogs.txt:
dog_name1
dog_name2
dog_name3
C:\Users\User\Code Environment\Python Work\Read_Write\struggle.txt.txt could not be found.
"""