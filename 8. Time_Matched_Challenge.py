import random
import time

OPERATORS = ["+", "-",  "*"]
MIN_OPERAND = 3
MAX_OPERAND = 12
TOTAL_PROBLEM = 10

def generate_problem():
    left = random.randint(MIN_OPERAND, MAX_OPERAND)
    right = random.randint(MIN_OPERAND, MAX_OPERAND)
    operator = random.choice(OPERATORS) #randomly pick one element from a list

    expr = str(left) + " " + operator + " " + str(right)
    answer = eval(expr) #it will tell the result of expr
    return expr, answer #match1

wrong = 0
guess_num = 0
input("Press enter to start! ")
print("----------------------")

start_time = time.time()

for i in range(TOTAL_PROBLEM):
    expr, answer = generate_problem() #match1
    while True:
        guess = input("Problem #" + str(i + 1) + ": " + expr + " = ")
        guess_num += 1
        if guess == str(answer):
            break
        wrong += 1

end_time = time.time()
total_time = round(end_time - start_time, 2)

print("----------------------")
print("Nice work! You finished in", total_time, "seconds! You have", guess_num/(wrong + guess_num), "accuracy")