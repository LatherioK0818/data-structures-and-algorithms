**ChatGPT**

# Challenge Title: Trees Implementation

## Whiteboard Process
![Whiteboard Solution](<White Board.png>)<

## Approach & Efficiency
This implementation uses a Node class and a BinaryTree class to construct and traverse binary trees. The BinaryTree class includes methods for pre-order, in-order, and post-order traversal. Each traversal method recursively visits nodes in a specific order, collecting their values into a list. The efficiency of these methods depends on the number of nodes in the tree (n). In the worst case, each node is visited once, making the time complexity O(n) for each traversal. Space complexity is also O(n) due to the storage of values in a list.

## Solution
To use this code:
1. Instantiate the BinaryTree class: `tree = BinaryTree()`.
2. Add nodes using the Node class: `node = Node(value)`.
3. Assign the root of the tree: `tree.root = node`.
4. Perform traversals like `tree.pre_order()`, `tree.in_order()`, and `tree.post_order()`. Each method will return a list of values in the specified traversal order.

**Example Usage:**
```python
tree = BinaryTree()
tree.root = Node(1)
tree.root.left = Node(2)
tree.root.right = Node(3)

print(tree.pre_order())  # Output: [1, 2, 3]
print(tree.in_order())   # Output: [2, 1, 3]
print(tree.post_order()) # Output: [2, 3, 1]
```
