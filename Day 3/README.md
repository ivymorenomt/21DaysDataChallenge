### Day Three: lists, dictionaries, and indexing
Dot's new rural abode is in a bit of disrepair. It desperately needs some care before it can be the cozy hide-away they've been dreaming of. The paint on the walls is dull and peeling, and some of the floorboards have rotted away.

The previous occupants were beginning to tackle the repairs before they moved out. They left Dot a shopping list for what's needed to complete the repairs. However, Dot is really particular with how they want the place to look. They want to change the shopping list so that it reflects the changes they want to make to the house.

Brief Tutorial
#### Indexing or Slicing Lists

In the previous challenge we introduced you to lists. Lists are Python data structures that can hold many types of data in a sequence. The act of calling specific data in a list based on their position within the list is referred to as indexing or slicing.

list_of_int = [1,2,3,4,5] # list of integers
list_of_string = ['string1','string2', 'string3'] # list of strings
list_of_anything = [1, 'string', 3.2] # list with an integer, string, and float.

list_of_string[0] # will print out 'string1'

list_of_int[0:2] # will print out [1,2,3]
To read more on list indexing and slicing, read this article

Note: Python is a zero-based indexing language, meaning that first element of a sequence will be at index = 0.

#### Appending and Replacing Values in Lists

Python lists are mutable structures, meaning a list's size or values can be changed. Below are some of the common methods of changing values in a list.

To learn more about the various Python list methods, read this article

list_of_int = [1 , 2 , 3 , 4 ,5] # list of integers

list_of_int.append('value') # Running this line of code will update list_of_int = [1,2,3,4,5, 'value']

list_of_int.insert(3 , 3.5) # Insert 3.5 in index 3, resulting in list_of_int = [1,2,3,3.5,4,5]

list_of_int.pop(0) # Removes the value in position 0, list_of_int = [2,3,4,5]
Python Dictionary

In addition to lists, Python has another data structure called dictionary, which is similar to that of a list. However, the difference is lists are ordered sets of objects, but dictionaries are unordered sets of objects, and the items in dictionaries are accessed by keys. Each key may contain a list that can be accessed and normally indexed like a list. See the example below. To learn more about python dictionary, read this article.

dictionary = {
    "key": ["value_1","value_2"]
    "key_2":[1,2]
    "key_3":[1,2,'value_3']
}
### Challenge
Dot has some specific rules for what they want to change in the shopping list:

They hate oak wood, and prefer maple.
They want to paint all the rooms blue except the kitchen, which they want to paint white.

old_blueprint = {
    "Kitchen": ['Dirty', 'Oak', "Damaged", "Green"],
    "Dining Room": ['Dirty', 'Pine', 'Good Condition', 'Grey'],
    "Living Room": ['Dirty', 'Oak', 'Damaged', 'Red'],
    "Bedroom" : ["Clean", 'Mahogany', 'Good Condition', 'Green'],
    "Bathroom": ["Dirty", 'White Tile', 'Good Condition','White'],
    "Shed"    : ['Dirty', "Cherry", "Damaged", "Un-painted"]
}

shopping_list = ['20 x Oak Plank', '20 x Oak Plank', '20 x Cherry Plank', 'White Paint', 'White Paint', 'White Paint']

Note: The blueprint above is in a dictionary format and we won't be needing to work with dictionaries in the challenge, use the blueprint as reference only.

Use python's pop(), insert(), and append() list functions to change the shopping_list above so that it reflects the right materials needed.

The list should be ordered by wood types first, then paint types.

example_shopping_list = ['wood type in room A', 'wood type in room b','paint type in room a','paint type in room b']

Create a paint_list list from the new_shopping_list list using the built in python list indexing ability.