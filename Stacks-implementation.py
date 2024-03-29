class Stack:

    def __init__(self):
        self.stack = []
    
    def isEmpty(self):
        return self.stack == []

    def push(self, data):
        self.stack.append(data)
    
    def pop(self):
        data = self.stack[-1]
        del self.stack[-1]
        return data
    
    def peek(self):
        return self.stack[-1]
    
    def sizeStack(self):
        return len(self.stack)


stack= Stack()

stack.push(5)
stack.push(9)
stack.push(98)
stack.push(97)
print(stack.sizeStack())