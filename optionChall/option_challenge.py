answer = "2"
guess = "-"
while guess != answer:
    print("Please choose your option from the list below:")
    print("1.\tLearn Python")
    print("2.\tLearn Java")
    print("3.\tGo swimming")
    print("4.\tHave dinner")
    print("5.\tGo to bed")
    print("0.\tExit")

    guess = str(input())

    if guess == answer:
        print("You guessed it. It was {}".format(guess))
        break
    elif guess == "0":
        print("Bye!!! Bye!!!")
        break
    else:
        print("\tWrong!! Go again")
