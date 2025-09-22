class Node:
    def __init__(self, key: int):
        self.key = key
        self.next = None

class HashTable:
    def __init__(self, size: int = 10):
        self.size = size
        self.table = [None] * size

    def hash_function(self, key: int):
        return key % self.size

    def insert(self, key: int):
        index = self.hash_function(key)
        new_node = Node(key)
        new_node.next = self.table[index]
        self.table[index] = new_node

    def search(self, key: int):
        index = self.hash_function(key)
        current = self.table[index]
        while current:
            if current.key == key:
                return True
            current = current.next
        return False

    def delete(self, key: int):
        index = self.hash_function(key)
        current = self.table[index]
        prev = None

        while current:
            if current.key == key:
                if prev:
                    prev.next = current.next
                else:
                    self.table[index] = current.next
                return True
            prev = current
            current = current.next

        return False