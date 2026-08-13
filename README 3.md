Max Heap Implementation in C++
📌 Description

This project implements a Max Heap data structure in C++. It demonstrates the basic operations performed on a Max Heap:

Building a Max Heap
Inserting an element
Deleting the maximum element
Displaying the heap
Measuring execution time

A Max Heap is a complete binary tree in which every parent node is greater than or equal to its children.

🛠️ Features
Build Max Heap
Converts the given array into a valid Max Heap.
Insert Element
Adds a new element to the heap and maintains the Max Heap property.
Delete Maximum
Removes the largest element, which is always located at the root.
Execution Time
Measures the time taken to perform the heap operations.
💻 Requirements
C++ compiler supporting C++11 or later
GCC, MinGW, Clang, or Visual Studio
🚀 How to Compile

Using GCC:

g++ main.cpp -o maxheap
▶️ How to Run

On Windows:

maxheap

On Linux/macOS:

./maxheap
📥 Example Input
Enter the number of elements: 5
Enter the elements: 10 20 15 30 40

Enter element to insert: 50
📤 Example Output
Max Heap: 40 30 15 10 20

Heap after insertion: 50 30 40 10 20 15

Deleted Maximum Element: 50
Heap after deletion: 40 30 15 10 20

Execution Time: 0.00000234 seconds

The exact execution time will vary depending on the computer.

⏱️ Time Complexity
Operation	Time Complexity
Build Max Heap	O(n)
Insert	O(log n)
Delete Maximum	O(log n)
Heapify	O(log n)
📂 Project Structure
MaxHeap/
│
├── main.cpp
└── README.md
🧠 Max Heap Representation

For an element at index i:

Parent = (i - 1) / 2
Left Child = 2 * i + 1
Right Child = 2 * i + 2

For example:

          40
        /    \
      30      15
     /  \
   10    20

Array representation:

40 30 15 10 20
