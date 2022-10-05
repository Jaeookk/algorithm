T = int(input())


def main():
    dp = [0] * 101
    dp[1] = 1
    dp[2] = 1
    dp[3] = 1
    dp[4] = 2
    dp[5] = 2
    for _ in range(T):
        n = int(input())
        if n < 6:
            print(dp[n])
            continue
        for i in range(6, n + 1):
            dp[i] = dp[i - 1] + dp[i - 5]

        print(dp[n])


if __name__ == "__main__":
    main()
