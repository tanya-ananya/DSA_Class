'''
Data Structures Lab 2
Date: January 22
Author: Taaruni Ananya
'''

class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def reverse_list(self):
        prev = None
        current = self.head
        while current is not None:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev
        return self.head
    
    def find_middle(self):
        if self.head is None or self.head.next is None:
            return None
        slow = fast = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow.value
    
    def insert_at_beginning(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node
        return self.head

    def insert_at_end(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node
        return self.head

    def insert_at_middle(self, value):
        if not self.head or not self.head.next:
            self.insert_at_beginning(value)
            return
        slow = fast = self.head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        new_node = Node(value)
        new_node.next = slow.next
        slow.next = new_node
        return self.head

    def remove_by_value(self, val):
        if self.head is None:
            return self.head
        current = self.head.next
        previous = self.head
        while current:
            if current.value == val:
                previous.next = current.next
                return self.head
            previous = current
            current = current.next
        return self.head
    
    def search_for_value(self, value):
        current = self.head
        position = 0
        found = False
        while current:
            if current.value == value:
                print(f"Value {value} can be found at position {position}")
                found = True
            current = current.next
            position += 1
        if found == False:
            print(f"Value {value} can't found in the list.")

def print_list(linked):
    current = linked.head
    lst = []
    while current:
        lst.append(current.value)
        current = current.next
    print(' --> '.join(map(str, lst)))

# Testing
test = SinglyLinkedList()

test.insert_at_beginning(3)
print()
print('Insert value at beginning')
print_list(test)

test.insert_at_end(4)
print()
print('Insert value at end')
print_list(test)

test.insert_at_middle(5)
print()
print('Insert value at middle')
print_list(test)

test.insert_at_end(6)
test.insert_at_end(7)
test.insert_at_end(8)
test.insert_at_end(9)
test.insert_at_end(10)
test.insert_at_end(11)

test.remove_by_value(9)
print()
print('Remove value')
print_list(test)

print()
print('Search for value')
test.search_for_value(6)

test.reverse_list()
print()
print('Reverse')
print_list(test)

print()
print('Find middle')
print(f'{test.find_middle()}')

print()
print()
print()
print()