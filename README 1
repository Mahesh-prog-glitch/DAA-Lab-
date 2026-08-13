# Practical: Comparison of Sorting Algorithms

## 📌 Overview

This practical implements and compares five commonly used sorting algorithms in C++:

1. **Bubble Sort**
2. **Selection Sort**
3. **Insertion Sort**
4. **Merge Sort**
5. **Quick Sort**

The program generates a random dataset containing **10,000 integers** and applies each sorting algorithm to the same dataset. The execution time of every algorithm is measured using the C++ `<chrono>` library.

For additional comparison, the program also measures the performance of C++'s built-in `std::sort()` function.

The main objective is to understand the differences in algorithmic complexity and practical execution performance.

---

## 🎯 Objectives

The objectives of this practical are:

* To implement different sorting algorithms in C++.
* To understand how each sorting algorithm works.
* To compare their time complexities.
* To generate random test data.
* To measure the execution time of each algorithm.
* To compare custom sorting algorithms with the C++ Standard Library's `std::sort()`.

---

## 🔢 Dataset

The program uses:

```cpp
const int n = 10000;
```

Therefore, **10,000 random integer values** are generated.

The values are generated using:

```cpp
random_device rd;
mt19937 gen(rd());
uniform_int_distribution<> distrib(1, 10000);
```

This provides a randomly generated dataset containing values between `1` and `10,000`.

Every sorting algorithm receives a copy of the **same original dataset**, ensuring that the comparison is fair.

---

# 1. Bubble Sort

Bubble Sort repeatedly compares adjacent elements and swaps them if they are in the wrong order.

The implementation is optimized using an early-exit condition. If no swaps occur during a complete pass, the array is already sorted and the algorithm stops.

### Complexity

| Case         | Time Complexity |
| ------------ | --------------: |
| Best Case    |          `O(n)` |
| Average Case |         `O(n²)` |
| Worst Case   |         `O(n²)` |

**Space Complexity:** `O(1)`

### Advantage

The early-exit optimization makes Bubble Sort faster when the input is already sorted or nearly sorted.

---

# 2. Selection Sort

Selection Sort divides the array into sorted and unsorted portions.

During each iteration, it searches for the smallest element in the unsorted portion and places it at the beginning of that portion.

### Complexity

| Case         | Time Complexity |
| ------------ | --------------: |
| Best Case    |         `O(n²)` |
| Average Case |         `O(n²)` |
| Worst Case   |         `O(n²)` |

**Space Complexity:** `O(1)`

### Advantage

Selection Sort performs a relatively small number of swaps compared with some other simple sorting algorithms.

---

# 3. Insertion Sort

Insertion Sort builds the sorted array one element at a time.

Each new element is compared with the previously sorted elements and inserted into its correct position.

### Complexity

| Case         | Time Complexity |
| ------------ | --------------: |
| Best Case    |          `O(n)` |
| Average Case |         `O(n²)` |
| Worst Case   |         `O(n²)` |

**Space Complexity:** `O(1)`

### Advantage

Insertion Sort performs well on small or nearly sorted datasets.

---

# 4. Merge Sort

Merge Sort uses the **divide-and-conquer** technique.

The array is repeatedly divided into smaller subarrays. These subarrays are then merged back together in sorted order.

The implementation uses a temporary vector that is allocated only once before the recursive sorting process begins.

### Complexity

| Case         | Time Complexity |
| ------------ | --------------: |
| Best Case    |    `O(n log n)` |
| Average Case |    `O(n log n)` |
| Worst Case   |    `O(n log n)` |

**Auxiliary Space:** `O(n)`

### Advantage

Merge Sort provides predictable `O(n log n)` performance even in the worst case.

---

# 5. Quick Sort

Quick Sort is another **divide-and-conquer** sorting algorithm.

This implementation uses:

* A **middle element as the pivot**
* **Hoare's partition scheme**

The array is partitioned around the pivot, and the resulting portions are recursively sorted.

### Complexity

| Case         | Time Complexity |
| ------------ | --------------: |
| Best Case    |    `O(n log n)` |
| Average Case |    `O(n log n)` |
| Worst Case   |         `O(n²)` |

**Average Auxiliary Space:** `O(log n)` due to recursion.

### Advantage

Quick Sort is often very fast in practice because of its efficient memory access and low constant factors.

---

# 6. C++ `std::sort()`

The program also compares the custom implementations with:

```cpp
sort(a.begin(), a.end());
```

`std::sort()` is the standard sorting function provided by C++.

It is highly optimized and is generally much faster than basic algorithms such as Bubble Sort, Selection Sort, and Insertion Sort for large datasets.

Its complexity guarantee is typically **`O(n log n)`**.

---

# ⏱️ Execution Time Measurement

The program uses the C++ `<chrono>` library to measure the execution time of each algorithm.

The timing starts immediately before the sorting function and ends immediately after sorting is completed:

```cpp
auto start = high_resolution_clock::now();

sortFunc(dataCopy);

auto stop = high_resolution_clock::now();
```

The elapsed time is converted into microseconds:

```cpp
duration_cast<microseconds>(stop - start).count();
```

### Important Note

Execution times depend on:

* Processor speed
* Compiler and optimization settings
* Operating system
* Current system workload
* Random input distribution

Therefore, execution times may differ between different computers and different runs.

---

# 📊 Complexity Comparison

| Algorithm      |     Best Case |  Average Case |    Worst Case |                    Space |
| -------------- | ------------: | ------------: | ------------: | -----------------------: |
| Bubble Sort    |        `O(n)` |       `O(n²)` |       `O(n²)` |                   `O(1)` |
| Selection Sort |       `O(n²)` |       `O(n²)` |       `O(n²)` |                   `O(1)` |
| Insertion Sort |        `O(n)` |       `O(n²)` |       `O(n²)` |                   `O(1)` |
| Merge Sort     |  `O(n log n)` |  `O(n log n)` |  `O(n log n)` |                   `O(n)` |
| Quick Sort     |  `O(n log n)` |  `O(n log n)` |       `O(n²)` |       `O(log n)` average |
| `std::sort()`  | `O(n log n)`* | `O(n log n)`* | `O(n log n)`* | Implementation-dependent |

*The exact implementation details of `std::sort()` depend on the C++ standard library implementation, but modern implementations generally provide an `O(n log n)` worst-case guarantee.

---

# 📤 Sample Output

A typical output may look like:

```text
Number of Elements = 10000

Bubble Sort       : 185000 microseconds
Selection Sort    : 72000 microseconds
Insertion Sort    : 41000 microseconds
Merge Sort        : 1200 microseconds
Quick Sort        : 800 microseconds
std::sort (Baseline): 500 microseconds
```

> **Note:** These values are only examples. Your actual execution times will vary depending on your system.

---

# 🔬 Experimental Analysis

The experiment highlights a significant difference between **quadratic** and **`n log n`** sorting algorithms.

Bubble Sort, Selection Sort, and Insertion Sort have `O(n²)` average/worst-case complexity. With 10,000 elements, these algorithms can require a large number of comparisons and therefore generally take considerably longer.

Merge Sort and Quick Sort have approximately `O(n log n)` average performance and are significantly more suitable for larger datasets.

The C++ `std::sort()` function is included as a practical baseline because it is highly optimized for general-purpose sorting and will typically outperform the basic educational implementations.

---

# 🧠 Key Observations

1. **Bubble Sort** is simple but inefficient for large random datasets.
2. **Selection Sort** consistently performs quadratic numbers of comparisons.
3. **Insertion Sort** is useful for small or nearly sorted datasets.
4. **Merge Sort** provides consistent `O(n log n)` performance.
5. **Quick Sort** is generally very efficient in practice but has a theoretical `O(n²)` worst case.
6. **`std::sort()`** is highly optimized and is usually the fastest or among the fastest options in this comparison.
7. Increasing the dataset size makes the performance difference between algorithms more noticeable.

---

# 🗂️ Suggested GitHub Repository Structure

```text
practical-03-sorting/
│
├── sorting.cpp
└── README.md
```

### `sorting.cpp`

Contains the complete C++ implementation of all sorting algorithms and the benchmarking code.

### `README.md`

Contains the description, algorithm explanations, complexity analysis, experimental results, and conclusion.

---

# ▶️ How to Compile and Run

### Compile using g++

```bash
g++ sorting.cpp -o sorting
```

### Run on Linux/macOS

```bash
./sorting
```

### Run on Windows

```bash
sorting.exe
```

For a more meaningful comparison, compile with optimization enabled:

```bash
g++ -O2 sorting.cpp -o sorting
```

---

# 💡 Applications of Sorting Algorithms

Sorting is an important operation in computer science and is used in:

* Database management
* Searching and indexing
* Data analysis
* E-commerce product ordering
* Ranking systems
* File organization
* Operating systems
* Scientific computing
* Information retrieval

Choosing the appropriate sorting algorithm depends on the size and characteristics of the dataset.

---

# ⚠️ Limitations

* The experiment uses only one dataset size (`10,000` elements).
* Execution time can vary between systems.
* A single benchmark run may not provide statistically reliable results.
* The random dataset can contain duplicate values.
* Basic algorithms such as Bubble Sort and Selection Sort are not suitable for very large datasets.

For a more detailed performance study, the program could be extended to test multiple input sizes such as `1,000`, `10,000`, `100,000`, and `1,000,000` elements and run each algorithm multiple times.

---

# 🏁 Conclusion

This practical implements and compares **Bubble Sort, Selection Sort, Insertion Sort, Merge Sort, Quick Sort, and C++ `std::sort()`**.

The experiment demonstrates that algorithmic complexity has a major impact on sorting performance. The simple quadratic algorithms are easier to understand and implement but become inefficient as the input size increases.

Merge Sort and Quick Sort provide much better performance for large datasets because they generally operate in `O(n log n)` time. The C++ Standard Library's `std::sort()` provides an optimized real-world solution and is typically considerably faster than the basic implementations.

Overall, this practical demonstrates why selecting an appropriate sorting algorithm is essential for achieving efficient program performance.
