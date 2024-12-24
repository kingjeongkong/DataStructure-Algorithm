from collections import deque

class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert_level_order(self, arr):
        """Insert nodes in level order from an array"""
        if not arr:
            return
        
        self.root = TreeNode(arr[0])
        queue = deque([self.root])
        i = 1

        while queue and i < len(arr):
            node = queue.popleft()

            if i < len(arr):
                node.left = TreeNode(arr[i])
                queue.append(node.left)
                i += 1

            if i < len(arr):
                node.right = TreeNode(arr[i])
                queue.append(node.right)
                i += 1

    def inorder_traversal(self, node=None):
        """Left -> Root -> Right"""
        if node is None:
            node = self.root

        result = []

        def inorder(node):
            if node:
                inorder(node.left)
                result.append(node.data)
                inorder(node.right)

        inorder(node)
        return result

    def preorder_traversal(self, node=None):
        """Root -> Left -> Right"""
        if node is None:
            node = self.root

        result = []

        def preorder(node):
            if node:
                result.append(node.data)
                preorder(node.left)
                preorder(node.right)

        preorder(node)
        return result

    def postorder_traversal(self, node=None):
        """Left -> Right -> Root"""
        if node is None:
            node = self.root

        result = []

        def postorder(node):
            if node:
                postorder(node.left)
                postorder(node.right)
                result.append(node.data)

        postorder(node)
        return result

    def level_order_traversal(self):
        """Level order traversal"""
        if not self.root:
            return []

        result = []
        queue = deque([self.root])

        while queue:
            level = []
            level_size = len(queue)

            for _ in range(level_size):
                node = queue.popleft()
                level.append(node.data)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            result.append(level)

        return result

    def height(self, node=None):
        """Height of the tree"""
        if node is None:
            node = self.root
            
        def calculate_height(node):
            if not node:
                return -1
            return 1 + max(calculate_height(node.left), calculate_height(node.right))

        return calculate_height(node)

    def size(self, node=None):
        """Calculate number of nodes"""
        if node is None:
            node = self.root

        def calculate_size(node):
            if not node:
                return 0
            return 1 + calculate_size(node.left) + calculate_size(node.right)

        return calculate_size(node)