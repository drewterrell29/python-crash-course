

active = True

while active == True:
    topping = input("Give me the name of a topping: ")
    if topping == "quit":
        active = False
    if topping == "quit" and active == False:
        break #kinda silly
    print(f"Your topping is {topping}")
