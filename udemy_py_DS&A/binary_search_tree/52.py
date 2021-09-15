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

    def traverse(self):
        if self.root:
            self.traverse_in_order(self.root)

    def traverse_in_order(self, node):
        if node.leftChild:
            self.traverse_in_order(node.leftChild)

        print('%s' % node.data)

        if node.rightChild:
            self.traverse_in_order(node.rightChild)

    def get_max_value(self):
        if self.root:
            return self.get_max(self.root)

    def get_max(self, node):
        if node.rightChild:
            return self.get_max(node.rightChild)

        return node.data

    def get_min_value(self):
        if self.root:
            return self.get_min(self.root)

    def get_min(self, node):
        if node.leftChild:
            return self.get_min(node.leftChild)

        return node.data


bst = BinarySearchTree()
bst.insert(10)
bst.insert(5)
bst.insert(66)
bst.insert(-5)
bst.insert(1)
bst.insert(99)
bst.insert(34)
bst.insert(-1000)
bst.traverse()


print("\n\n" + str(bst.get_max_value()))
print("\n\n" + str(bst.get_min_value()))
