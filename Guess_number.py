from random import*

# generate a random number and attempts
rand_num = randint(1, 10)
attempts = 0
trys = 3

# Ask user for number guess
# create a loop that only allows 3 guess
# create an if statemtent for correct answer (higher/lower than)
while attempts < 3:
    guess_num = int(input("Guess a number between 1 and 10, you have "+ str(trys)+
                          " trys.\nGuess: "))

    attempts += 1
    trys -= 1

    if guess_num < rand_num:
        print("Your guess is too low\n")
    elif guess_num > rand_num:
        print("Your guess is too high\n")
    else:
        break

if guess_num == rand_num:
    print("You guessed the correct number!\n")
