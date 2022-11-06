cat = ["fuzzy", "gronk"]
while True:
    print("Enter a cat's name.")
    name = input()
    if name not in cat:
            print(name + " is not my cat")
    else:
            print (name +" is my cat.")
    if name == '':
        break