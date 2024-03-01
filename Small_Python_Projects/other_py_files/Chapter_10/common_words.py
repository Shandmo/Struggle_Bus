# 10-10 Common Words

def word_counter(file_name, word):
    file_name = "C:\\Users\\User\\Code Environment\\Python Work\\Read_Write\\" + str(file_name)
    # Grab the files contents
    with open(file_name, encoding='utf-8') as f:
        contents = f.read()
    # Check how many times the word "the" appears in the file regardless of case.
        times_counted = contents.lower().count(str(word))
    return(times_counted)

word_counter("trench_warfare_book.txt", "the ")
# This also counts all words that contain "the" such as "there", "then", etc.
# passing with an additional space will more accurately reflect how many times just "the" appears.
# Count before using .lower() function: 2410
# Count after .lower(): 2831
# Count after passing the additional space: 2165

