def clearDigits(s):
    stack = []

    for char in s :
        if char.isdigit():
            if stack :
                stack.pop()
        else:
            stack.append(char)
    return ''.join(stack)
        
       
    
s = 'c1be34'
clearDigits(s)