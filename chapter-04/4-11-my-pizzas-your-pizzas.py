pizzas = ["cheese", "pepperoni", "hamburger"]

friend_pizzas = pizzas[:]

pizzas.append("pinapple")

friend_pizzas.append("italian sausage")

print(f"My favorites pizzas are: {pizzas}")

print(f"My friend's favorite pizzas are: {friend_pizzas}")

for i in pizzas:
    print(f"Mine: {i}")
for j in friend_pizzas:
    print(f"Yours: {j}")