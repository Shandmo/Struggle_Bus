## Buying A Car ##
def nbMonths(old, new, saving, percent):
    month = 0
    while old - new + saving * month < 0:
        month += 1          #Iterating the month counter
        devalue = (100.0 - percent - 0.5 * (month // 2)) / 100.0        #100 - 1.5 - .5 (increasing devalue) * month // 2 (Floor Division / 100.0
        old *= devalue                                                  #Because of PEMDAS the first thing to be evaluated is (month // 2) which equals 0 on month 1.
        new *= devalue                                                  #Month One = 0.5 * (0) = 0;   Month Two = 0.5 * (1) = 0.5
        #print(month)                                                    #100 - 1.5 - 0 / 100 = .985; Month Two = 100 - 1.5 - 0.5 = .980
        #print(old)                                                      #The genius of the devalue is that the 0.5 extra addition to the percent will only increase every 2 months
        #print(new)
    return [month, round(old - new + saving * month)]

nbMonths(2000, 8000, 1000, 1.5)

## Replace with Alphabet Position ##
def alphabet_position(text):
    text = [char for char in text]
    final = []
    for letter in text:
        letter = letter.lower()  #convert all letters to lowercase
        letter = (ord(letter) - 96) #use ord() -96 to get a characters 
        #ASCII position and then minus 96 as 97 is where the Lowercase part of the alphabet starts
        final.append(letter) #append each lowercase letter to the list final
    final = [item for item in final if item >= 0] #remove all negative numbers from final, this stops
    #all non lowercase alphabet characters from being in the list.
    final = ' '.join(map(str, final)) # join the list of integers with whitespace as delimeter
    return(final)

''' Output
Iteration One
1
1970.0          #2000 *= .985
7880.0          #8000 *= .980
Iteration Two
2
1930.6
7722.4
Iteration Three
3
1891.9879999999998
7567.951999999999
Iteration Four
4
1844.6882999999998
7378.753199999999
Iteration Five
5
1798.5710924999998
7194.284369999999
Iteration Six
6
1744.6139597249999
6978.455838899999
[6, 766]
'''