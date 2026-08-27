import time

INF = 9999


def greedy_change(coins, amount):
    """
    Greedy approach for Making Change.
    Sorts coins in descending order and greedily picks the largest available coin.
    Time Complexity: O(n log n)
    Space Complexity: O(1)
    """
    sorted_coins = sorted(coins, reverse=True)
    count = 0
    rem = amount
    used_coins = []

    for coin in sorted_coins:
        while rem >= coin:
            used_coins.append(coin)
            rem -= coin
            count += 1

    return count, used_coins


def dp_change(coins, amount):
    """
    Dynamic Programming approach for Making Change.
    Builds a 2D table dp[i][j] representing minimum coins needed to make amount j using first i coins.
    Time Complexity: O(n * amount)
    Space Complexity: O(n * amount)
    """
    n = len(coins)
    dp = [[0] * (amount + 1) for _ in range(n + 1)]

    # Base cases initialization
    for j in range(1, amount + 1):
        dp[0][j] = INF  # Amount j cannot be formed with 0 coins

    for i in range(1, n + 1):
        for j in range(1, amount + 1):
            dp[i][j] = dp[i - 1][j]  # Exclude current coin
            if coins[i - 1] <= j:
                dp[i][j] = min(dp[i][j], dp[i][j - coins[i - 1]] + 1)  # Include current coin

    # Backtrack to find coins used in DP solution
    used_coins = []
    curr_amount = amount
    curr_coin = n
    while curr_amount > 0 and curr_coin > 0:
        if dp[curr_coin][curr_amount] != dp[curr_coin - 1][curr_amount]:
            used_coins.append(coins[curr_coin - 1])
            curr_amount -= coins[curr_coin - 1]
        else:
            curr_coin -= 1

    return dp[n][amount], dp, used_coins


def print_dp_table(coins, amount, dp):
    """Prints the DP table formatted with aligned columns."""
    print("\n========== DP TABLE (min coins for each amount) ==========")
    header = f"{'Coin\\Amt':<10}" + "".join([f"{j:>5}" for j in range(amount + 1)])
    print(header)
    print("-" * len(header))

    for i in range(1, len(coins) + 1):
        row = f"{coins[i - 1]:<10}"
        for j in range(amount + 1):
            val = "-" if dp[i][j] >= INF else str(dp[i][j])
            row += f"{val:>5}"
        print(row)
    print("-" * len(header))


def main():
    coins = [1, 5, 6, 9]
    print(f"Coins available: {coins}")
    
    try:
        amount = int(input("Enter amount: "))
        if amount < 0:
            print("Amount cannot be negative.")
            return
    except ValueError:
        print("Invalid input! Please enter a valid integer.")
        return

    # Greedy Execution
    start_greedy = time.perf_counter()
    greedy_res, greedy_coins = greedy_change(coins, amount)
    end_greedy = time.perf_counter()
    greedy_time_ns = (end_greedy - start_greedy) * 1e9

    # DP Execution
    start_dp = time.perf_counter()
    dp_res, dp_table, dp_coins = dp_change(coins, amount)
    end_dp = time.perf_counter()
    dp_time_ns = (end_dp - start_dp) * 1e9

    # Output DP Table
    print_dp_table(coins, amount, dp_table)

    # Detailed Results
    print("\nGreedy Coins Used :", " ".join(map(str, greedy_coins)))
    print("DP Coins Used     :", " ".join(map(str, dp_coins)))

    print("\n========== RESULTS ==========")
    print(f"Amount              : {amount}")
    print(f"Greedy Result       : {greedy_res} coins")
    print(f"Greedy Time         : {greedy_time_ns:.2f} ns")
    print("-" * 31)
    print(f"DP Result           : {dp_res} coins")
    print(f"DP Time             : {dp_time_ns:.2f} ns")
    print("-" * 31)

    # Method Comparison Table
    print("\n========== COMPARISON ==========")
    print(f"{'Method':<12} | {'Coins':<10} | {'Optimal?':<10}")
    print("-" * 38)
    is_greedy_optimal = "Yes" if greedy_res == dp_res else "No"
    print(f"{'Greedy':<12} | {greedy_res:<10} | {is_greedy_optimal:<10}")
    print(f"{'DP':<12} | {dp_res:<10} | {'Yes':<10}")
    print("=" * 38)


if __name__ == "__main__":
    main()
