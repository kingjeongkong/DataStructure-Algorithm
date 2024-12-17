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

    def traverse_forward(self):
        current = self.head
        while current:
            print(current.data, end=" <-> ")
            current = current.next
        print("None")

    def traverse_backward(self):
        current = self.tail
        while current:
            print(current.data, end=" <->")
            current = current.prev
        print("None")

    def search(self, data):
        current = self.head
        while current:
            if current.data == data:
                return True
            current = current.next
        return False

dll = DoublyLinkedList()

dll.insert_at_beginning(3)
dll.insert_at_beginning(2)
dll.insert_at_beginning(1)
dll.insert_at_end(4)
dll.insert_after_node(3, 3.5)

print("Forward traversal:")
dll.traverse_forward()
print("\nBackward traversal:")
dll.traverse_backward()

dll.delete_node(3)
print("\nAfter deleting 3:")
dll.traverse_forward()

print("\nSearching for 2:", dll.search(2))
print("Searching for 3:", dll.search(3))