from Node import Node


# Binary tree class
class Tree:
    def __init__(self, number_of_nodes):
        self.tree_root = Node(3)
        array = [5, 3, 4, 2, 1]
        for i in array:
            print("for" + str(i))
            self.insert(self.tree_root, i)

    def get_root(self):
        return self.tree_root

    # This function inserts a new node with the given data
    def insert(self, root, data):
        if root is None:
            return Node(data)
        else:
            if root.data == data:
                print("root")
                return root
            elif root.data < data:
                print("right")
                root.right = self.insert(root.right, data)
            else:
                print("left")
                root.left = self.insert(root.left, data)
        return root
