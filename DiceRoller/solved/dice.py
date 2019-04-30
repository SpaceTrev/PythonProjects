# import random module
import random

# declare a variable that stores a value equivalent to each side of the dice in a list (aka array)
dice = [1, 2, 3, 4, 5, 6]
# declare a variable that activates the random module and picks a random choice out of the list provided to the function
roll = random.choice(dice)

# prints the results of the simulated dice roll to the console
print(roll)

# there are a lot of ways to solve this one so be creative

# bonuse
# 0.00-100.00 randomizer
# onehunnit = random.random() * 100
