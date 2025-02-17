'''
Lab 4, Part 2: Queue List Implementation
Author: Taaruni Ananya
'''

class Node:
   def __init__(self, data):
       self.value = data
       self.next = next

class Queue:
    def __init__(self):
        self.queue = []

    # Enqueue (add element to the front of the queue)
    def enqueue(self, item):
        self.queue.append(item)
        print(f'Enqueued: {item}')

    # Dequeue, removes and returns front element
    def dequeue(self):
        if not self.is_empty():
            item = self.queue.pop()
            print(f'Dequeued: {item}')
            return item
        else:
            print('Queue is empty, cannot dequeue') # Checks for underflow
            return None
        
    # peek operation (see front without removing)
    def peek(self):
        if not self.is_empty():
            return self.queue[0]
        else:
            print('Queue is empty.')
            return None
        
    # Check if queue is empty
    def is_empty(self):
        return len(self.queue) == 0
    
    # Size of queue
    def size(self):
        return len(self.queue)
    
    # Display the queue
    def display(self):
        print(f'Queue: {self.queue}')

q = Queue()
print()
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
q.display()
print()
print(f'Front item is: {q.peek()}')
q.dequeue()
q.display()
print()
q.dequeue()
q.display()
print()
q.dequeue()
q.display()
print()
