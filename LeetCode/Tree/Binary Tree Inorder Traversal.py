# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        answer = []

        def inorder(node):
            if node:
                inorder(node.left)
                answer.append(node.val)
                inorder(node.right)

        inorder(root)

        return answer
    

# Inorder Traversal follows the order: left -> root -> right.
# First, check if the root is None (empty tree).
# After that declare the another inorder function to perform recursion.
# The recursion logic:
# - Traverse the left subtree recursively until reaching None (no node).
# - Once None is reached, backtrack and append the current node's value to the answer list.
# - Recursively traverse the right subtree.
# This process ensures all nodes are visited in the correct inorder sequence.