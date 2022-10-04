# dp[i] = i자리 이친수의 개수
# dp[1] = 1
# dp[2] = 1
# dp[3] = 2
# dp[4] = 3
# dp[5] = 5

n = int(input())
dp = [0] * 91


def main():
    dp[1] = 1
    dp[2] = 1
    if n < 3:
        print(dp[n])
        return
    for i in range(3, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    print(dp[n])


if __name__ == "__main__":
    main()
