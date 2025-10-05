class node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


node1 = node(15)
node2 = node(14)
node3 = node(13)
node4 = node(9)
# 15 -- > 14 -- > 13 -- > 9
node1.next = node2
node2.next = node3
node3.next = node4

head = node1

curr = head
# reverse the linked list
prev = None

while curr:
    temp = curr.next
    curr.next = prev
    prev = curr
    curr = temp

curr = prev
while curr:
    print(curr.data, end="-->")
    curr = curr.next
