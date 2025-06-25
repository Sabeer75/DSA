def isValid(s):
    stack = []
    ClosetoOpen = {')':'(','}':'{',']':'['}

    for i in s:
        if i in ClosetoOpen:
            if stack and stack[-1] == ClosetoOpen[i]:
                stack.pop()
            else:
                return False
        else:
            stack.append(i)

    return True if not stack else False
#stack


s = "()[]{}"
print(isValid(s))