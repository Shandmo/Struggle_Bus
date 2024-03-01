#####################################################
def workout_total():
    exercises = []
    totals = []
    print("How many different exercises today?")        #How many exercises did the user do?
    MAX_LENGTH_LIST = int(input())
    print("What exercises did you do?")
    while len(exercises) != MAX_LENGTH_LIST:        #What were the exercises?
        movement = input()
        exercises.append(movement)
    
    #Get sets, reps, and weight for each exercise.
    for exercise in exercises:
        print("How many sets did you do for {}?".format(exercise.title()))
        sets = int(input())
        print("How many repetitions?")
        reps = int(input())
        print("How much weight?")
        weight = int(input())
        exer_total = (reps * weight) * sets      #Get the total for that exercise, add it to an overall total
        totals.append(exer_total)
        total = sum(totals)
        print("You moved {}lbs during {}.".format(exer_total, exercise.title()))
        if exercise != exercises[0]:
            print("You moved {}lbs total.".format(total))

workout_total()
