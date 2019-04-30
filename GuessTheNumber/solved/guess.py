import random

computerguess = random.randint(1, 10)

userinput = int(input())

if userinput > computerguess:
    print("guess too high")
elif userinput < computerguess: 
    print("guess too low")
else:
    print('YOU GOT IT!')
