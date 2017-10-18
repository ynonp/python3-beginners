items = [
    'rice',
    10,
    'apples',
    5,
    'bread',
    15
]

items.append('oranges')
items.append(5)
items.extend(['pineapples', 20])

print("You're buying:")
for name in items[::2]:
    print(name)

total_price = 0
for price in items[1::2]:
    total_price += price

print("You'll pay: {} NIS".format(total_price))

