class MaxStack:
    def __init__(self):
        self.mainStack = []
        self.maxStack = []  

    def push(self, data):
        self.mainStack.append(data)

        if len(self.mainStack) == 1:
            self.maxStack.append(data)
            return

        if data > self.maxStack[-1]:
            self.maxStack.append(data)
        else:
            self.maxStack.append(self.maxStack[-1])

    # O(1) running time
    def pop(self):
        data = self.mainStack[-1]
        del self.mainStack[-1]
        del self.maxStack[-1]

        return data

    # O(1) running time
    def get_max_item(self):
        return self.maxStack[-1]


maxstack = MaxStack()
maxstack.push(1)
maxstack.push(23)
maxstack.push(50)
maxstack.push(1000)
print(maxstack.get_max_item())