import random
min_number = 1
max_number = 100
max_attempts = 10
result = random.randint(min_number,max_number)
for i in range(max_attempts):
    guess = int(input("Enter your number: "))
    if guess < result:
        print("Too low!")
    elif guess > result:
        print("Too high!")
    else:
        print("Congratulations, your guess is correct")
        break 


