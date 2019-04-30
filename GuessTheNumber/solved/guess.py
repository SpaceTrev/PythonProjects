# import the random module
import random

# declare a variable and call the random module and the randint feature off of it then stating the range.
computerguess = random.randint(1, 10)

# declare variable that takes a console input, wrap it in the integer function forcing it's type to be a number aka integer
userinput = int(input())

# if the user input is greater that the computers guess print that to the console
if userinput > computerguess:
    print("guess too high")
# if the user input is less than the computers guess print that to the console
elif userinput < computerguess: 
    print("guess too low")
# catch statement if none of the other conditionals are met. in this case if the two inputs are equal print "YOU GOT IT!" to the console
else:
    print('YOU GOT IT!')
