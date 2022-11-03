print('hello world')

# Random test
lst = [(1, 2), (1, 4), (3, 5), (5, 7)]
price = [item for item in lst if item[0] == 1]
print(price)
for name, price in lst:
    if name == 1:
        price += 1
print(price)
