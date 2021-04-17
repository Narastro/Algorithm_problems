# 2021.04.17. leetcode algorithm problem #108
# Convert Sorted Array to Binary Search Tree

def sorted_array_BST(nums):
    if not nums:
        return None
    
    mid = len(nums)//2

    # Using the divisional conquest
    node = TreeNode(nums[mid])
    node.left = sorted_array_BST(nums[:mid])
    node.right = sorted_array_BST(nums[mid+1:])

    return node
