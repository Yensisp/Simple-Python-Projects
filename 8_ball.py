import random
# Create Array to hold answers
answers = ["It is certain", "Reply hazy, try again", "Don't count on it",
           "Most likely", "Ask again later", "My sources say no",
           "Signs point to yes", "Concentrate and ask again", "Very doubtful"]

rand_ans = random.choice(answers)
# Ask user for question
input = input(print("Hello there, please ask the 8-ball a question: \n"))
# return answer to users question
print("8-balls says: "+rand_ans)
