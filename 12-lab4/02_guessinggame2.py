import random

# First we create a random number between 1 and 1,000
secret  = random.randint(1,1000)
# islying is a random number between 1 and 4
islying = random.randint(1,4)

# And then let the user guess
# Converting the input into int while we read it
# saves it as a number in guess so we can later compare it
guess = int(input("Your guess is...: "))

if guess == secret:
    print("Bingo!")
elif guess < secret:
    # islying has a 25% chance to be 1, and so in 25% 
    # of the games the computer will be lying
    if islying == 1:
        print("Sorry, too small. My number was:", secret)
    else:
        print("Sorry, too large. My number was:", secret)
else:
    if islying == 1:
        print("Sorry, too large. My number was:", secret)
    else:
        print("Sorry, too small. My number was:", secret)

