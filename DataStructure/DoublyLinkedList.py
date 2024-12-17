class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_at_beginning(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            self.head.prev = new_node
            new_node.next = self.head
            self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

    def insert_after_node(self, prev_node_data, data):
        if not self.head:
            print('List is empty')
            return

        current = self.head
        while current and current.data != prev_node_data:
            current = current.next

        if not current:
            print(f"Node with data {prev_node_data} not found.")
            return

        new_node = Node(data)
        new_node.next = current.next
        new_node.prev = current

        if current.next:
            current.next.prev = new_node
        else:
            self.tail = new_node

        current.next = new_node