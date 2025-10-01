class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        else:
            return "Stack is empty!"

    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        else:
            return "Stack is empty!"

    def is_empty(self):
        return len(self.stack) == 0

    def size(self):
        return len(self.stack)

stack = Stack()
print("Size after push:", stack.size())
stack.push(5)
stack.push(4)
stack.push(3)
print("Top element:", stack.peek())
print("Pop:", stack.pop())
print("Size after pop:", stack.size())
print("Is empty?", stack.is_empty())
print("Pop from empty:", stack.pop())
