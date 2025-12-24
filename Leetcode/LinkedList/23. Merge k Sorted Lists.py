class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists):
        order = []
        for head in lists:
            curr = head
            while curr:
                order.append(curr.val)
                curr = curr.next

        if not order:
            return None

        order.sort()

        head = ListNode(order[0])
        curr = head

        for i in order[1:]:
            curr.next = ListNode(i)
            curr = curr.next
        return head
