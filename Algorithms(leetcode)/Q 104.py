# 2021.03.08. Leetcode algorithm problem #104
# Maximum Depth of Binary Tree

import collections

def maxDepth(root:TreeNode) -> int:
    if root in None:
        return 0
    queue = collections.deque([root])
    depth = 0

    while queue:
        depth += 1
        for _ in range(len(queue)):
            cur_root = queue.popleft()
            if cur_root.left:
                queue.append(cur_root.left)
            if cur_root.right:
                queue.append(cur_root.right)
    return depth