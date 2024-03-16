import random

# r = random.randrange(-1, 10) #we wont get 10, it is the upper brakcet
# r = random.randint(-1, 10) # this will include 10
# print(r)

top_of_range = input("Type a number: ")

if top_of_range.isdigit(): # Even though the input is INT, it still return as STRING
    top_of_range = int(top_of_range)

    if top_of_range <= 0:
        print("Please input a number larger than 0 next time.")
        quit()
else:
    print("Please type a number next time")
    quit()


random_number = random.randint(0, top_of_range)
# print(random_number)

guesses = 0

while True:
    guesses += 1
    user_guess = input("Make a guess: ")
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print("Print type a number next time.")
        continue
    if user_guess == random_number:
        print("You got it!")
        break
    elif user_guess > random_number:
        print("You should guess lower number")
    else:
        print("You should guess higher number")

print("You got it in", guesses, "guesses")