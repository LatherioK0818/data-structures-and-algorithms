from data_structures.binary_tree import BinaryTree

# Define the tree_intersection function
def tree_intersection(tree1, tree2):
    def traverse_tree(node, hashmap):
        if node:
            hashmap[node.value] = True
            traverse_tree(node.left, hashmap)
            traverse_tree(node.right, hashmap)

    hashmap = {}
    traverse_tree(tree1.root, hashmap)

    common_values = set()
    def find_common(node):
        nonlocal common_values
        if node:
            if node.value in hashmap:
                common_values.add(node.value)
            find_common(node.left)
            find_common(node.right)

    find_common(tree2.root)
    return common_values


