
#def delist(spam):
"""This function takes a list, extracts each individual value and prints an output with " ," seperating each item except
for the last list item that has " and"

        Thinking...
            1) Create a for loop that goes through each item in the list and adds " ," between each item.
            2) insert and at the second to last item (-2)
            3) Eport the list as

    Option 2)
    Create there are limited number of list outcomes:
        1) list is empty
        2) List has one thing
        3) List has 2 things (and)
        4) List has more than two things ( ", " " and ")

        Create an elif tree that works through the different combinations.
            """


def list_to_string(spam):
    comma = ", "
    if len(spam) == 0:
        return "The list is empty."
    elif len(spam) == 1:
        return spam[0]
    elif len(spam) == 2:
        return spam[0] + " and " + spam[1]
    elif len(spam) > 2:
        return comma.join(spam[:-1])+" and "+spam[-1]
