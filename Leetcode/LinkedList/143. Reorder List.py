class node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


node1 = node(1)
node2 = node(2)
node3 = node(3)
node4 = node(4)
node5 = node(5)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = None 

head = node1

s , f = head , head.next

while f and f.next:
    s = s.next 
    f = f.next.next

second = s.next
s.next = prev = None 

while second:
    temp = second.next 
    second.next = prev 
    prev = second 
    second = temp 
        
first , second = head , prev 
while second:
    temp1 , temp2 = first.next , second.next 
    first.next = second 
    second.next = temp1 
    first , second = temp1 , temp2 

curr = head 

while curr:
    print(curr.data,end = "-->")
    curr = curr.next 

