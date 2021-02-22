# 2021.02.22. Leetcode algorithm problem #234
# Palindrome Linked list

class ListNode:
    def __init__(self,x):
        self.val = x
        self.next = None



def isPalindrome1(head:ListNode) -> bool:
    q : list = []

    if not head:
        return True

    node = head
    # convert to list
    while node is not None:
        q.append(node.val)
        node = node.next

    # determine palindrome
    while len(q) > 1:
        if q.pop(0) != q.pop():
            return False
    return True

def isPalindrome2(head:ListNode) -> bool:
    rev = None
    slow = fast = head
    # configure reverse linked list using runner
    while fast and fast.next:
        fast = fast.next.next
        rev, rev.next, slow = slow, rev, slow.next
    if fast:
        slow = slow.next

    # check if it is palindrome
    while rev and rev.val == slow.val:
        slow, rev = slow.next, rev.next
    return not rev

