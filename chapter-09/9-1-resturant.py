from restaurant import Restaurant
from restaurant import IceCreamStand

my_restaurant=Restaurant("Hammy's", "Ham")

my_restaurant.describe_restaurant()

my_restaurant.open_restaurant()

iscream_icecream =IceCreamStand("IScream", "Ice Cream")
iscream_icecream.describe_restaurant()
iscream_icecream.flavors = ["Chocolate"]
iscream_icecream.print_flavors()