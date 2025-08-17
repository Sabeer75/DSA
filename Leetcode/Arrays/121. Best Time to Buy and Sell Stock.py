prices = [7, 6, 4, 3, 9]
min_price = float("inf")
profit = 0
for i in prices:
    if i < min_price:
        min_price = i
    else:
        profit = max(profit, i - min_price)
print(profit)
