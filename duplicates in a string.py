def duplicate(s):
    list1 = list(s)
    list1.sort()
    dict = {}
    count = 1
    print(list1)
    for i in range(len(list1)):
        if i <len(list1)-1 and list1[i] == list1[i+1] :
            count += 1
        else:
            dict[list1[i]] = count
            count = 1
    print(dict)
    for j in dict:
        if dict[j]>1:
            print(j,dict[j])
s = 'geeksforgeeks'
print(duplicate(s))


