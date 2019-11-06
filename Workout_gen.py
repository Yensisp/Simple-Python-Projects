import random
# create arrays to holds training method, upper, lower, and cardio
tr_set = ["5 x 5 for ", "5 x 10 for ", "5 x 20 for "]
tr_rest = ["2 min rest", "1 min rest", "30 sec rest", "no rest"]
up_exlist = ["Bench-Press + ", "Pull-Up + ", "Row + ", "Pushup + ",
             "Shoulder-Press + "]
low_exlist = ["Squat + ", "Deadlift + ", "Lunge + ", "Hip-Thrust + "]
abs_exlist = ["100 crunches", "100 leg-lifts", "60 wind-wipers"]
card_exlist = ["HITT", "20 min run", "20 min bike", "50 burpees"]

# generate random training method, upper, lower, and cardio inputs
sets_reps = random.choice(tr_set)
rest = random.choice(tr_rest)
upper_exercise = random.choice(up_exlist)
lower_exercise = random.choice(low_exlist)
abs = random.choice(abs_exlist)
cardio = random.choice(card_exlist)

# print out the workout
print("Cardio: " + cardio)
print("Upper Body: " + sets_reps + upper_exercise + rest)
print("Lower Body: " + sets_reps + lower_exercise + rest)
print("Abs: " + abs + "\n")
