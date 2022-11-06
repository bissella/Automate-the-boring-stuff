#infinite loop

while True:
   print("who are you?")
   name = input()
    if name != 'Joe':
        continue
    print("Hello Joe. Password?")
    password = input()
    if password == 'swordfish':
        break
print ('access granted')