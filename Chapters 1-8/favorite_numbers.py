### 6-10 Favorite Numbers ###
people ={
    'shandmo': ['green', 'blue', 'purple'],
    'jodi': ['red', 'black', 'teal'],
    'kevin': ['yellow', 'pink', 'white']
}
for key, value in people.items():
    print("{} favorite colors are: ".format(key.title()))
    for val in value:
        print("\t{}".format(val.title()))