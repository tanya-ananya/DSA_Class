class Stack:
   def __init__(self):
       self.stack = []

   def push(self, item):
       self.stack.append(item)

   def pop(self):
       if self.is_empty():
           return None
       return self.stack.pop()
   
   def peek(self):
       if self.is_empty():
           return None
       return self.stack[-1]
   
   def is_empty(self):
       return len(self.stack) == 0
   
   def size(self):
       return len(self.stack)

def checkBalancedParenthesis(s):
    stack = Stack()
    if s == '':
        raise TypeError
    
    pair_dicts = {
        '}': '{',
        ']': '[',
        ')': '('
    }

    for x in s:
        if x in pair_dicts.values():
            stack.push(x)
        elif x in pair_dicts:
            if stack.is_empty() == True:
                return "Unbalanced"
            if pair_dicts[x] != stack.pop():
                return "Unbalanced"
    if stack.is_empty():
        return "Balanced"
    return "Unbalanced"

def getUnbalancedPositions(s):
    stack = []
    unbalanced = []
    if s == '':
        raise TypeError
    
    pair_dicts = {
        '}': '{',
        ']': '[',
        ')': '('
    }

    for index, x in enumerate(s):
        if x in pair_dicts.values():
            stack.append((x, index))

        elif x in pair_dicts:
            if len(stack) == 0:
                unbalanced.append(index)
            else:
                paren, ind = stack.pop()
                if pair_dicts[x] != paren:
                    unbalanced.append(ind)
                    unbalanced.append(index)
    
    while stack:
        paren, ind = stack.pop()
        unbalanced.append(ind)

    return unbalanced