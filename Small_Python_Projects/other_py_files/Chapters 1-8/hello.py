print("The Very Beginning of My Python Adventures")

first_name = "shay"
last_name = "barnes"
full_name = first_name + " " + last_name
print(full_name)
#Page 21 the concept of 'f strings' are mentioned. 
full_name = f"{first_name} {last_name}"
print(full_name)
print(f"Hello, {full_name.title()}!")
#The title method converts every word to begin with an uppercase letter.
#f strings were introduced in python 3.6, to use them in earlier version you have to use format()
full_name = "Hello, {} {}!".format(first_name, last_name)
print(full_name)