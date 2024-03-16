import random

def roll():
    min_value = 1
    max_value = 6
    dice_roll = random.randint(min_value, max_value)

    return dice_roll

while True:
    players = input("Enter the number of players (2 -4):")
    if players.isdigit():
        players = int(players)
        if 2 <= players <= 4:
            break
        else:
            print("Must ge between 2 - 4 players")
    else:
        print("Invalid, try again.")

max_score = 50
player_scores = [0 for i in range(players)]
# let's say 2 players, it will contain 0 for both like [0,0]

while max(player_scores) < max_score: #Loop1
    for player_idx in range(players):
        print("\nPlayer", player_idx + 1, "turn has just started!") #range function does not include the upper number, that's why player_idx needed + 1
        print("Your total score is:", player_scores[player_idx], "\n")
        current_score = 0

        while True: #Loop2 return current score
            should_roll = input("would you like to roll (y)? ")
            if should_roll.lower() != "y":
                break #break from Loop2. If 'y', it will pass down

            value = roll()  #use the roll() function
            if value == 1:
                print("You rolled a 1! Turn done!")
                break #break from Loop2
            else:
                current_score += value
                print("You rolled a:", value)
            if current_score < max_score:
                print("Your score is:", current_score)
            else:
                break

        player_scores[player_idx] += current_score
        print("Your total score is: ", player_scores[player_idx])


max_score = max(player_scores)
winning_idx = player_scores.index(max_score)
print("Player number", winning_idx + 1, "is the winner with a score of", max_score)

