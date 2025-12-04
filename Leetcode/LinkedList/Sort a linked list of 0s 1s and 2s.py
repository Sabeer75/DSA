class node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


node1 = node(1)
node2 = node(1)
node3 = node(2)
node4 = node(0)
node5 = node(2)
node6 = node(0)
node7 = node(1)
# 15 -- > 14 -- > 13 -- > 9
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = node6
node6.next = node7

head = node1

cnt = [0, 0, 0]
curr = head
while curr:
    if curr.data == 0:
        cnt[0] += 1

    elif curr.data == 1:
        cnt[1] += 1
    else:
        cnt[2] += 1

    curr = curr.next
print(cnt)

curr = head
while curr is not None:
    if cnt[0] != 0:
        curr.data = "0"
        curr = curr.next
        cnt[0] -= 1
    else:
        if cnt[1] != 0:
            curr.data = "1"
            curr = curr.next
            cnt[1] -= 1
        else:
            if cnt[2] != 0:
                curr.data = "2"
                curr = curr.next
                cnt[2] -= 1

curr = head
while curr:
    print(curr.data, end="->")
    curr = curr.next
print("None")
