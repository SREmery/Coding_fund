import random
import dice


def dice_throw():
    x = random.randint(1,6)
    print(x)

for i in range(0,2):
    dice.dice_throw()