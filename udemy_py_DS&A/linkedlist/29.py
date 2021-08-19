class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.nextNode = None
        self.prevNode = None
    
class DoublyLinkedList:
    def __init__(self) -> None:
        self.head = None
        self.tail = None
        self.size = 0

    def insert_start(self, data):

        new_node = Node(data)

        # When the list is empty
        if self.head == None:
            self.head = new_node
            self.tail = new_node

        # else the list is not empty
        else:
            new_node.nextNode = self.head
            self.head.prevNode = new_node
            self.head = new_node
        
        self.size += 1

    def insert_end(self, data):

        new_node = Node(data)

        # When the list is empty
        if self.head == None:
            # Initialise the new node to be self.head and self.tail, 
            # and their nextNode and prevNode to be NONE
            self.head = new_node
            self.tail = new_node

        # If the list is not empty
        else:
            # Set the inserted node prevNode to be self.tail
            # self.tail = oldNode, self.tail.next = None
            new_node.prevNode = self.tail
            # new_node.prevNode = self.tail 


            # Set the previous self.tail's nextNode to be new_node
            # self.tail.next = newNode
            self.tail.nextNode = new_node

            # Finally, set tail as the newInserted Node
            # Set self.tail to the new_node
            self.tail = new_node

        self.size += 1
    
    def traverse_forward(self):

        actualNode = self.head
        idx = 0

        while actualNode != None:
            print(f"{idx}: {actualNode.data}")
            idx += 1
            actualNode = actualNode.nextNode
        

    def traverse_backward(self):

        actualNode = self.tail
        idx = self.size - 1

        while actualNode != None:
            print(f"{idx}: {actualNode.data}")
            idx -= 1
            actualNode = actualNode.prevNode

    
ll = DoublyLinkedList()
ll.insert_start(0)
ll.insert_start(1)
ll.insert_start(2)
ll.insert_start(3)
ll.traverse_forward()