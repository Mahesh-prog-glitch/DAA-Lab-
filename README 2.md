# Practical: Linear Search and Binary Search

## 📌 Overview

This practical demonstrates and compares two commonly used searching algorithms in C++:

1. **Linear Search**
2. **Binary Search**

The program searches for a given value in a sorted array containing **100,000 elements**. It calculates the position of the target using both algorithms and measures their execution time using the C++ `<chrono>` library.

The main purpose of this practical is to understand the difference in performance and complexity between linear and binary searching.

---

## 🎯 Objectives

The objectives of this practical are:

* To understand the concept of searching algorithms.
* To implement Linear Search in C++.
* To implement Binary Search in C++.
* To compare their time complexities.
* To measure their execution time.
* To understand why Binary Search is more efficient for sorted data.

---

## 🔎 1. Linear Search

Linear Search is a simple searching technique that checks each element sequentially from the beginning of the array until the target value is found.

For example, to search for `152`:

```text id="y83n4t"
1 → 2 → 3 → 4 → ... → 151 → 152
```

The algorithm stops when the target is found.

### Characteristics

* Works with sorted or unsorted data.
* Easy to implement.
* Does not require the data to be sorted.
* Performance decreases as the input size increases.

### Complexity

| Case         | Time Complexity |
| ------------ | --------------: |
| Best Case    |          `O(1)` |
| Average Case |          `O(n)` |
| Worst Case   |          `O(n)` |

**Space Complexity:** `O(1)`

---

## ⚡ 2. Binary Search

Binary Search is a more efficient searching algorithm that works on **sorted data**.

Instead of checking every element, it repeatedly divides the search range into two halves.

For example, if the target is `152`, the algorithm:

1. Checks the middle element.
2. Determines whether the target is smaller or larger.
3. Discards the half that cannot contain the target.
4. Repeats the process until the target is found.

### Characteristics

* Requires sorted data.
* Significantly faster than Linear Search for large datasets.
* Uses a divide-and-conquer approach.
* Reduces the search range by half after every comparison.

### Complexity

| Case         | Time Complexity |
| ------------ | --------------: |
| Best Case    |          `O(1)` |
| Average Case |      `O(log n)` |
| Worst Case   |      `O(log n)` |

**Space Complexity:** `O(1)` for the iterative implementation used in this program.

---

## 💻 Program Implementation

The program creates a vector containing **100,000 sorted integers**, from `1` to `100000`.

It then asks the user for a target value and searches for that value using both Linear Search and Binary Search.

The `<chrono>` library is used to measure execution time in microseconds.

---

## ⏱️ Execution Time Measurement

The following C++ function is used to record the starting and ending times:

```cpp
high_resolution_clock::now()
```

The elapsed time is calculated using:

```cpp
duration_cast<microseconds>(finish - begin).count()
```

This provides the execution time in **microseconds**.

Actual execution times may vary depending on the computer, compiler, optimization settings, and current system workload.

---

## 📊 Complexity Comparison

| Algorithm     | Best Case | Average Case | Worst Case |  Space |
| ------------- | --------: | -----------: | ---------: | -----: |
| Linear Search |    `O(1)` |       `O(n)` |     `O(n)` | `O(1)` |
| Binary Search |    `O(1)` |   `O(log n)` | `O(log n)` | `O(1)` |

### Key Difference

For a dataset containing `n` elements:

* Linear Search may need to examine almost every element.
* Binary Search eliminates half of the remaining elements after each comparison.

Therefore, Binary Search is much more efficient for large **sorted** datasets.

---

## 📝 Sample Input

```text id="2rcg7v"
Enter the value to search: 152
```

## 📤 Sample Output

```text id="e4p2tm"
----- Linear Search -----
Value found at index: 151
Execution Time: 2 microseconds

----- Binary Search -----
Value found at index: 151
Execution Time: 1 microseconds

=== Code Execution Successful ===
```

Since C++ vectors use **zero-based indexing**, the value `152` is stored at index `151`.

---

## 🗂️ Suggested GitHub Repository Structure

```text id="4mbc3a"
practical-02-searching/
│
├── searching.cpp
└── README.md
```

### `searching.cpp`

Contains the complete C++ implementation of Linear Search and Binary Search.

### `README.md`

Contains the explanation, algorithms, complexity analysis, sample input/output, and conclusion.

---

## ▶️ How to Compile and Run

### Compile using g++

```bash id="1v42j9"
g++ searching.cpp -o searching
```

### Run on Linux/macOS

```bash id="e5u9h1"
./searching
```

### Run on Windows

```bash id="y5x3jm"
searching.exe
```

---

## 🔬 Experimental Analysis

For the given input size of **100,000 elements**, both algorithms can successfully locate the target value.

However, their approaches are different:

**Linear Search** examines elements one by one. If the target is near the end of the array, it may have to perform a large number of comparisons.

**Binary Search** repeatedly divides the search space into two halves. For 100,000 elements, it requires only a small number of comparisons compared with a worst-case Linear Search.

The measured execution time in this experiment may show Binary Search completing faster, although the exact difference can be very small for a single run.

For a more reliable performance comparison, the experiment can be repeated multiple times with different input sizes.

---

## ⚠️ Important Requirement for Binary Search

Binary Search can only be used correctly when the input data is **sorted**.

In this program, the vector is initialized as:

```cpp
numbers[i] = i + 1;
```

Therefore, the data is already sorted in ascending order.

If the vector were unsorted, the Binary Search implementation could return an incorrect result.

---

## 🌍 Applications

Searching algorithms are used in many real-world applications, including:

* Database searching
* File systems
* Contact lists
* Search engines
* Information retrieval
* Software applications
* Data processing systems

Binary Search is particularly useful when large amounts of data are already sorted.

---

## ✅ Advantages and Limitations

### Linear Search

**Advantages:**

* Simple to implement.
* Works with sorted and unsorted data.
* Requires no preprocessing.

**Limitations:**

* Slow for large datasets.
* Worst-case time complexity is `O(n)`.

### Binary Search

**Advantages:**

* Very efficient for large sorted datasets.
* Worst-case time complexity is `O(log n)`.
* Requires only constant auxiliary space in the iterative implementation.

**Limitations:**

* Data must be sorted.
* Maintaining sorted data can require additional work.

---

## 🏁 Conclusion

This practical demonstrates the implementation and performance comparison of **Linear Search and Binary Search** using C++.

Linear Search has a worst-case time complexity of **O(n)**, while Binary Search has a worst-case complexity of **O(log n)**. As the size of the dataset increases, the performance advantage of Binary Search becomes more significant.

The experiment shows why selecting an appropriate searching algorithm is important when working with large datasets. For sorted data, **Binary Search provides a much more efficient solution than Linear Search**.
