class node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


node1 = node(15)
node2 = node(14)
node3 = node(15)
node4 = node(9)
# 15 -- > 14 -- > 15 -- > 9
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = None

head = node1

curr = head.next

val = [node1.data]
while curr:
    if curr.data in val:
        curr.data = curr.next.data
        curr.next = curr.next.next

    else:
        val.append(curr.data)
        curr = curr.next

curr = head
while curr:
    print(curr.data, end="->")
    curr = curr.next

print("None")
