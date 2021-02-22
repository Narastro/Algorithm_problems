# 2021.02.22. Leetcode algorithm problem #92
# Reverse Linked list 2

class ListNode:
    def __init__(self,x):
        self.val = x
        self.next = None

def reverseBetween(self, head:ListNode, m:int, n:int) -> ListNode:
    # Exception
    if not head or m == n:
        return head
    root = start = ListNode(None)
    root.next = head

    # start, end
    for _ in range(m-1):
        start = start.next
    end = start.next

    # reverse node
    for _ in range(n-m):
        tmp = start.next
        start.next = end.next
        end.next = end.next.next
        start.next.next = tmp
    return root.next