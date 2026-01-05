s = "((a+b))+(c+d)"

stack = []
dup = False
for i in s:
    if i == ")":
        inside = 0

        while stack and stack[-1] != "(":
            stack.pop()
            inside += 1

        stack.pop()

        if inside == 0:
            dup = True
            break

    else:
        stack.append(i)


if dup:
    print("duplicate present")

else:
    print("no duplicates")
