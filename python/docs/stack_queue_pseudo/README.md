# Code Challenge: Implement a Queue using Two Stacks

This challenge involves implementing a Queue using two Stack data structures. The goal is to understand and apply the concepts of basic data structures to simulate a queue operation using stacks.

## Whiteboard Process


## Approach & Efficiency
The approach for this challenge was to utilize two stack instances to emulate the behavior of a queue. The primary reason for this approach is to demonstrate how two different data structures can be combined to achieve a specific goal.

- **Enqueue Method**: For the enqueue operation, the complexity is O(1) for both time and space, as it involves a simple push operation to one of the stacks.
- **Dequeue Method**: The dequeue operation has a time complexity of O(n) because it may require transferring all the elements from one stack to another. The space complexity remains O(1) as it does not require additional space proportional to the input size.

## Solution
To run this code, ensure you have a Java development environment set up with a Java compiler. Compile the source code and run the compiled class file. Below are some example commands and their expected outputs:

```bash
javac PseudoQueue.java
java PseudoQueue
```

**Example Usage:**

1. **Enqueue Operation:**
   - Command: `enqueue(10)`
   - Expected Output: `10 added to the queue`

2. **Dequeue Operation:**
   - Command: `dequeue()`
   - Expected Output: `10 removed from the queue`
