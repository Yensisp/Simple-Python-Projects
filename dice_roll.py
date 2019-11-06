from random import*

# intro to dice
name = input("Hello what is your name? \n")

# generate a random number (1-6)
repeat = 0
num = randint(1, 6)

while repeat == 0:
    for repeat in range(0, 1):
        print(name + ", the dice rolled: " + (str(num)))
        repeat += 1
        break
