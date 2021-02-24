import pandas as pd

user_boxes = {'weight': [4,2,18,21,14,13],
              'box_name': ['box1','box2', 'box3', 'box4', 'box5', 'box6']
             }

df = pd.DataFrame(user_boxes, columns=['weight', 'box_name'])
df.sort_values(by=['weight'], inplace=True)

print(f'Sorted Values: \n{df}')

#Solution
def open_box_order(user_boxes):
    for i in range(len(user_boxes['weight'])):

        for j in range(len(user_boxes['weight']) - 1):

            if user_boxes['weight'][j] > user_boxes['weight'][j + 1]:
                user_boxes['weight'][j], user_boxes['weight'][j + 1] = user_boxes['weight'][j + 1], \
                                                                       user_boxes['weight'][j]
                user_boxes['box_name'][j], user_boxes['box_name'][j + 1] = user_boxes['box_name'][j + 1], \
                                                                           user_boxes['box_name'][j]

    return print(user_boxes['box_name'])
open_box_order(user_boxes)
