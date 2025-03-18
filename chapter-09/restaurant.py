class Restaurant:
    """A restaurant"""
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
      print(f"This is {self.restaurant_name} that serves {self.cuisine_type}.")
    
    def open_restaurant(self):
       print(f"{self.restaurant_name} is now open!")

class IceCreamStand(Restaurant):
    """An Ice Cream Stand, child of Resturant"""
    def __init__(self, resturant_name, cuisine_type):
       super().__init__(resturant_name, cuisine_type)
       self.flavors = ["Vanilla"]

    def flavors(self, flavors):
        self.flavors = flavors

    def print_flavors(self):
       print(self.flavors)