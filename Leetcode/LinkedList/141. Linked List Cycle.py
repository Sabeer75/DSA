class node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


node1 = node(1)
node2 = node(2)
node3 = node(3)
node4 = node(4)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node2

head = node1
curr = head

visited = set()

is_cycle = False

while curr:
    if curr in visited:
        is_cycle = True
        break
    visited.add(curr)
    curr = curr.next

if is_cycle:
    print(True)
else:
    print(False)
