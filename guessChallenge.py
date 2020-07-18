import random

answer = random.randint(1, 15)
print(answer)

print("Put your number here between 1 and 15: ")
i = float(input())

while i != answer:
    if i < answer:
        print("Please guess higher")
        i = float(input())
        if i == answer:
            break
        #     print("Finally!!!")
        # else:
        #     continue
    elif i > answer:
        print("Please guess lower")
        i = float(input())
        if i == answer:
            break
        #     print("Son of a biTch!! You did it")
        # else:
        #     continue
if i == answer:
    print("You guessed it. It was {}".format(answer))