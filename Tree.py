from Node import Node


# Binary tree class
class Tree:
    def __init__(self, root_data,  data_array):
        self.tree_root = Node(root_data)
        for data in data_array:
            self.insert(self.tree_root, data)

    def get_root(self):
        return self.tree_root

    # This function inserts a new node with the given data
    def insert(self, root, data):
        if root is None:
            return Node(data)
        else:
            if root.data == data:
                return root
            elif root.data < data:
                root.right = self.insert(root.right, data)
            else:
                root.left = self.insert(root.left, data)
        return root
