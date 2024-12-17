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

    def delete_node(self, data):
        if not self.head:
            print('List is empty')
            return

        current = self.head

        # If head node itself holds the data to be deleted
        if current.data == data:
            if current.next:
                self.head = current.next
                self.head.prev = None
            else:
                self.head = None
                self.tail = None
            return

        while current and current.data != data:
            current = current.next

        if not current:
            print(f"Node with data {data} not found.")
            return
        
        # If node to be deleted is tail
        if current == self.tail:
            self.tail = current.prev
            self.tail.next = None
            return

        # If node to be deleted is middle node
        current.prev.next = current.next
        current.next.prev = current.prev

    def delete_at_position(self, position):
        if not self.head:
            print("List is empty")
            return

        if position == 0:
            if self.head.next:
                self.head = self.head.next
                self.head.prev = None
            else:
                self.head = None
                self.tail = None
            return

        current = self.head 
        for i in range(position):
            if not current:
                print("Position is out of bounds.")
                return
            current = current.next

        if not current:
            print("Position is out of bounds after the loop.")
            return

        if current == self.tail:
            self.tail = current.prev
            self.tail.prev = None
            return

        current.prev.next = current.next
        current.next.prev = current.prev