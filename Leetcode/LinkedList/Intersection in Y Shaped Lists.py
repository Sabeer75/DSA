"""
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

"""


class Solution:
    def intersectPoint(self, head1, head2):
        # code here
        h1, h2 = head1, head2

        while h1 != h2:
            if h1:
                h1 = h1.next
            else:
                h1 = head2

            if h2:
                h2 = h2.next
            else:
                h2 = head1
        return h1
