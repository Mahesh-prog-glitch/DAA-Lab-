# Practical 5: 0/1 Knapsack Problem (Dynamic Programming Analysis)

This directory contains the Python implementation of the **0/1 Knapsack Problem** solved using the **Dynamic Programming (DP)** paradigm. The program calculates the maximum value/profit achievable given a weight capacity $W$, item weights $w = \{w_1, w_2, \dots, w_n\}$, and item values $v = \{v_1, v_2, \dots, v_n\}$. It outputs a fully formatted DP tabulation matrix, backtracks to identify exact selected items, and records execution runtime using `time.perf_counter()`.

---

## 📌 Problem Overview & Paradigm

The **0/1 Knapsack Problem** is a classic combinatorial optimization problem. Given a set of $n$ items, each with a weight $w_i$ and a value $v_i$, determine which items to include in a collection such that the total weight does not exceed the knapsack capacity $W$ and the total value is maximized. Each item can either be taken (1) or left behind (0).

### Method Implemented

- **Dynamic Programming Tabulation (`knapsack_dp(weights, values, capacity)`)**
  - Constructs a 2D bottom-up matrix $dp[i][w]$ representing the maximum value that can be obtained using a subset of the first $i$ items with a knapsack weight capacity $w$.
  - **Recurrence Relation:**
    $$dp[i][w] = \begin{cases} dp[i-1][w] & \text{if } w_i > w \\ \max\left(dp[i-1][w], \; v_i + dp[i-1][w - w_i]\right) & \text{if } w_i \le w \end{cases}$$
  - **Base Cases:**
    - $dp[0][w] = 0$ for all $w \in [0, W]$ (0 value with 0 items).
    - $dp[i][0] = 0$ for all $i \in [0, n]$ (0 value with 0 capacity).
  - **Backtracking:** Traces back from $dp[n][W]$ to determine the exact set of items included in the optimal knapsack.
  - **Time Complexity:** $\mathcal{O}(n \times W)$ (where $n$ is number of items and $W$ is capacity).
  - **Space Complexity:** $\mathcal{O}(n \times W)$ for the 2D tabulation matrix.

---

## ⚡ Complexity Summary

| Approach | Best Case | Average Case | Worst Case | Auxiliary Space | Paradigm | Guarantees Optimality? |
| :--- | :---: | :---: | :---: | :---: | :--- | :---: |
| **Dynamic Programming (Tabulation)** | $\mathcal{O}(n \times W)$ | $\mathcal{O}(n \times W)$ | $\mathcal{O}(n \times W)$ | $\mathcal{O}(n \times W)$ | DP (Tabulation) | ✅ Yes (Always Optimal) |

---

## 💻 How to Run

1. Open your terminal or command prompt.
2. Navigate to the `practical_5` directory:
   ```bash
   cd practical_5
   ```
3. Execute the Python script:
   ```bash
   python knapsack.py
   ```

---

## 📋 Sample Input & Output

### Example (Weights = `[2, 3, 4, 5]`, Values = `[3, 4, 5, 6]`, Capacity = `5`):
```text
==================================================
      0/1 KNAPSACK PROBLEM (DYNAMIC PROGRAMMING)   
==================================================
Default Dataset:
  Weights  : [2, 3, 4, 5]
  Values   : [3, 4, 5, 6]
  Capacity : 5

Use custom input? (y/N): n

--- Running Dynamic Programming Solver ---

========== DP TABLE (Max Value for each capacity) ==========
Item (w,v)          0     1     2     3     4     5
---------------------------------------------------
0 (Base)            0     0     0     0     0     0
Item 1 (2,3)        0     0     3     3     3     3
Item 2 (3,4)        0     0     3     4     4     7
Item 3 (4,5)        0     0     3     4     5     7
Item 4 (5,6)        0     0     3     4     5     7
---------------------------------------------------

========== OPTIMAL KNAPSACK SELECTION ==========
  • Item 1: Weight = 2, Value = 3
  • Item 2: Weight = 3, Value = 4

========== RESULTS SUMMARY ==========
Knapsack Capacity  : 5
Total Weight Used  : 5 / 5
Maximum Profit/Val : 7
Execution Time     : 12500.00 ns
======================================
```

---

## 📖 Key Takeaways & Conclusion

1. **Optimal Substructure & Overlapping Subproblems**:
   - The 0/1 Knapsack problem exhibits optimal substructure. Dynamic Programming prevents redundant recalculation of subproblems by storing sub-results in a 2D lookup grid.
2. **0/1 Constraint**:
   - Items cannot be divided (unlike Fractional Knapsack, which uses a Greedy approach). Thus, DP guarantees the globally optimal choice for binary item selection.
3. **Time-Space Trade-off**:
   - Runs in pseudo-polynomial time $\mathcal{O}(n \times W)$ and requires $\mathcal{O}(n \times W)$ memory for the tabulation matrix.
