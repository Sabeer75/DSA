class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1, l2):
        val1 = []
        val2 = []

        while l1:
            val1.append(l1.val)
            l1 = l1.next
        while l2:
            val2.append(l2.val)
            l2 = l2.next

        v1 = int("".join(map(str, val1[::-1])))
        v2 = int("".join(map(str, val2[::-1])))

        total = v1 + v2

        head = None
        tail = None

        if total == 0:
            return ListNode(0)

        while total > 0:
            i = total % 10

            total //= 10

            new_node = ListNode(i)

            if head is None:
                head = new_node
                tail = new_node
            else:
                tail.next = new_node
                tail = new_node

        return head
