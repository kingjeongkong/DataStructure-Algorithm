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

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if not self.root:
            self.root = TreeNode(data)
            return
        
        def insert_recursive(node, data):
            if data < node.data:
                if node.left is None:
                    node.left = TreeNode(data)
                else:
                    insert_recursive(node.left, data)
            else:
                if node.right is None:
                    node.right = TreeNode(data)
                else:
                    insert_recursive(node.right, data)

        insert_recursive(self.root, data)

    def search(self, data):
        def search_recursive(node, data):
            if node is None or node.data == data:
                return node

            if data < node.data:
                return search_recursive(node.left, data)
            else:
                return search_recursive(node.right, data)

        return search_recursive(self.root, data)

    def delete(self, data):
        def min_value_node(node):
            current = node
            while current.left:
                current = current.left
            return current

        def delete_recursive(node, data):
            if not node:
                return node

            if data < node.data:
                node.left = delete_recursive(node.left, data)
            elif data > node.data:
                node.right = delete_recursive(node.right, data)
            else:
                # Node with only one child or no child
                if not node.left:
                    return node.right
                elif not node.right:
                    return node.left

                # Node with two children
                temp = min_value_node(node.right)
                node.data = temp.data
                node.right = delete_recursive(node.right, temp.data)
            
            return node

        self.root = delete_recursive(self.root, data)

    def find_min(self):
        if not self.root:
            return None

        current = self.root
        while current.left:
            current = current.left
        return current.data

    def find_max(self):
        if not self.root:
            return None

        current = self.root
        while current.right:
            current = current.right
        return current.data

    def successor(self, data):
        """Find the next larger value"""
        def find_successor(node, data):
            successor = None
            while node:
                if data < node.data:
                    successor = node
                    node = node.left
                elif data > node.data:
                    node = node.right
                else:
                    if node.right:
                        successor = find_min(node.right)
                    break
            
            if successor.data:
                return successor.data
            else:
                return None

        return find_successor(self.root, data)

    def predecessor(self, data):
        """Find the next smaller value"""
        def find_predecessor(node, data):
            predecessor = None
            while node:
                if data > node.data:
                    predecessor = node
                    node = node.right
                elif data < node.data:
                    node = node.left
                else:
                    if node.left:
                        predecessor = find_max(node.left)
                    break
            
            if predecessor.data:
                return predecessor.data
            else:
                return None

        return find_predecessor(self.root, data)
