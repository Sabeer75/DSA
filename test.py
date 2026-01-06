gas = [4, 5, 7, 4]
cost = [6, 6, 3, 5]

if sum(gas) < sum(cost):
    print(-1)
start = 0
for start in range(len(gas)):
    if gas[start] > cost[start]:
        j = (start + 1) % len(gas)
        available_gas = 0
        while j != start:
            available_gas = gas[start] - cost[start]
            if available_gas + gas[j] > cost[j]:
                available_gas = available_gas + gas[j] - cost[j]
                j = (j + 1) % len(gas)
            break

        else:
            print(start)
