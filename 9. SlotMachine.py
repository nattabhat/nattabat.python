import random


MAX_LINES = 3 #this reminds us that this value must be the same
MAX_BET = 100
MIN_BET = 1

ROWS = 3
COLS = 3

symbol_count = {
    "A": 2,                  #"A" is the most valuable symbol in each reel, each reel only have two of them
    "B": 4,
    "C": 6,
    "D": 8
}

symbol_value = {
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2
}

def check_winnings(columns, lines, bet, values):
    winnings = 0
    winnings_lines = []
    for line in range(lines):
        symbol = columns[0][line] #the value of the first column in the current row
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break #user do not win
        else:
            winnings += values[symbol] * bet
            winnings_lines.append(lines)

    return winnings, winnings_lines

def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []
    #     "A"         2
    for symbol, symbol_count in symbols.items(): #by using item, it provide both key and its value at the same time
        for _ in range(symbol_count): #using _ when we don't care about the count or value when looping
            all_symbols.append(symbol) #this will add that symbol in times base on symbols_count

    columns = []
    for _ in range(cols):
        column = []
        current_symbol = all_symbols[:] # [:] makes all_symbols just a copy, changes in original all_symbols won't affect current_symbol/ any change in current_symbol won't affect original all_symbols
        for _ in range(rows):
            value = random.choice(current_symbol) #when choose a symbol it will be permanently removed from all_symbols
            current_symbol.remove(value) #remove picked value
            column.append(value) #add the chosen value to the column

        columns.append(column) # add the column to the columns list

    return columns

# right now what we have in columns list is in a form of row, we have to turn it into column for slot machine's reel
#    [A, B , C]            [A] [B]
#    [B, A , A]  -->       [B] [A]
#                          [C] [A]

def print_slot_machine(columns):
    for row in range(len(columns[0])): #loop for every single row
        for i, column in enumerate(columns): #in every single row, we loop through each column
            if i != len(columns) - 1: #this is the upper index of columns list
                print(column[row], end=" | ")
            else:
                print(column[row], end=" ")

        print() #make a new line, like enter


def deposit():
    while True: #make user input the right deposit amount
        amount = input("What would you like to deposit? $")
        if amount.isdigit(): #check if the input string is digit or not
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Amount must be greater than 0.")
        else:
            print("Please enter a number")

    return amount

def get_number_of_lines():
    while True:
        lines = input("Enter the number of lines to bet on (1-" + str(MAX_LINES) + ")? ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("Enter a valid number of lines")
        else:
            print("Please enter a number")

    return lines

def get_bet():
    while True:
        amount = input("What would you like to bet on each line? $")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(f"Amount must be between ${MAX_BET} - ${MAX_BET}.") #this is just a fancy way of turning INT to STRING
        else:
            print("Please enter a number")

    return  amount

def spin(balance):
    lines = get_number_of_lines()
    # checking if the amount of bet is inside the amount of user's deposit
    while True:
        bet = get_bet()
        total_bet = bet * lines

        if total_bet > balance:
            print(f"You do not have enough money in your account, your current balance is: ${balance}")
        else:
            break

    print(f"you are betting ${bet} on {lines} lines. Total bet is equal to: ${total_bet}")

    slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
    print_slot_machine(slots)
    winnings, winning_lines = check_winnings(slots, lines, bet, symbol_value)
    print(f"You won ${winnings}.")
    print(f"You won on lines:", *winning_lines)  # it will pass every line from winning_line
    return winnings - total_bet


def main():
    balance = deposit()
    while True:
        print(f"Current balance is ${balance}")
        answer = input("Press enter to play (q to quit). ")
        if answer == "q":
            break
        balance += spin(balance)

    print(f"You left with ${balance}")

main()