# intro to calc
print("Select an operator from below:\n")

# enter operator
operator = int(input("1 = Additon(+)\n"
                     "2 = Subtraction(-)\n"
                     "3 = Multiplication(*)\n"
                     "4 = Division(/)\n"))

# enter  two numbers
num1 = int(input("First number:\n"))
num2 = int(input("Second number:\n"))

# do the math and return answer
if operator == 1:
    print("Answer: " + str(num1+num2))
elif operator == 2:
    print("Answer: " + str(num1-num2))
elif operator == 3:
    print("Answer: " + str(num1*num2))
elif operator == 4:
    print("Answer: " + str(num1/num2))
else:
    print("Sorry try and re-run the program")
