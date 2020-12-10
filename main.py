from Tree import Tree


def calculate_height(node):
    if node is None:
        return -1
    else:
        left_height = calculate_height(node.left)
        right_height = calculate_height(node.right)

        if left_height > right_height:
            return left_height + 1
        else:
            return right_height + 1


tree = Tree(8, [3, 1, 6, 4, 7, 10, 14, 13])
root = tree.get_root()

print("THe height of the given tree is", str(calculate_height(root)))
