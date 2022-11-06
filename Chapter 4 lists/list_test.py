spam = [0,1,2]
1
# Adding items to lists:
## This causes an error
spam[4] = 4

## This is one way.

spam = spam + [4]

#here is another way
spam.append(69)
## Deleting items
del spam[0]
#here is another
spam.remove("hello")


# Reallocating list items
spam[3] = "Four"

