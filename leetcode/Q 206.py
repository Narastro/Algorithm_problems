# 2021.02.22. Leetcode algorithm problem #206
# Reverse linked list

class ListNode:
    def __init__(self,x):
        self.val = x
        self.next = None

# using recursive function
def reverseList1(self, head:ListNode) -> ListNode:
    def reverse(node:ListNode, prev: ListNode = None):
        if not node:
            return prev
        next, node.next = node.next, prev
        return reverse (next, node)
    return reverse(head)

# using repeating statement
def reverseList2(self, head:ListNode) -> ListNode:
    node, prev = head, None

    while node:
        next, node.next = node.next, prev
        prev, node = node, next

    return prev