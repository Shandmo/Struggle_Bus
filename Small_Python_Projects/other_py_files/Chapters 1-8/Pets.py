### 6-8 Pets ###
sammy = {
    'owner': 'Shawn',
    'name': 'Sammy'
    'animal_type': 'cat',
    'color': 'orange and white',
    'age': 21
}
clark = {
    'owner': 'Zaque',
    'name': 'clark'
    'animal_type': 'cat',
    'color': 'brown',
    'age': 8
}
scout = {
    'owner': 'Shandmo',
    'name': 'scout'
    'animal_type': 'dog',
    'color': 'brown',
    'age': 12
}

pets = [scout, sammy, clark]

for pet in pets:
    for key, value in pet.items():
        print(key,value)