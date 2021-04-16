# 2021.04.16. Leetcode algorithm problem #687
# Longest Univalue Path

class solution:
    result : int = 0

    def longest_path(self, root) -> int:
        def dfs(node):
            if node is None:
                return 0

            left = dfs(node.left)
            right = dfs(node.right)

            if node.left and node.left.val = node.val:
                left += 1
            else: left = 0

            if node.right and node.right.val = node.val:
                right += 1
            else:
                right = 0

            self.result = max(self.result,left+right)
            return max(left,right)

        dfs(root)
        return self.result
            
