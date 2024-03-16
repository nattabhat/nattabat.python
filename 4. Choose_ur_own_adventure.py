name = input("Type your name: ")
print("Welcome", name, "to this adventure!")

while True:
    print('If you want to quit, type quit')
    answer = input("The path is blocked, you can go left or right, which way? ").lower()

    if answer == "left":
        answer = input("There's a river in front of you, walk around or swim? ").lower()

        if answer == "swim":
            print("You got ate by an aligator.Try again")
            continue
        elif answer == "walk":
            print("You walked so long, you passed way. Try again")
            continue
        else:
            print('Not a valid option. You lose. Try again')
            continue

    elif answer == "right":
        answer = input("You found a treasure, open or walk away ").lower()

        if answer == "open":
            print("There is a bomb inside, you were blown away. Try agian")
            continue
        elif answer == "walk away":
            answer = input("you found a diamond, pick it up or not (yes/no) ").lower()
            if answer == "yes":
                print("You won!!!!")
                break
            elif answer == "no":
                print("You got hit by an meteo")
            else:
                print('Not a valid option. You lose. Try again')
                continue
        else:
            print('Not a valid option. You lose. Try again')
            continue
    elif answer == "quit":
        break
    else:
        print('Not a valid option. You lose. Try again')
        continue