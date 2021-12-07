# 2021.02.22. Leetcode algorithm problem #2
# Add Two Numbers (linked list)

class ListNode:
    def __init__(self,x):
        self.val = x
        self.next = None

def swapPairs(self, head: ListNode) -> ListNode:
    if head and head.next:
        p = head.next
        # return swap value
        head.next = self.swapPairs(p.next)
        p.next = head
        return p
    return head