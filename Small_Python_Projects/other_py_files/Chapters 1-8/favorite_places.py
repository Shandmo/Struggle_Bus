### 6-9 favorite_places ###
### List inside dictionary use case ###

favorite_places = {
    'Jodi':['texas','south carolina'],
    'Kaleb':['florida','oregon'],
    'Shay':['kentucky','virginia']
}
for key,value in favorite_places.items():
    print("{}'s favorite places are: ".format(key))
    for val in value:
        print("\t {}".format(val.title()))
