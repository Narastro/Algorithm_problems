# 2021.02.26. Leetcode algorithm problem #706
# Design HashMap

import collections

class ListNode:
    def __init__(self, key=None, value=None):
        self.value = key
        self.value = value
        self.next = None

class My_HashMap:
    # initialization
    def __init__(self):
        self.size = 1000
        self.table = collections.defaultdict(ListNode)

    # inserting
    def put(self, key:int, value:int)->None:
        index = key % self.size
        # End after implementation if no nodd in index
        if self.table[index].value is None:
            self.table[index] = ListNode(key, value)
            return

        # linked list if there is index in node
        p = self.table[index]
        while p:
            if p.key == key:
                p.value = value
                return
            if p.next is None:
                break
            p = p.next
        p.next = ListNode(key, value)

    # checking
    def get(self, key:int)->int:
        index = key % self.size
        if self.table[index].value is None:
            return -1

        # searching matching keys if there is the node
        p = self. table[index]
        while p:
            if p.key == key:
                return p.value
            p = p.next
        return -1

    #removing
    def remove(self, key:int)->None:
        index = key % self.size
        if self.table[index].value is None:
            return

        # remove if it is first node
        p = self.table[index]
        if p.key == key:
            self.table[index] = ListNode() if p.next is None else p.next
            return

        # removing linked-list's node
        prev = p
        while p:
            if p.key == key:
                prev.next = p.next
                return
            prev, p = p, p.next