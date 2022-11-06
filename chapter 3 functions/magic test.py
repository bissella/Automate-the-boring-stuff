import random

def getAnswer(answerNumber):
    if answerNumber == 1:
           print( 'It is certain')
       elif answerNumber == 2:
           print ('It is decidedly so')
       elif answerNumber == 3:
           print('Yes')

r = random.randint(1, 3)
fortune = getAnswer(r)
print(fortune)
print.__code__.co_varnames
