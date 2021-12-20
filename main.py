# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings .
import random

while True:
    try:
        lower = int(input('Input the lower boundary for the range of numbers to start your guesses:  '))
        higher = int(input('Input the Higher boundary for the range of numbers to end your guesses:  '))

    except ValueError as t:
        print('something went wrong', t)
        continue
    else:
        if lower >= higher:
            print('The lower value is greater than the higher value')
            continue
        print("you've not entered your values correctly")
        break
rand_int = random.randint(lower, higher)
try:
    user_input = int(input(f"Enter a random number within the range of {lower} - {higher}: "))
except ValueError as t:
    print('Input range of numbers', t)
    user_input = int(input(f"Enter a random number within the range of {lower} - {higher}: "))

print(rand_int)

repeat = True
while repeat:

    if rand_int == user_input:
        print('Hurray you guessed right')
        repeat = False

    elif rand_int > user_input:
        print('hmm, you are below the number')
        user_input = int(input("Enter a random number within the range: "))

    elif rand_int < user_input:
        print('You guess is above the score')
        user_input = int(input("Enter a random number within the range: "))
