def compute(n):
    """
    docstring
    """
    coins = [1, 2, 5, 10, 20, 50, 100, 200]
    ways = [0] * (n+1)
    ways[0] = 1  # ways[n] how many ways to achive n
    for i in range(len(coins)):
        for j in range(coins[i], n+1):
            # 比如 coins[i] = 5, j = 13, ways[13] += ways[13 - 5 ] 即 ways[13] += ways[7]
            # 因为所有7 + coins[i]即可以为13，所以要加上所有为7的可能性。
            ways[j] += ways[j-coins[i]]
    return ways[n]


if __name__ == "__main__":
    print(compute(200))
