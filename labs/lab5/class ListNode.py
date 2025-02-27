class ListNode:
    def __init__(self, data: any) -> None:
        self.data = data
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self) -> None:
        self.head = None
        self.tail = None

    def insert_first(self, value: any) -> None:
        new_node = ListNode(value)
        if self.head is None:
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def insert_last(self, value: any) -> None:
        new_node = ListNode(value)
        if self.tail is None:
            self.head = self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

    def delete_node(self, value: any) -> None:
        current = self.head
        while current:
            if current.data == value:
                if current.prev:
                    current.prev.next = current.next
                if current.next:
                    current.next.prev = current.prev
                if current == self.head:
                    self.head = current.next
                if current == self.tail:
                    self.tail = current.prev
                return
            current = current.next

    def search_node(self, value: any) -> bool:
        current = self.head
        while current:
            if current.data == value:
                return True
            current = current.next
        return False

    def insert_after(self, node: any, value: any) -> None:
        current = self.head
        while current:
            if current.data == node:
                new_node = ListNode(value)
                new_node.prev = current
                new_node.next = current.next
                if current.next:
                    current.next.prev = new_node
                current.next = new_node
                if current == self.tail:
                    self.tail = new_node
                return
            current = current.next

    def length(self) -> int:
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count

    def reverse(self) -> None:
        current = self.head
        self.tail = current
        prev = None
        while current:
            next_node = current.next
            current.next = prev
            current.prev = next_node
            prev = current
            current = next_node
        self.head = prev

    def remove_duplicates(self) -> None:
        current = self.head
        while current and current.next:
            if current.data == current.next.data:
                next_node = current.next.next
                if next_node:
                    next_node.prev = current
                current.next = next_node
                if current.next is None:
                    self.tail = current
            else:
                current = current.next

    def rotate(self, n: int) -> None:
        if not self.head or n == 0:
            return
        length = self.length()
        n = n % length
        if n == 0:
            return
        current = self.head
        for _ in range(length - n - 1):
            current = current.next
        new_head = current.next
        new_tail = current
        new_head.prev = None
        new_tail.next = None
        self.tail.next = self.head
        self.head.prev = self.tail
        self.head = new_head
        self.tail = new_tail