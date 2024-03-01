# 10-6
# Write an addition calculator, add a way to handle errors if the user inputs text instead of integers.
""" Addition Calculator """
print("Give me two numbers to add together.")
print("Enter \'q\' to quit.")

while True:
    num_one = input('\nFirst Number: ')
    if num_one == 'q':
        break
    num_two = input('\nSecond Number: ')
    if num_two == 'q':
        break
    try:
        answer = int(num_one) + int(num_two)
    except ValueError:
        print("You must use numbers!")
        break
    print(f"The answer is {answer}")

