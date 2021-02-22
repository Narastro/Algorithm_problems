# 2021.02.22. Leetcode algorithm problem #21
# Merge Two sorted Lists

class ListNode:
    def __init__(self,x):
        self.val = x
        self.next = None

def mergeTwoLists(self, l1:ListNode, l2:ListNode) -> ListNode:
    if (not l1) or (l2 and l1.val > l2.val):
        # swap
        l1, l2 = l2, l1
    if l1:
        # recursive function
        l1.next = self.mergeTwoLists(l1.next, l2)
    return l1