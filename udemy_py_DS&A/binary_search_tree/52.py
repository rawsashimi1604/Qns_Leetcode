class Node:
    def __init__(self, data, parent):
        self.data = data
        self.leftChild = None
        self.rightChild = None
        self.parent = parent


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        # Insert to Root Node if root node is not found.
        if self.root == None:
            self.root = Node(data, None)

        else:
            self.insert_node(data, self.root)

    def insert_node(self, data, parent_node):
        # Insert normally to the left
        if data < parent_node.data:
            # If parent node is not empty, we need to traverse the left tree further (Use Recursion to traverse)
            if parent_node.leftChild:
                self.insert_node(data, parent_node.leftChild)

            # Base Case, data is smaller than parent node and there is not left child.
            # Create new node at parent left child, set parent to current iteration
            else:
                parent_node.leftChild = Node(data, parent_node)

        # Insert normally to the right
        else:
            if data > parent_node.data:
                if parent_node.rightChild:
                    self.insert_node(data, parent_node.rightChild)

                else:
                    parent_node.rightChild = Node(data, parent_node)


bst = BinarySearchTree()
bst.insert(10)
bst.insert(5)
bst.insert(66)
