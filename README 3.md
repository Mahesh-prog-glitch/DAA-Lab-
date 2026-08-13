# Max Heap Implementation in C++

## Overview

This project implements a **Max Heap data structure in C++**. It demonstrates the basic operations performed on a Max Heap, including:

- Building a Max Heap
- Inserting an element
- Deleting the maximum element
- Displaying the heap
- Measuring execution time

A Max Heap is a complete binary tree in which every parent node is greater than or equal to its children. Therefore, the maximum element is always stored at the root.

---

## Features

- Build a Max Heap from an input array
- Insert a new element into the heap
- Delete the maximum element
- Display the heap after each operation
- Measure execution time
- Uses an array-based heap implementation
- Does not use the STL `priority_queue`

---

## Requirements

- C++ compiler
- C++11 or later
- GCC, MinGW, Clang, or Visual Studio

---

## Project Structure

```text
MaxHeap/
│
├── main.cpp
└── README.md
Compilation

Using GCC:

g++ -std=c++11 main.cpp -o maxheap

Or using C++17:

g++ -std=c++17 main.cpp -o maxheap
Running the Program
Windows
maxheap.exe
Linux/macOS
./maxheap
Example
Input
Enter the number of elements: 5
Enter the elements: 10 20 15 30 40

Max Heap: 40 30 15 10 20

Enter element to insert: 50
Output
Max Heap: 40 30 15 10 20
Heap after insertion: 50 30 40 10 20 15
Deleted Maximum Element: 50
Heap after deletion: 40 30 15 10 20

Execution Time: 0.00000234 seconds

Note: The execution time will vary depending on the computer and system load.

Max Heap Representation

For an element at index i:

Parent      = (i - 1) / 2
Left Child  = 2 * i + 1
Right Child = 2 * i + 2

Example:

              40
            /    \
          30      15
         /  \
       10    20

Array representation:

40 30 15 10 20
Operations
Build Max Heap

The program converts the input array into a valid Max Heap using the heapify() function.

Time Complexity: O(n)

Insert

A new element is added to the end of the heap and moved upward until the Max Heap property is restored.

Time Complexity: O(log n)

Delete Maximum

The root element is removed and replaced with the last element. The heap is then restored using heapify().

Time Complexity: O(log n)

Complexity Analysis
Operation	Time Complexity
Build Max Heap	O(n)
Heapify	O(log n)
Insert	O(log n)
Delete Maximum	O(log n)
Algorithms
Build Max Heap
Find the last non-leaf node.
Start from that node and move toward the root.
Apply heapify() to each node.
The resulting array becomes a Max Heap.
Insert
Add the new element at the end of the heap.
Find its parent.
Compare the element with its parent.
If the element is greater, swap them.
Continue until the Max Heap property is restored.
Delete Maximum
Store the root element.
Replace the root with the last element.
Remove the last element.
Apply heapify() from the root.
Return the deleted maximum element.
Technologies Used
Language: C++
Standard: C++11 or later
Libraries:
<iostream>
<vector>
<chrono>
Learning Objectives

This project demonstrates:

Binary Heap data structure
Complete binary trees
Array representation of trees
Heapify operation
Heap insertion
Heap deletion
Time complexity
Execution-time measurement
