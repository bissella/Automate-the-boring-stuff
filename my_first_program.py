#This program says hello and asks for a name and age.

print('Hello, world!')
print('What is your name?')
my_name = input()

print(my_name + 'is a lame name.')
print('what is your age ' + my_name + '?')

my_age = input()

print("You're old. You will be "+ str(int(my_age)+1) + 'in a year.')