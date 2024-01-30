# Challenge Title: Find Maximum Value in a Binary Tree

## Whiteboard Process

*Imagine a whiteboard diagram showing the binary tree with various nodes and values. The diagram would illustrate the traversal process across the tree, highlighting the comparison of node values.*

## Approach & Efficiency

### Approach:

The approach taken is a recursive traversal of the binary tree. This method is chosen because it provides a straightforward way to explore all nodes in the tree. The function compares the value of each node with the maximum value found so far in its left and right subtrees.

### Efficiency:

- **Time Complexity**: O(n), where n is the number of nodes in the tree. This is because each node is visited exactly once during the traversal.
- **Space Complexity**: O(h), where h is the height of the tree. This accounts for the maximum number of function calls stacked in the call stack due to recursion, which occurs in the case of a skewed tree.

## Solution

### How to Run:

1. Define the `Node` and `BinaryTree` classes as provided earlier.
2. Implement the `find_max_value` method in the `BinaryTree` class.
3. Create a binary tree and populate it with nodes.
4. Call the `find_max_value` method and print the result.

### Example:
```python
# Define the classes as discussed previously

# Create a binary tree
tree = BinaryTree()
tree.root = Node(10)
tree.root.left = Node(7)
tree.root.right = Node(15)
tree.root.left.left = Node(5)
tree.root.left.right = Node(9)
tree.root.right.right = Node(20)

# Find the maximum value
max_value = tree.find_max_value()
print(f"The maximum value in the tree is: {max_value}")
```

### Expected Output:
```
The maximum value in the tree is: 20
```

