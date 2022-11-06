def spam():
    eggs = 99
    bacon()
    print(eggs)

def bacon():
    eggs = 0

spam()

def spam():
    print(eggs)

eggs = 42

spam()
print(eggs)