class Node:
   def __init__(self, data):
       self.data = data
       self.prev = None
       self.next = None

class CircularDoublyLinkedList:
    def __init__(self):
        self.head = None

    def insert_first(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            new_node.next = self.head
            self.head.prev = self.head
        else:
            tail = self.head.prev
            new_node.next = self.head
            new_node.prev = tail
            self.head.prev = new_node
            tail.next = new_node
            self.head = new_node

    def insert_last(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            self.head.next = self.head
            self.head.prev = self.head
        else:
            tail = self.head.prev
            tail.next = new_node
            new_node.prev = tail
            new_node.next = self.head
            self.head.prev = new_node

    def delete_first(self):
        if not self.head:
            print('Empty List') 
            return
        elif self.head.next == self.head:
            self.head = None
        else:
            tail = self.head.prev
            self.head = self.head.next
            self.head.prev = tail
            tail.next = self.head

    def delete_last(self):
        if not self.head:
            print('Empty List')
            return
        elif self.head.next == self.head:
            self.head = None
        else:
            tail = self.head.prev
            new_tail = tail.prev
            new_tail.next = self.head
            self.head.prev = new_tail
            tail = None