# 2021.02.26. Leetcode algorithm problem #23
# Merge k Sorted Lists

import heapq

class ListNode:
    def __init__(self,x):
        self.val = x
        self.next = None

def merge_k_lists(lists:list[ListNode])->ListNode:
    root = result = ListNode(None)
    heap = []

    # stor root of each linked list in heap
    for i in range(len(lists)):
        if lists[i]:
            heapq.heappush(heap, lists[i].val, i, lists[i])

    # stor node again after heap extraction
    while heap:
        node = heapq.heappop(heap)
        idx = node[1]
        result.next = node[2]

        result = result.next
        if result.next:
            heapq.heappush(heap, (result.next.val, idx, result.next))

    return root.next
