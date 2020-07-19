import random

highest = 1500
answer = random.randint(1, highest)
print(answer)

print("Put your number here between 1 and {}: ".format(highest))

# Initial value of i
i = 0
# Loop starts
while i != answer:
    i = float(input())      # enter value of i here

    if i == 0:              # break the loop by pressing 0 and it will exit you out of the game
        print("Bye Bye !!!")
        break
    elif i == answer: # Guess the right answer to break the loop
        print("You guessed it. It was {}".format(answer))
        break
    else: # if the above conditions don't satisfy then the loop keeps running until you press 0 and exit or guess the right answer
        if i < answer:
            print("Please guess higher")
        else:
            print("Please guess lower")
