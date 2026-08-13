# Factorial Using Iterative and Recursive Methods

## 📌 Overview

This practical demonstrates two different approaches to calculate the **factorial of a non-negative integer** using C++:

1. **Iterative Method**
2. **Recursive Method**

The program calculates the factorial using both approaches and compares their execution times using the C++ `<chrono>` library.

---

## 🧮 What is Factorial?

The factorial of a non-negative integer `n` is the product of all positive integers from `1` to `n`.

It is represented as:

```text
n! = n × (n-1) × (n-2) × ... × 2 × 1
```

For example:

```text
5! = 5 × 4 × 3 × 2 × 1
5! = 120
```

The factorial of `0` is defined as:

```text
0! = 1
```

---

## ⚙️ Methods Used

### 1. Iterative Method

The iterative approach uses a `for` loop to calculate the factorial.

```cpp
for (int count = 2; count <= number; count++) {
    factorial *= count;
}
```

**Time Complexity:** `O(n)`

**Space Complexity:** `O(1)`

The iterative method does not require additional memory proportional to the input size.

---

### 2. Recursive Method

The recursive approach calculates the factorial by repeatedly calling the same function with a smaller value.

The mathematical definition is:

```text
n! = n × (n - 1)!
```

with the base cases:

```text
0! = 1
1! = 1
```

**Time Complexity:** `O(n)`

**Space Complexity:** `O(n)`

The additional space is required because every recursive function call is stored on the call stack.

---

## ⏱️ Execution Time Measurement

The program uses the C++ `<chrono>` library to measure the execution time of both methods.

The following functions are used:

```cpp
chrono::high_resolution_clock::now()
```

The execution time is calculated in **nanoseconds (ns)**.

This allows us to observe the performance difference between the iterative and recursive implementations.

> **Note:** For small input values, execution times can be extremely small and may vary between runs because of system load, compiler optimizations, and hardware differences.

---

## 💻 Program Features

* Accepts a non-negative integer from the user.
* Validates the input.
* Calculates factorial using the iterative method.
* Calculates factorial using the recursive method.
* Measures execution time for both methods.
* Displays the calculated factorial and execution time.
* Uses `unsigned long long` to store the result.

---

## 📊 Complexity Comparison

| Method    | Time Complexity | Space Complexity |
| --------- | --------------- | ---------------- |
| Iterative | `O(n)`          | `O(1)`           |
| Recursive | `O(n)`          | `O(n)`           |

### Comparison

The two approaches have the same asymptotic time complexity, `O(n)`. However, the iterative method uses constant auxiliary space, while the recursive method requires additional stack memory for each function call.

---

## 📝 Sample Input

```text
Enter a non-negative integer: 5
```

## 📤 Sample Output

```text
Factorial Results
Input Number : 5

Iterative Method
Factorial : 120
Execution Time : 100 ns

Recursive Method
Factorial : 120
Execution Time : 200 ns
```

*The execution times shown are examples. Actual values will vary depending on the system.*

---

## 🗂️ Suggested GitHub Structure

```text
practical-01-factorial/
│
├── factorial.cpp
└── README.md
```

### `factorial.cpp`

Place the provided C++ implementation in this file.

### `README.md`

This document can be used as the README file for the GitHub repository.

---

## ▶️ How to Compile and Run

### Using g++

```bash
g++ factorial.cpp -o factorial
```

Run the program:

```bash
./factorial
```

On Windows:

```bash
factorial.exe
```

---

## ⚠️ Limitation

The program uses `unsigned long long`, which can store factorial values only up to a limited range. For larger input values, the result will overflow.

For example, on systems where `unsigned long long` is 64-bit, factorial values beyond `20!` cannot be represented correctly.

---

## 🎯 Conclusion

This practical compares **iterative and recursive approaches for calculating factorials in C++**. Both methods have `O(n)` time complexity, but they differ in their memory requirements.

The iterative approach is generally more memory-efficient because it uses `O(1)` auxiliary space. The recursive approach provides a simple and mathematical implementation but requires `O(n)` stack space.

This practical also demonstrates how the C++ `<chrono>` library can be used to measure and compare the execution time of different algorithms.
