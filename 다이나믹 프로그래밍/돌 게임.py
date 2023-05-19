# 백준 9655 실버5

import sys


if __name__ == "__main__":
    input = sys.stdin.readline

    n = int(input())

    dp = [-1] * 1001

    dp[1] = 1  # SK
    dp[2] = 0  # CY
    dp[3] = 1  # SK

    for i in range(4, n + 1):
        if dp[i - 1] == 1 or dp[i - 3] == 1:
            dp[i] = 0

        else:
            dp[i] = 1

    if dp[n] == 1:
        print("SK")

    else:
        print("CY")
