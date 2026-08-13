# Practical 3: Max Heap Data Structure and Operations Analysis

## 1. Introduction

A **Max Heap** is a complete binary tree implemented efficiently using an array. In a Max Heap, the value of every parent node is greater than or equal to the values of its children. Therefore, the largest element is always stored at the root of the heap.

Max Heaps are widely used in **priority queues, scheduling systems, graph algorithms, and Heap Sort** because they provide efficient insertion and deletion of the maximum element.

This practical demonstrates the implementation and analysis of the following Max Heap operations:

* `heapify()`
* `build_max_heap()`
* `insert()`
* `delete_max()`

The program also uses Python's `time.perf_counter()` function to measure the execution time of the operations.

---

## 2. Objectives

The objectives of this practical are:

1. To understand the structure and properties of a Max Heap.
2. To implement a Max Heap using a Python list.
3. To implement the `heapify` operation.
4. To construct a Max Heap from an unsorted array.
5. To insert elements into a Max Heap.
6. To remove the maximum element from the heap.
7. To analyze the time and auxiliary space complexity of each operation.
8. To measure the execution time of the implementation.

---

## 3. Properties of a Max Heap

A Max Heap follows these important properties:

* It is a **complete binary tree**.
* Every parent node has a value greater than or equal to its children.
* The maximum element is always present at the root.
* It can be represented efficiently using an array.

For an element at index `i`, its corresponding positions are:

```text
Parent   = (i - 1) // 2
Left     = 2 * i + 1
Right    = 2 * i + 2
```

For example:

```text
             10
           /    \
          5      3
         / \
        4   1
```

Array representation:

```text
[10, 5, 3, 4, 1]
```

---

## 4. Operations Performed

### 4.1 Heapify

The `heapify()` operation restores the Max Heap property of a subtree.

It compares the current node with its left and right children. If one of the children is larger, the largest value is exchanged with the current node, and the process continues downward.

**Time Complexity:** `O(log n)`

**Auxiliary Space:** `O(log n)` for recursive implementation.

---

### 4.2 Build Max Heap

The `build_max_heap()` operation converts an arbitrary array into a valid Max Heap.

It starts from the last non-leaf node and calls `heapify()` repeatedly until reaching the root.

The last non-leaf node is located at:

```text
n // 2 - 1
```

**Time Complexity:** `O(n)`

**Auxiliary Space:** `O(1)` apart from recursive `heapify()` stack usage.

---

### 4.3 Insertion

To insert a new element:

1. Add the element at the end of the array.
2. Compare it with its parent.
3. If it is larger than the parent, swap them.
4. Continue moving upward until the Max Heap property is restored.

This process is called **sift-up** or **percolate-up**.

**Time Complexity:** `O(log n)`

**Auxiliary Space:** `O(1)`

---

### 4.4 Delete Maximum

The `delete_max()` operation removes the root element, which is the maximum value.

The procedure is:

1. Store the root value.
2. Replace the root with the last element.
3. Remove the last element.
4. Apply `heapify()` from the root.
5. Return the removed maximum value.

**Time Complexity:** `O(log n)`

**Auxiliary Space:** `O(log n)` for recursive `heapify()`.

---

## 5. Python Implementation

```python
import time


def heapify(arr, n, i):
    """Restore Max Heap property for the subtree rooted at index i."""
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    # Check left child
    if left < n and arr[left] > arr[largest]:
        largest = left

    # Check right child
    if right < n and arr[right] > arr[largest]:
        largest = right

    # If the largest element is not the current node
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]

        # Recursively heapify the affected subtree
        heapify(arr, n, largest)


def build_max_heap(arr):
    """Convert an unsorted array into a Max Heap."""
    n = len(arr)

    # Start from the last non-leaf node
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)


def insert(heap, value):
    """Insert a new value into the Max Heap."""
    heap.append(value)

    i = len(heap) - 1

    # Sift-up operation
    while i > 0:
        parent = (i - 1) // 2

        if heap[parent] >= heap[i]:
            break

        heap[parent], heap[i] = heap[i], heap[parent]
        i = parent


def delete_max(heap):
    """Remove and return the maximum element."""
    if not heap:
        raise IndexError("Cannot delete from an empty heap")

    if len(heap) == 1:
        return heap.pop()

    maximum = heap[0]

    # Move the last element to the root
    heap[0] = heap.pop()

    # Restore heap property
    heapify(heap, len(heap), 0)

    return maximum


def main():
    print("----- MAX HEAP IMPLEMENTATION -----")

    n = int(input("Enter the number of elements: "))

    elements = list(
        map(int, input("Enter the elements separated by spaces: ").split())
    )

    if len(elements) != n:
        print("Error: Number of elements does not match the given size.")
        return

    start_time = time.perf_counter()

    # Build Max Heap
    build_max_heap(elements)

    print("\nMax Heap:", elements)

    # Insert operation
    value = int(input("\nEnter element to insert: "))
    insert(elements, value)

    print("Heap after insertion:", elements)

    # Delete maximum
    deleted = delete_max(elements)

    print("Deleted Maximum Element:", deleted)
    print("Heap after deletion:", elements)

    end_time = time.perf_counter()

    print(f"\nExecution Time: {end_time - start_time:.8f} seconds")


if __name__ == "__main__":
    main()
```

---

## 6. Algorithms

### Algorithm: Build Max Heap

```text
BUILD-MAX-HEAP(A)
1. n ← length of A
2. for i ← n/2 - 1 down to 0
3.     HEAPIFY(A, n, i)
4. return A
```

### Algorithm: Insert

```text
INSERT(A, value)
1. Add value at the end of A
2. Set i to the index of the new element
3. while i > 0
4.     Find the parent of i
5.     If parent >= A[i], stop
6.     Swap parent and A[i]
7.     Move i to the parent index
```

### Algorithm: Delete Maximum

```text
DELETE-MAX(A)
1. If A is empty, report an error
2. Store A[0] as maximum
3. Replace A[0] with the last element
4. Remove the last element
5. HEAPIFY(A, length(A), 0)
6. Return maximum
```

---

## 7. Complexity Analysis

| Operation          | Time Complexity | Auxiliary Space | Description                             |
| ------------------ | --------------: | --------------: | --------------------------------------- |
| `heapify()`        |      `O(log n)` |      `O(log n)` | Restores heap property downward         |
| `build_max_heap()` |          `O(n)` |     `O(log n)`* | Builds a heap from an unsorted array    |
| `insert()`         |      `O(log n)` |          `O(1)` | Adds an element using sift-up           |
| `delete_max()`     |      `O(log n)` |     `O(log n)`* | Removes root and restores heap property |

*The space shown accounts for the recursive call stack used by `heapify()`. With an iterative implementation, the auxiliary space can be reduced to `O(1)`.

An important observation is that **building a heap is O(n), not O(n log n)**. Although `heapify()` can take `O(log n)` for one node, most nodes in a heap are close to the leaves and require very little work.

---

## 8. Sample Input and Output

### Input

```text
----- MAX HEAP IMPLEMENTATION -----
Enter the number of elements: 5
Enter the elements separated by spaces: 4 10 3 5 1

Max Heap: [10, 5, 3, 4, 1]

Enter element to insert: 15
Heap after insertion: [15, 5, 10, 4, 1, 3]

Deleted Maximum Element: 15
Heap after deletion: [10, 5, 3, 4, 1]

Execution Time: 0.0000xxxx seconds
```

The exact execution time will vary depending on the computer, Python version, system load, and input size.

---

## 9. Experimental Analysis

The program uses `time.perf_counter()` to measure the execution time of the Max Heap operations.

For small input sizes, the measured time may be extremely small and can vary between executions. Therefore, a single measurement should not be considered a complete performance analysis.

For more meaningful results, the program can be executed with different input sizes such as:

```text
10 elements
100 elements
1,000 elements
10,000 elements
100,000 elements
```

As the input size increases:

* `build_max_heap()` should demonstrate approximately linear growth.
* `insert()` should require at most logarithmic work.
* `delete_max()` should also require at most logarithmic work.
* `heapify()` should process a subtree in logarithmic time in the worst case.

---

## 10. Applications of Max Heap

Max Heaps are useful in many practical applications, including:

1. **Priority Queues** – managing elements according to priority.
2. **Heap Sort** – sorting elements efficiently.
3. **Job Scheduling** – selecting the highest-priority task.
4. **Graph Algorithms** – supporting priority-based operations.
5. **Resource Management** – efficiently identifying the largest or highest-priority value.

---

## 11. Advantages

* Efficient retrieval of the maximum element.
* Insertion takes `O(log n)` time.
* Deletion of the maximum element takes `O(log n)` time.
* Requires no additional tree node objects because it can be represented using an array.
* Building a heap from an unsorted array takes only `O(n)` time.

---

## 12. Limitations

* Searching for an arbitrary element is not efficient and can take `O(n)` time.
* A Max Heap does not maintain the complete ordering of a Binary Search Tree.
* Recursive `heapify()` requires additional call-stack space.
* The heap structure is less convenient for operations involving arbitrary sorted traversal.

---

## 13. Conclusion

This practical demonstrates the implementation of a **Max Heap using Python** and covers the fundamental operations `heapify`, `build_max_heap`, `insert`, and `delete_max`.

The analysis shows that individual heap adjustments, insertion, and deletion require **O(log n)** time in the worst case, while constructing a Max Heap from an unsorted array can be performed in **O(n)** time.

The Max Heap is therefore an efficient data structure for applications where the maximum or highest-priority element needs to be accessed or removed repeatedly. It is also an important component of **priority queues and Heap Sort**.
