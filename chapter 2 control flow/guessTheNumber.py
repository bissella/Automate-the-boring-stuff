#this is a silly guessing game.

import random
secretNumber = random.randint(1,100)
print("I'm thinking of a number between 1 and 100.")

#ask for secret number 6 times
for guessesTaken in range (1,7,1):
    print('Take a guess.')
    guess = int(input())

    if guess <secretNumber:
        print("too low")
    elif guess >secretNumber:
        print("too high")
    else:
        break #this is the right number or they ran out of guesses.

if guess == secretNumber:
    print ("good job, you guessed the right number in " + str(guessesTaken) +" guesses")
else:
    print ("The number i was thinking of was " + str(secretNumber) +"!")