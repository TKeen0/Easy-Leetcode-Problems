# Definition for a binary tree node.

# You are given the root of a binary tree that consists of exactly 3 nodes:
# the root, its left child, and its right child.
# Return true if the value of the root is equal to the sum of the values of
# its two children, or false otherwise.

# Example 1:
# Input: root = [10,4,6]
# Output: true
# Explanation: The values of the root, its left child, and its right child are 10, 4, and 6, respectively.
# 10 is equal to 4 + 6, so we return true.

# Constraints:
# The tree consists only of the root, its left child, and its right child.
# -100 <= Node.val <= 100


from typing import Optional

class TreeNode:
    def __init__(self, val: int = 0, left: Optional['TreeNode'] = None, right: Optional['TreeNode'] = None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def checkTree(self, root: Optional[TreeNode]) -> bool:
        # Check if root node value equal to sum(two children values)
        return root.val == root.left.val + root.right.val

# Test the solution
if __name__ == "__main__":
    root = TreeNode(10, TreeNode(4), TreeNode(6))
    print(Solution().checkTree(root))  # Output: True