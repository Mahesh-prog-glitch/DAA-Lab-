# Practical 7: Coin Change Problem (Greedy vs. Dynamic Programming Analysis)

This directory contains the Python implementation of the **Making Change Problem (Coin Change)** solved using both the **Greedy Algorithm** and **Dynamic Programming (DP)** paradigms. The program calculates the minimum number of coins needed to make a target amount given a coin denomination set $C = \{c_1, c_2, \dots, c_n\}$, outputs a fully formatted DP matrix, backtracks to identify exact coins used, and compares execution runtime using `time.perf_counter()`.

---

## 📌 Problem Overview & Paradigms

The **Coin Change Problem** asks for the minimum number of coins needed to make change for a target integer amount $V$ using a given set of coin denominations $C = \{c_1, c_2, \dots, c_n\}$.

### Methods Implemented

1. **Greedy Approach (`greedy_change(coins, amount)`)**
   - Sorts the coin denominations in descending order and greedily selects the largest available coin value less than or equal to the remaining amount.
   - **Time Complexity:** $\mathcal{O}(n \log n)$ (due to initial sorting of denominations).
   - **Space Complexity:** $\mathcal{O}(1)$ auxiliary space (excluding result list).
   - **Limitation:** Does **not** guarantee optimal solutions for arbitrary non-canonical coin systems (e.g., for $C = [1, 5, 6, 9]$ and target amount $11$, Greedy picks $9 + 1 + 1 = 3$ coins instead of the optimal $6 + 5 = 2$ coins).

2. **Dynamic Programming Approach (`dp_change(coins, amount)`)**
   - Constructs a 2D bottom-up tabulation matrix $dp[i][j]$ representing the minimum number of coins needed to form target amount $j$ using the first $i$ coin denominations.
   - **Recurrence Relation:**
     $$dp[i][j] = \begin{cases} dp[i-1][j] & \text{if } coins[i-1] > j \\ \min\left(dp[i-1][j], \; dp[i][j - coins[i-1]] + 1\right) & \text{if } coins[i-1] \le j \end{cases}$$
   - **Base Cases:**
     - $dp[i][0] = 0$ for all $i \in [0, n]$ (0 coins needed for amount 0).
     - $dp[0][j] = \infty$ for all $j > 0$ (amount cannot be formed with 0 coins).
   - **Backtracking:** Traces back through $dp[n][amount]$ to retrieve the exact set of coins that construct the optimal sum.
   - **Time Complexity:** $\mathcal{O}(n \times \text{amount})$
   - **Space Complexity:** $\mathcal{O}(n \times \text{amount})$

---

## ⚡ Complexity Summary

| Approach | Best Case | Average Case | Worst Case | Auxiliary Space | Paradigm | Guarantees Optimality? |
| :--- | :---: | :---: | :---: | :---: | :--- | :---: |
| **Greedy Method** | $\mathcal{O}(n \log n)$ | $\mathcal{O}(n \log n)$ | $\mathcal{O}(n \log n)$ | $\mathcal{O}(1)$ | Greedy Choice | ❌ No (Fails on non-canonical sets) |
| **Dynamic Programming** | $\mathcal{O}(n \times \text{amount})$ | $\mathcal{O}(n \times \text{amount})$ | $\mathcal{O}(n \times \text{amount})$ | $\mathcal{O}(n \times \text{amount})$ | DP (Tabulation) | ✅ Yes (Always Optimal) |

---

## 💻 How to Run

1. Open your terminal or command prompt.
2. Navigate to the `practical_7` directory:
   ```bash
   cd practical_7
   ```
3. Execute the Python script:
   ```bash
   python coin_change.py
   ```

---

## 📋 Sample Input & Output

### Example 1 (Target Amount = 11, Denominations = [1, 5, 6, 9]):
```text
Coins available: [1, 5, 6, 9]
Enter amount: 11

========== DP TABLE (min coins for each amount) ==========
Coin\Amt      0    1    2    3    4    5    6    7    8    9   10   11
----------------------------------------------------------------------
1             0    1    2    3    4    5    6    7    8    9   10   11
5             0    1    2    3    4    1    2    3    4    5    2    3
6             0    1    2    3    4    1    1    2    3    4    2    2
9             0    1    2    3    4    1    1    2    3    1    2    2
----------------------------------------------------------------------

Greedy Coins Used : 9 1 1
DP Coins Used     : 6 5

========== RESULTS ==========
Amount              : 11
Greedy Result       : 3 coins
Greedy Time         : 8300.00 ns
-------------------------------
DP Result           : 2 coins
DP Time             : 13599.99 ns
-------------------------------

========== COMPARISON ==========
Method       | Coins      | Optimal?  
--------------------------------------
Greedy       | 3          | No        
DP           | 2          | Yes       
======================================
```

---

## 📖 Key Takeaways & Conclusion

1. **Greedy vs. DP Optimality**:
   - The Greedy approach is locally optimal but can fail globally when coin systems are non-canonical (like $[1, 5, 6, 9]$).
   - Dynamic Programming explores overlapping subproblems and guarantees global optimality for any set of positive integer coin denominations.
2. **Time vs. Space Trade-off**:
   - Greedy runs in $\mathcal{O}(n \log n)$ time with $\mathcal{O}(1)$ extra memory.
   - DP requires $\mathcal{O}(n \times \text{amount})$ time and space to build the full 2D lookup table.
