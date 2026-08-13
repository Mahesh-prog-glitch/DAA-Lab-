# Practical 3: Max Heap Data Structure & Operations Analysis

This directory contains the Python implementation of a **Max Heap** data structure and its core operations (`heapify`, `build_max_heap`, `insert`, and `delete_max`). The program allows interactive execution with timing measurements using `time.perf_counter()`.

---

## 📌 Heap Concepts & Operations

A **Max Heap** is a complete binary tree where the key at the root node must be greater than or equal to the keys present at all of its children. The same property must be recursively true for all sub-trees in that binary tree.

### Key Operations Implemented

1. **`heapify(arr, n, i)`**
   - Restores the Max Heap property for a subtree rooted at index `i`, assuming subtrees are already heaps.
   - **Time Complexity:** $O(\log n)$
   - **Space Complexity:** $O(\log n)$ due to recursion stack (or $O(1)$ iterative).

2. **`build_max_heap(arr)`**
   - Converts an arbitrary unsorted list into a valid Max Heap by calling `heapify` bottom-up starting from the last non-leaf node (`n // 2 - 1` down to `0`).
   - **Time Complexity:** $O(n)$ (Linear time bound).

3. **`insert(heap, value)`**
   - Appends a new value to the end of the heap array and performs a **sift-up** (percolate up) operation until the heap property is restored.
   - **Time Complexity:** $O(\log n)$

4. **`delete_max(heap)`**
   - Removes and returns the maximum element (root) from the heap. Replaces the root with the last element and executes **`heapify`** on the root.
   - **Time Complexity:** $O(\log n)$

---

## ⚡ Complexity Summary

| Operation | Time Complexity | Auxiliary Space Complexity | Description |
| :--- | :---: | :---: | :--- |
| **Heapify** | $\mathcal{O}(\log n)$ | $\mathcal{O}(\log n)$ | Maintains heap property downward |
| **Build Max Heap** | $\mathcal{O}(n)$ | $\mathcal{O}(1)$ | Builds max heap from unsorted array |
| **Insertion** | $\mathcal{O}(\log n)$ | $\mathcal{O}(1)$ | Inserts element and sifts upward |
| **Delete Max** | $\mathcal{O}(\log n)$ | $\mathcal{O}(\log n)$ | Extracts root and heapifies downward |

---

## 💻 How to Run

1. Open your terminal or command prompt.
2. Navigate to the root directory or `practical-03-max-heap`:
   ```bash
   cd practical-03-max-heap
   ```
3. Run the Python script:
   ```bash
   python max_heap.py
   ```

### Sample Input & Output

```text
Enter the number of elements: 5
Enter the elements: 4 10 3 5 1

Max Heap: [10, 5, 3, 4, 1]

Enter element to insert: 15
Heap after insertion: [15, 5, 10, 4, 1, 3]
Deleted Maximum Element: 15
Heap after deletion: [10, 5, 3, 4, 1]

Execution Time: 0.00012345 seconds
```

## Summary
This practical implements a Max Heap data structure in Python, showcasing fundamental operations such as heapifying, building a max heap from an unsorted array, inserting new elements, and deleting the maximum element. The script also measures the execution time of these operations to illustrate their efficiency.

## Conclusion
The Max Heap provides an efficient way to repeatedly extract the maximum element from a dynamic dataset, achieving $O(\log n)$ time complexity for insertions and deletions. Building the heap structure is optimized to $O(n)$ time, making the heap a highly effective data structure for implementing priority queues and sorting algorithms like Heap Sort.
