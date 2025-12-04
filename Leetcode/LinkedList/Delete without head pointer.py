class node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


node1 = node(15)
node2 = node(14)
node3 = node(13)
node4 = node(9)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = None

del_node = node2
head = node1
curr = del_node

curr.data = curr.next.data
curr.next = curr.next.next

cur = head
while cur:
    print(cur.data, end="->")
    cur = cur.next
print("None")
