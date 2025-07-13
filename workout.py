import random 

push_main = ['Inclined w/o smith Bench press 3x 8-12 or 6-8 ', 'Seated Cable/Machine Pec Flye 3x 8-12 ']
push = ['Dips 2x 8-12', 'Smith machine bench press 2x 8-12 or 6-8', 'cable press around 2x 8-12', 'Machine Chest press 2x 8-12']
push_shoulders = ['Cable Lateral Raise 3x 8-15', 'Lean-in DB Lateral Raise 2x 8-15', 'Lateral Raise 3x 8-15', 'Machine Shoulder press or db Overhead press 2x 8-12']
push_triceps = ['Overhead Cable Triceps Extension (Bar) 3x 8-12', 'Barbell Skullcrusher 2x 8-12', 'Triceps Pressdown (Bar)2x 8-12']

First_exercise = random.sample(push, 2)
second_exercise = random.sample(push_shoulders, 2)
third_exercise = random.sample(push_triceps, 2)

complet_push = push_main + First_exercise + second_exercise + third_exercise

back_main = ['Neutral Grip lat pull down 3x 8-12 ', 'Wide Gripe Rows 3x 8-12']
back = ['one arm lat pull down 3x 8-12', 'Wide grip pull ups 3x 8-12', 'Meadows Row 3x 8-12', 'Widegrip lat pull down 2x 8-12']
back_shoulders = ['Reverse Cable Crossover 3-4x 12-15', 'Bent Over Reverse DB flye 3-4x 12-15', 'Rope Facepull 3-4x 12-15']
back_bicep_short = ['Machine Preacher Curl or DB 3x 8-12','Preacher Hammer curl  3x 8-12', ] #Hammer curl are not for short biceps but it's cool for variety becuase i don't isolate brachialis often
back_bicep_long =['EZ bar curl  3x 8-12', 'Face Away Bayesian Curl  3x 8-12', 'Incline Dumbell Curl  3x 8-12'] 

exercise1 = random.sample(back, 2)
exercise2 = random.sample(back_shoulders, 2)
exercise3 = random.sample(back_bicep_short, 1)
exercise4 = random.sample(back_bicep_long, 1)

complete_pull = back_main + exercise1 + exercise2 + exercise3 + exercise4

legs = ['Back Squats 3x 8-12', 'Walking Lunge 3x12 ']
legs_main = ['Leg Extension 3x 8-12', 'Leg Press 3x 8-12', 'Leg Curls 3x 8-12', 'Calf Raises 3x 8-12']
abs = ['Cable Crunches 3x 8-12', 'Machine Crunches 3x 8-12', 'Hanging Leg Raises 3x 8-12']

exercise01 = random.sample(legs, 1)
exercise02 = random.sample(abs, 2)

leg_workout =  exercise01 + exercise02 + legs_main
Lower_complete = leg_workout
####
Upper_body = random.sample(back_shoulders + push_shoulders, 2)
upper_body2 = random.sample(back_bicep_long + back_bicep_short + push_triceps, 2)

Upper_complete = back_main + push_main + Upper_body + upper_body2

choice = input("Which Workout would you like to generate? (Pull/Push/Legs/Upper/Lower): ")

if choice == 'push':
  for exercise_push in complet_push:
    print(exercise_push)
elif choice == 'pull':
 for exercise_pull in complete_pull:
    print(exercise_pull)
elif choice == 'legs':
  for exercise_legs in leg_workout:
    print(exercise_legs)
elif choice =='upper':
  for exercise_upper in Upper_complete:
    print(exercise_upper)
elif choice == 'lower':
  for exercise_lower in Lower_complete:
    print(exercise_lower)
else:
    print("Enter a valid value..")
    exit()