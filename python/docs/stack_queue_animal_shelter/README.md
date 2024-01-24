# Challenge Title: First-in, First-out Animal Shelter

## Description of the Challenge

This challenge involves creating an Animal Shelter system that operates on a first-in, first-out basis and only accommodates dogs and cats. The system should be able to handle the admission (enqueue) of animals and the adoption (dequeue) based on the preference of the adopter.

## Whiteboard Process



## Approach & Efficiency

The approach for this challenge is to implement a class, `AnimalShelter`, which uses two queues internally: one for dogs and one for cats. This is to ensure that the first animal of the specified type that was admitted is the first one to be adopted, adhering to the first-in, first-out principle.

- **Time Complexity**: The enqueue operation has O(1) time complexity as it involves adding an animal to the end of a queue. The dequeue operation also has O(1) time complexity as it involves removing an animal from the front of the queue.
- **Space Complexity**: The space complexity is O(n), where n is the number of animals in the shelter, as we need to store each animal.

## Solution

**To run this code:**
1. Clone the repository and switch to the `stack-queue-animal-shelter` branch.
2. Navigate to the directory containing the `AnimalShelter` class.
3. Run the program to see the enqueue and dequeue operations in action.

**Example Usage:**
```python
shelter = AnimalShelter()
shelter.enqueue(Cat("Whiskers"))
shelter.enqueue(Dog("Fido"))
print(shelter.dequeue("cat"))  # Outputs: Cat named Whiskers
print(shelter.dequeue("dog"))  # Outputs: Dog named Fido
```

**Note**: Ensure to have classes or structs for `Dog` and `Cat` with at least `species` and `name` properties.
