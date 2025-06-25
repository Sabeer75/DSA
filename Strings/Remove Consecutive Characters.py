def removeConsecutiveCharacter(s):
    stack = []
    for i in s:
        if not stack or stack[-1] != i:
            stack.append(i)
    return "".join(stack)


#stack 
s = "aabb"
print(removeConsecutiveCharacter(s))