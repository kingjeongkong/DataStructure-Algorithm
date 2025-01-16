# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        def calculate_depth(node, depth):
            if not node:
                return depth - 1

            if not node.left and not node.right:
                return depth

            return max(calculate_depth(node.left, depth + 1), calculate_depth(node.right, depth + 1))

        return calculate_depth(root, 1)

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # Base case: If the tree is empty, its depth is 0
        if not root:
            return 0

        # Recursive calls to calculate the depth of left and right subtrees
        left_depth = self.maxDepth(root.left)
        right_depth = self.maxDepth(root.right)

        # Combine the results: Depth of the current tree is 1 + maximum depth of subtrees
        return max(left_depth, right_depth) + 1
