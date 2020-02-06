## 9-1 Restaurant
## __init__ method should store two attributes. Make two methods, one that describes the restaurant, and one that "opens" the restaurant.

class Restaurant():

    def __init__(self, restaurant_name, cuisine_type):
        # attach attributes
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
    
    def describe_restaurant(self):
        print(f"Restaurant Name: {self.restaurant_name.title()}\nCuisine: {self.cuisine_type.title()}")
    
    def open_restaurant(self):
        print(f"{self.restaurant_name.title()} is open for business!")
