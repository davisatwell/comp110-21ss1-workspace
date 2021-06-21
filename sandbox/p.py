toppings = ["pepperoni", "pineapple", "cheese", "sausage", "olives", "anchovies", "mushrooms"]
prices = [2,6,3,2,7,2]

# i: int = 0
# while i < len(prices):
#     if (prices[i]) != 2:
#         prices.pop(i)
#     i += 1

for elt in prices:
    if (elt != 2):
        prices.pop([elt])

print(prices)