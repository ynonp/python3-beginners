def calc_price(shoppinglist, pricetable):
    total_price = 0
    for product in shoppinglist:
        total_price += pricetable[product]

    return total_price

items = ['rice', 'rice', 'bread', 'oranges', 'potatoes', 'potatoes']
price = {
    'rice': 10,
    'bread': 15,
    'oranges': 6,
    'potatoes': 20,
}


print("Items = {}; price = {}".format(items, calc_price(items, price)))
