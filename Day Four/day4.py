item_list = ['Oak Wood', 'Blue Paint', 'White Paint', 'Paint Finish']
amount_list = [600,150,15,165]
# compare with wholesale price vs retail price
wholesale_price_list = [7000, 1000, 1000, 800]
retail_price = [12.99, 8.99, 9.99, 3.99]

retail_price_list = retail_price

for i in range(len(retail_price_list)):
    retail_price_list[i] = retail_price_list[i] * amount_list[i]

print(f"This is the retail price list multiply the amount list: {retail_price_list}")

price_diff = len(retail_price_list) * [0]
new_item_list = []
for i in range(len(price_diff)):
    price_diff[i] = retail_price_list[i] - wholesale_price_list[i]
    for item in item_list:
        new_item_list.append(item)
        if price_diff[i] < 0:
            new_item_list.append("Buy Retail Price")
        else:
            new_item_list.append("Buy Wholesale Price")
        break

print(price_diff)
print(new_item_list)
# if positive, that means this is higher than the wholesale price - buy wholesale
# if negative, that means this is lower than the wholesale price - buy retail

retail_price2 = [12.99, 8.99, 9.99, 3.99]
amount_list2 = [600,150,15,165]


full_price = [] #Create an empty list

for i in range(len(item_list)):

    total_price = amount_list2[i] * retail_price2[i] #Store the total price for each item
    full_price.append(total_price)
print(full_price)