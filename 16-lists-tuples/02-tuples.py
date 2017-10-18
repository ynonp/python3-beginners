items = [
    ('rice',10),
    ('apples',5),
    ('bread',15),
]

items.append(('oranges', 5))

print("You're buying:")
for product in items:
    print(product[0])

total_price = 0
for product in items:
    total_price += product[1]

print("You'll pay: {} NIS".format(total_price))

