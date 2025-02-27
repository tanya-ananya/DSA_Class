class ListNode:
    def __init__(self, data:any) -> None:
        self.data = data
        self.prev = None
        self.next = None
    
class DoublyLinkedList:
    def __init__(self) -> None:
        self.head = None
        self.tail = None
    
    def insert_first(self, value: int) -> None:
        new_node = ListNode(value)

        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def insert_last(self, value: int) -> None:
        new_node = ListNode(value)
        
        if self.head is None:
            self.head = new_node
            return
        current = self.head
        while current:
            current = current.next
        temp = current
        current.next = new_node
        new_node.prev = current
    
    def delete_node(self, value: int) -> None:
        current = self.head

        if current is None:
            print("List is empty")
            return
        
        if current.data == value:
            self.head = current.next
            if self.head:
                self.head.prev = None
            current = None
            return
        while current and current.data != value:
            current = current.value
        if current is None:
            print(f'Node with value: {value}!')
            return
        if current.next:
            current.next.prev = current.prev
        if current.prev:
            current.prev.next = current.next
        current = None

    def search_node(self, value: int) -> bool:
        current = self.head

        if current is None:
            print("List is empty")
            return False
        
        while current:
            if current.data == value:
                return True
            current = current.next
        return False
    
    def insert_after(self, node: int, value: int) -> None:
        new_node = ListNode(node)
        current = self.head

        if current is None:
            print("List is empty")
            return False
        
        while current:
            if current.data == value:
                new_node.next = current.next
                new_node.prev = current
                if current.next:
                    current.next.prev = new_node
                current.next = new_node
                return
            current = current.next

    def length(self) -> int:
        current = self.head
        count = 0

        while current:
            current = current.next
            count += 1
        return count
    
    def reverse(self) -> None:
        current = self.head
        temp = None

        while current:
            temp = current.prev
            current.prev = current.next
            current.next = temp
            current = current.prev

        self.head = temp.prev
        
    def remove_duplicates(self) -> None:
        current = self.head

        while current:
            if current.next and current.data == current.next.data:
                next_node = current.next.next
                if next_node:
                    next_node.prev = current
                current.next = next_node
            else:
                current = current.next

    def rotate(self, n: int) -> None:
        if not self.head or n == 0:
            return

        current = self.head
        length = 1

        while current.next:
            current = current.next
            length += 1

        n = n % length
        if n == 0:
            return

        current.next = self.head
        self.head.prev = current

        steps_to_new_head = length - n
        new_tail = self.head

        for _ in range(steps_to_new_head - 1):
            new_tail = new_tail.next

        self.head = new_tail.next
        self.head.prev = None
        new_tail.next = None