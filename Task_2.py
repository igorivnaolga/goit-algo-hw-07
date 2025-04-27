class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

    def __str__(self, level=0, prefix="Root: "):
        ret = "\t" * level + prefix + str(self.val) + "\n"
        if self.left:
            ret += self.left.__str__(level + 1, "L--- ")
        if self.right:
            ret += self.right.__str__(level + 1, "R--- ")
        return ret

def insert(root, key):
    if root is None:
        return Node(key)
    else:
        if key < root.val:
            root.left = insert(root.left, key)
        else:
            root.right = insert(root.right, key)
    return root

def min_value_node(node):
    current = node
    while current.left:
        current = current.left
    return current

# Test
root = Node(30)
root = insert(root, 33)
root = insert(root, 22)
root = insert(root, 24)
root = insert(root, 37)
root = insert(root, 31)
root = insert(root, 38)

print(root)

min_node = min_value_node(root)
print(f"Min value in the tree is {min_node}")