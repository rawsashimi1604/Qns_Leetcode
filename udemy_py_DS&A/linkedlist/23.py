class Node:
    def __init__(self, data):
        self.data = data
        self.nextNode = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.numOfNodes = 0

    # This is why we like linked lists / O(1)
    def insert_start(self, data):
        self.numOfNodes += 1
        new_node = Node(data)

        # If node head does not exist, head is the new node.
        if not self.head:
            self.head = new_node
        # Else, make the new_node point to the previous node. Then, make the new_node the head.
        else:
            new_node.nextNode = self.head
            self.head = new_node

    # This is slow to implement / O(n)
    def insert_end(self, data):
        self.numOfNodes += 1
        new_node = Node(data)

        # If head node does not exist, insert_end adds the first node
        if not self.head:
            self.head = new_node

        # Else, until we find the last node, keep updating tmpNode. Then point the last node to the new node.
        else:
            tmpNode = self.head
            while (tmpNode.nextNode != None):
                tmpNode = tmpNode.nextNode

            tmpNode.nextNode = new_node

    # O(1)
    def size_of_list(self):
        return self.numOfNodes

    # Linear time complexity / O(n)
    def traverse(self):
        actual_node = self.head
        while (actual_node.nextNode != None):
            print(actual_node.data)
            actual_node = actual_node.nextNode

        print(actual_node.data)

    # O(n)
    def remove(self, data):
        # No nodes exist.
        if self.head is None:
            return

        current_node = self.head
        previous_node = None

        # current_node not none incase data does not exist in linked list
        while current_node is not None and current_node.data != data:
            previous_node = current_node
            current_node = current_node.nextNode

        if current_node == None:
            return

        # If previous_node is none, we want to remove the head node
        if previous_node == None:
            # Set the head to the nextNode
            self.head = current_node.nextNode

        # Else, point previous_node to the deleted-node's nextNode, thereby "missing out" the delete node.
        else:
            previous_node.nextNode = current_node.nextNode

        self.numOfNodes -= 1


l1 = LinkedList()
l1.insert_start(5)
l1.insert_start(10)
l1.insert_start(15)
l1.insert_end(30)
l1.insert_end('trevor')
l1.insert_end(1000.510)
l1.traverse()

print("----")
l1.remove(5)
l1.remove('trevor')
l1.traverse()

print("----")
print(l1.size_of_list())
