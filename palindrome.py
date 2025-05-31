def palin(s):
    list1 = list(s.lower())
    list2 = []

    for i in list1:
        if i.isalnum():
            list2.append(i)
    if list2 == list2[::-1]:
        return True
    else:
        return False
s='A man, a plan, a canal: Panama'
print(palin(s))





    

