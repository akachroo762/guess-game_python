import random

answer = random.randint(1, 15)
print(answer)

print("Put your number here between 1 and 15: ")
i = 0
while i != answer:
    i = float(input())
    if i == 0:
        print("Bye Bye !!!")
        break
    elif i == answer:
        print("You guessed it. It was {}".format(answer))
        break
    else:
        if i < answer:
            print("Please guess higher")
        else:
            print("Please guess lower")
