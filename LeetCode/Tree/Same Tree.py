# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True

        node_p = []
        node_q = []
        
        def preorder(input, node):
            if input:
                node.append(input.val)
                preorder(input.left, node)
                preorder(input.right, node)
            else:
                node.append(None)

        preorder(p, node_p)
        preorder(q, node_q)

        if node_p == node_q:
            return True
        else:
            return False
        
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # Base case 1: Both nodes are None, so they are identical
        if not p and not q:
            return True
        # Base case 2: One node is None or values are different
        if not p or not q or p.val != q.val:
            return False
        # Recursive case: Check left and right subtrees
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

# First solution is what I did, and second solution is from ChatGPT
# When I started this problem, I came up with the recursion to sovle this problem. But I didn't know how to implement it using the isSameTree function.
# So I thought using preorder traversal and saved the tree's values in a list in preorder traversal order could be also compared.
# Second solution's base case 1 is same as mine. And base case 2, I also thought about p.val != q.val up to this point. But also I needed to consider more about only one node is None.
# And for recursion, need to think about perform recursion on left and right subtrees. Both recursion's are true then return true.
