class Node:
   def __init__(self, value):
       self.value = value
       self.next = None

class Queue:
    def __init__(self):
       self.front = None
       self.rear = None
       self._size = 0
    
    # Enqueue (add element to the front of the queue)
    def enqueue(self, item):
        new_node = Node(item)
        if self.rear is None:
           self.front = self.rear = new_node
        else:
           self.rear.next = new_node
           self.rear = new_node
        self._size += 1
        print(f'Enqueue: {item}')

    # Dequeue, removes and returns front element
    def dequeue(self):
        if self.is_empty():
           print('Queue is empty, cannot dequeue.')
           return None
        temp = self.front
        self.front = self.front.next

        if self.front is None:
           self.rear = None
        self._size -= 1
        print(f'Dequeued: {temp.value}')
        return temp.value
    
    # peek operation (see front without removing)
    def peek(self):
        if self.is_empty():
           print('Queue is empty')
           return None
        return self.front.value 
    
    # Check if queue is empty
    def is_empty(self):
       return self.front is None
    
    # Size of queue
    def size(self):
        return self._size
    
     # Display the queue
    def display(self):
        if self.is_empty():
           print('Queue is empty')
           return
        current = self.front
        print('Queue:', end=' ')
        while current:
           print(current.value, end=' -> ')
           current = current.next
        print("None")

print()
q = Queue()
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
print()
q.display()
print()
print(f'Front item is: {q.peek()}')
q.dequeue()
print()
q.display()
print()
q.dequeue()
print()
q.display()
print()
q.dequeue()
print()
q.display()
print()
