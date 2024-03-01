### 6-11 Cities ###
#use names of three cities as keys, store information about each city, include its country, population, and one fact.

cities = {
    "Washington D.C.": {
        "country": 'United States',
        "population": 1_250_000,
        "neat fact": "The \"D.C.\" part stands for District of Columbia."
    },
    "Baghdad": {
        "country": "Afghanistan",
        "population": 856_000,
        "neat fact": "This city gets shit on constantly by terrorists."
    },
    "Paris": {
        "country": "France",
        "population": 5_000_000,
        "neat fact": "The germans straight dicked this one."
    }
}

for key,value in cities.items():        #get the keys/values from cities.
    print("\n{}".format(key))           #Print the city name (key).
    for k,v in value.items():           #get the key/values from the internal dictionary.
        if k == "country":              #multiple conditionals to add extra text formatting to the output.
            print("Location: {}".format(v))
        elif k == "population":
            print("Estimated population: {}".format(v))
        elif k == "neat fact":
            print("Neat fact: {}".format(v))