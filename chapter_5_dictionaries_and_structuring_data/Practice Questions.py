"""1. What does the code for an empty dictionary look like?"""

empty_dict={}

"""2. What does a dictionary value with a key 'foo' and a value 42 look like?"""
full_dict={'foo':'42'}

"""3. What is the main difference between a dictionary and a list?"""
print("Dictionaries have data structured with a specific key, whereas lists use reference position")


"""4. What happens if you try to access spam['foo'] if spam is {'bar': 100}?"""
print("Key error")

"""5. If a dictionary is stored in spam, what is the difference between the expressions 'cat' in spam and 'cat' in spam.keys()?"""
print('cat in spam searches for cat in the keys and values whereas spam.keys searches for cat in the keys')
# Wrong, there is no difference.

"""6. If a dictionary is stored in spam, what is the difference between the expressions 'cat' in spam and 'cat' in spam.values()?"""
print("spam.values searches for cat in the values of the dictionary, whereas cat in spam searches across the key and values.")
#

"""7. What is a shortcut for the following code?

if 'color' not in spam:
    spam['color'] = 'black'"""

spam.setdefault('colour', 'black')

"""8. What module and function can be used to “pretty print” dictionary values? """
pprint module and pprint function.

#pprint.pprint()