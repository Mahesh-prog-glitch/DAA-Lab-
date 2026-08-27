import time


def knapsack_dp(weights, values, capacity):
    """
    Dynamic Programming (Tabulation) solution for the 0/1 Knapsack Problem.
    
    Builds a 2D table dp[i][w] representing the maximum value that can be 
    obtained using a subset of the first i items with weight capacity w.
    
    Time Complexity: O(n * W)
    Space Complexity: O(n * W)
    
    :param weights: List of item weights
    :param values: List of item values/profits
    :param capacity: Maximum weight capacity of the knapsack
    :return: (max_value, dp_matrix, selected_item_indices)
    """
    n = len(weights)
    # Initialize DP table with 0s
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]

    # Build table bottom-up
    for i in range(1, n + 1):
        for w in range(1, capacity + 1):
            if weights[i - 1] <= w:
                # Max of excluding current item vs. including current item
                dp[i][w] = max(
                    dp[i - 1][w],
                    values[i - 1] + dp[i - 1][w - weights[i - 1]]
                )
            else:
                # Item cannot fit in current capacity limit
                dp[i][w] = dp[i - 1][w]

    # Backtrack to find items included in optimal knapsack
    selected_items = []
    w = capacity
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i - 1][w]:
            selected_items.append(i - 1)  # 0-indexed item index
            w -= weights[i - 1]

    selected_items.reverse()  # Maintain natural item order
    return dp[n][capacity], dp, selected_items


def print_dp_table(weights, values, capacity, dp):
    """Prints the formatted 2D DP matrix."""
    print("\n========== DP TABLE (Max Value for each capacity) ==========")
    header = f"{'Item (w,v)':<15}" + "".join([f"{w:>6}" for w in range(capacity + 1)])
    print(header)
    print("-" * len(header))

    # Row 0: No items
    row0 = f"{'0 (Base)':<15}" + "".join([f"{dp[0][w]:>6}" for w in range(capacity + 1)])
    print(row0)

    # Rows 1 to n
    for i in range(1, len(weights) + 1):
        item_label = f"Item {i} ({weights[i-1]},{values[i-1]})"
        row = f"{item_label:<15}" + "".join([f"{dp[i][w]:>6}" for w in range(capacity + 1)])
        print(row)

    print("-" * len(header))


def main():
    print("==================================================")
    print("      0/1 KNAPSACK PROBLEM (DYNAMIC PROGRAMMING)   ")
    print("==================================================")

    # Default dataset for automated / interactive runs
    default_weights = [2, 3, 4, 5]
    default_values = [3, 4, 5, 6]
    default_capacity = 5

    print(f"Default Dataset:")
    print(f"  Weights  : {default_weights}")
    print(f"  Values   : {default_values}")
    print(f"  Capacity : {default_capacity}")
    
    user_choice = input("\nUse custom input? (y/N): ").strip().lower()
    
    if user_choice == 'y':
        try:
            n = int(input("Enter number of items: "))
            weights = []
            values = []
            print("Enter weight and value for each item:")
            for i in range(n):
                w, v = map(int, input(f"  Item {i + 1} (weight value): ").split())
                weights.append(w)
                values.append(v)
            capacity = int(input("Enter knapsack capacity: "))
        except Exception as e:
            print(f"Invalid input ({e})! Falling back to default dataset.")
            weights, values, capacity = default_weights, default_values, default_capacity
    else:
        weights, values, capacity = default_weights, default_values, default_capacity

    print("\n--- Running Dynamic Programming Solver ---")
    start_time = time.perf_counter()
    max_val, dp_table, selected_indices = knapsack_dp(weights, values, capacity)
    end_time = time.perf_counter()
    execution_time_ns = (end_time - start_time) * 1e9

    # Display DP matrix
    print_dp_table(weights, values, capacity, dp_table)

    # Summary Results
    print("\n========== OPTIMAL KNAPSACK SELECTION ==========")
    total_weight = 0
    total_value = 0
    if selected_indices:
        for idx in selected_indices:
            w, v = weights[idx], values[idx]
            total_weight += w
            total_value += v
            print(f"  - Item {idx + 1}: Weight = {w}, Value = {v}")
    else:
        print("  No items could be included in the knapsack.")

    print("\n========== RESULTS SUMMARY ==========")
    print(f"Knapsack Capacity  : {capacity}")
    print(f"Total Weight Used  : {total_weight} / {capacity}")
    print(f"Maximum Profit/Val : {max_val}")
    print(f"Execution Time     : {execution_time_ns:.2f} ns")
    print("======================================")


if __name__ == "__main__":
    main()
