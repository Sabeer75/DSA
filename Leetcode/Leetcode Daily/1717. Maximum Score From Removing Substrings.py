s = "cdbcbbaaabab"
x = 4
y = 5
op = 0 

if x >= y :
    first_pair , first_point = "ab" , x
    second_pair , second_point = "ba" , y
else:
    first_pair , first_point = "ba" , y
    second_pair , second_point = "ab" , x

stack = []
for i in s:
    if stack and stack[-1] + i == first_pair:
        stack.pop()
        op += first_point
    else:
        stack.append(i)

new_stack = []
for j in stack:
    if new_stack and new_stack[-1] + j == second_pair:
        new_stack.pop()
        op += second_point
    else:
        new_stack.append(j)
print(op)