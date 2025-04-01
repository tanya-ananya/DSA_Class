class Stack:
    def __init__(self):
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

def expression(vals):
    if not vals:
        print('Values not provided')

    treeStack = Stack()
    numeric = False
    for x in vals:
        if x.isnumeric():
            treeStack.push(int(x))
            numeric = True
        elif x.isalpha():
            treeStack.push(x)
        else:
            if numeric:
                right_child = treeStack.pop()
                left_child = treeStack.pop()
                if x == '+':
                    treeStack.push(right_child + left_child)
                elif x == '-':
                    treeStack.push(right_child - left_child)
                elif x == '*':
                    treeStack.push(right_child * left_child)
                elif x == '/':
                    treeStack.push(right_child / left_child)
            else:
                right_child = treeStack.pop()
                left_child = treeStack.pop()
                treeStack.push(f"({left_child} {x} {right_child})")
    return treeStack.peek()

print(expression(["3", "4", "+", "2", "*", "7", "/"]))  # Expected output: 2.0
print(expression(["5", "1", "2", "+", "4", "*", "+", "3", "-"]))  # Expected output: 14
print(expression(["a", "b", "+", "c", "*", "d", "e", "+", "/"]))  # Expected output: ((a + b) * c) / (d + e)
