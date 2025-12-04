class node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


node1 = node(3)
node2 = node(2)

node3 = node(0)
node4 = node(2)

node1.next = node2
node2.next = None
first = node1

node3.next = node4
node4.next = None
second = node3

modu = 10**9 + 7
num1 = 0
num2 = 0

while first:
    num1 = (num1 * 10 + first.data) % modu
    first = first.next

while second:
    num2 = (num2 * 10 + second.data) % modu
    second = second.next

print((num1 * num2) % modu)
