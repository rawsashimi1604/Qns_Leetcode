import math
class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.nextNode = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        
        newNode = Node(data)

        if self.head == None:
            self.head = newNode

        else:
            newNode.nextNode = self.head
            self.head = newNode
        
    def traverse(self):
        ptrNode = self.head
        idx = 0
        while ptrNode != None:
            print(f"{idx}: {ptrNode.data}")
            idx += 1
            ptrNode = ptrNode.nextNode
    
    def findMiddleNode(self):
        fastPtr = self.head
        slowPtr = self.head

        while fastPtr.nextNode != None and fastPtr.nextNode.nextNode != None:
            fastPtr = fastPtr.nextNode.nextNode
            slowPtr = slowPtr.nextNode

        return slowPtr

    def findMiddleNodeSecond(self):
        ptrNode = self.head
        count = 0

        while ptrNode != None:
            count += 1
            ptrNode = ptrNode.nextNode
    
        ptrNode = self.head
        count = math.floor(count/2)
        for i in range(count):
            ptrNode = ptrNode.nextNode

        return ptrNode
            
l1 = LinkedList()
l1.insert(5)
l1.insert(4)
l1.insert(3)
l1.insert(2)
l1.insert(1)
l1.traverse()
print(l1.findMiddleNodeSecond().data)