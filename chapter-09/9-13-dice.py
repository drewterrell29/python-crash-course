from random import randint
class dice():

    def roll_die():
        return randint(1,6)

result = dice.roll_die()
i = 0
while i < 10:
    print(dice.roll_die())
    i += 1