# 2021.04.16. leetcode algorithm problem #42
# Diameter of Binary Tree

class solution:
    longest : int  = 0

    def diameter_binary_tree(self, root:TreeNode) -> int:
        def dfs(node : TreeNode) -> int:
            if not node:
                return -1
            left = dfs(node.left)
            right = dfs(node.right)

            self.longest = max(self.longest, left+right+2)
            return max(left,right)+1

        dfs(root)
        return self.longest
