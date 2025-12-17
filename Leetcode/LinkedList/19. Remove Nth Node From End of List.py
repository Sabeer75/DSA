class node:
    def __init__(self,val,next = None):
        self.val = val 
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

head = node1
n = 2 

dummy = node(0)
dummy.next = head 
s = f = dummy 

for _ in range(n):
    f = f.next 
while f.next:
    s = s.next 
    f = f.next 

s.next = s.next.next 

while dummy.next:
    print(dummy.next.val,end="-->")
    dummy = dummy.next 
