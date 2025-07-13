n,m = map(int , input().split())

total_making_cost = n * 30 
total_selling_cost = m * 50 

profit_or_loss = total_selling_cost - total_making_cost

print(profit_or_loss)