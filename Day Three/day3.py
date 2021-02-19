'''Dot has some specific rules for what they want to change in the shopping list:
They hate oak wood, and prefer maple.
They want to paint all the rooms blue except the kitchen, which they want to paint white.'''

'''Use python's pop(), insert(), and append() list functions to change the shopping_list above so that it reflects the right materials needed.
The list should be ordered by wood types first, then paint types.

example_shopping_list = ['wood type in room A', 'wood type in room b','paint type in room a','paint type in room b']
Create a paint_list list from the new_shopping_list list using the built in python list indexing ability.
'''

shopping_list = ['20 x Oak plank', '20 x Oak Plank', '20 x Cherry Plank', 'White Paint', 'White Paint', 'White Paint']
new_shopping_list = shopping_list
print(new_shopping_list)
new_shopping_list.pop(-1)
print(new_shopping_list)
new_shopping_list.pop(-1)
print(new_shopping_list)
new_shopping_list.append('Blue Paint')
new_shopping_list.extend(['Blue Paint','Blue Paint','Blue Paint','Blue Paint',])
print(new_shopping_list)
new_shopping_list.pop(0)
new_shopping_list.insert(0, "20 x Maple Plank")
print(new_shopping_list)
new_shopping_list.pop(1)
new_shopping_list.insert(1, "20 x Maple Plank")
print(new_shopping_list)

# Solution
paint_list = new_shopping_list[3:]
print(paint_list)