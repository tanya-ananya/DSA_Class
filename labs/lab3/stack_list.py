class Node:
    def __init__(self, data):
        self.value = data
        self.next = next

class Stack:
    def __init__(self):
        self.top = None
        self.stack = []

    # Push operation (add an element)
    def push(self, item):
        self.stack.append(item)

    # Pop operation (remove and return top)
    def pop(self):
        if self.is_empty():
            return "Stack is empty, cannot pop"
        return self.stack.pop()
    
    # Peek operation (return top element, without removing)
    def peek(self):
        if self.is_empty():
            return "Stack is empty, cannot peak"
        return self.stack[-1]
    
    # Check if the stack is empty
    def is_empty(self):
        return len(self.stack) == 0
    
    # Return the size of the stack
    def size(self):
        return len(self.stack)
   
# Example usage of Stack
if __name__ == "__main__":
    my_stack = Stack()
    my_stack.push(10)
    my_stack.push(20)
    my_stack.push(30)

    print()
    print("Top element: ", my_stack.peek()) # Output: 30
    print()
    print("Stack size: ", my_stack.size()) # Output: 30
    print()

    print("Popped element: ", my_stack.pop()) # Output: 30
    print()
    print("Stack size after pop: ", my_stack.size()) # Output: 20
    print()