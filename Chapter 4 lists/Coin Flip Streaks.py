"""
BRIEF:
For this exercise, we’ll try doing an experiment. If you flip a coin 100 times and write down an “H” for each heads and
 “T” for each tails, you’ll create a list that looks like “T T T T H H H H T T.” If you ask a human to make up 100
 random coin flips, you’ll probably end up with alternating head-tail results like “H T H T H H T H T T,” which looks
 random (to humans), but isn’t mathematically random. A human will almost never write down a streak of six heads or six
 tails in a row, even though it is highly likely to happen in truly random coin flips. Humans are predictably bad at
 being random.

Write a program to find out how often a streak of six heads or a streak of six tails comes up in a randomly generated
list of heads and tails. Your program breaks up the experiment into two parts: the first part generates a list of
randomly selected 'heads' and 'tails' values, and the second part checks if there is a streak in it. Put all of this
code in a loop that repeats the experiment 10,000 times so we can find out what percentage of the coin flips contains a
streak of six heads or tails in a row. As a hint, the function call random.randint(0, 1) will return a 0 value 50% of
the time and a 1 value the other 50% of the time.
"""

import random

numberOfStreaks = 0
checkerList = []
#Code that creates a list of 100 'heads' or 'tails' values.
HTlist = []
for i in range(10000):
    HTlist.append(random.randint(0, 1))
    if HTlist[i] == 0:
        HTlist[i] = 'H'
    else:
        HTlist[i] = 'T'

# Code that checks if there is a streak of 6 heads or tails in a row.

numberOfStreaks = 0
for i in range(len(HTlist)):

    if len(checkerList) == 0:
        checkerList.append(HTlist[i])# Appends the latest item in the HTlist to the checker list if empty
    elif checkerList[-1] == HTlist[i]:# If the last item in checkerList matches i, it appends it to checkerList.
        checkerList.append(HTlist[i])

        if len(checkerList) == 6:
            numberOfStreaks = numberOfStreaks + 1
            checkerList = []# resets the counter
    else:
        checkerList = []
        checkerList.append(HTlist[i])

"""
For loop that goes through the HTlist.
count = 0
Create a separate list (checker) initiated by the first element of the HTlist i.e 
checkerList = HTlist[0]

for i along HTlist[1,99]
    if i == checkerList[i]:
        append i to checkerList.
        if len(checkerlist) == 6:
        numberOfStreaks = numberOfStreaks +1
        checkerList = 0    
    else:
    checkerlist = checkerlist[i]
    
If the I along list [1:99] is the same as new_list(i) then add append to new_list.
else, rewrite list [1]
"""



# print('Chance of streak: %s%%' % (numberOfStreaks /100))
