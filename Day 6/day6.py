import random
import pandas as pd

random.seed(34)

hole_sizes = [random.randint(1, i) for i in range(1, 101)]
random.shuffle(hole_sizes)

# hole sizes in mm
hole_sizes[:5]

hole_price = []
size = pd.Series(hole_sizes)
# Q1
print(f'The mean average: {size.mean()}')
# for i in range(len(size)):
#     if hole_sizes[i] < 20:
#         hole_price.append(1.30)
#     elif hole_sizes[i] > 20 and hole_sizes[i] < 70:
#         hole_price.append(1.60)
#     elif hole_sizes[i] > 70:
#         hole_price.append(2.10)
# price_series = pd.Series(hole_price)

# print(f'Average is {price_series.mean()}')
# print(f'Total Sum is: {sum(hole_price)}')
print('Stretch\n')
print(f'The largest hole is: {size.max()}')
print(f'The smallest hole is: {size.min()}')
#Solution

count_small = 0
count_medium = 0
count_large = 0

for i in hole_sizes:
    if i < 20:
        count_small += 1
    elif i >= 20 and i < 70:
        count_medium += 1
    else:
        count_large += 1

print(f'The amount of small holes is {count_small}.')
print(f'The amount of small holes is {count_medium}.')
print(f'The amount of small holes is {count_large}.')

# Q2
average_cost = ((count_small*1.3)+(count_medium*1.6)+(count_large*2.1))/ 100
print(f'The average cost is: ${round(average_cost,4)}')

# Q3
total_cost = 0

for i in hole_sizes:
    if i < 20:
        total_cost += 1.3
    elif i >= 20 and i < 70:
        total_cost += 1.6
    else:
        total_cost += 2.1

print(f'The total cost is: {round(total_cost, 4)}')