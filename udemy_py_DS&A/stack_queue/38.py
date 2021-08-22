# LIFO STRUCTURE

class Stack: 
    def __init__(self) -> None:
        self.stack = []

    # Insert item into the stack, O(1)
    def push(self, data):
        self.stack.append(data)
    
    # Remove and return the last item we have inserted (LIFO), O(1)
    def pop(self):

        if self.stack_size() < 1:
            return

        data = self.stack[-1]
        del self.stack[-1]

        return data

    # Returns last item without removing it, O(1)
    def peek(self):
        if self.stack_size() < 1:
            return
        return self.stack[-1]

    # Check whether stack is empty, O(1)
    def is_empty(self):
        return self.stack == []

    def stack_size(self):
        return len(self.stack)


stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)

print(f'size : {stack.stack_size()}')
print(f'popped : {stack.pop()}')
print(f'size : {stack.stack_size()}')
print(f'peeked : {stack.peek()}')
print(f'size : {stack.stack_size()}')


