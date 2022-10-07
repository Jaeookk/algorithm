n = int(input())
arr = [0] + [int(input()) for _ in range(n)]

# 1. 테이블 정의하기
# dp[i][j] = i번째 포도주까지 j번 연속해서 마셨을 때 최댓값

# 2. 점화식 찾기
# dp[k][0] = k번째 포도주를 마시지 않고 건너 뛰는 경우
# 즉, dp[k][0] = max(dp[k-1][1], dp[k-1][2])

# dp[k][1] = k번째 포도주를 마셨을때 처음으로 연속되어지는 포도주이므로
#           k-2번째 포도주를 마시고 2계단 건너뛰어 k번째 포도주를 마셨거나
#           k-1번째에서 아무것도 마시지 않고 k번째 포도주를 마시는 경우
# 즉, dp[k][1] = max(dp[k-1][0], dp[k-2][1], dp[k-2][2]) + s[k] (s[k]는 k번째 포도주)

# dp[k][2] = dp[k-1][1] + s[k]

# 3. 초기값 정하기
# dp[1][1] = s[1], dp[1][2] = 0
# dp[2][1] = s[2], dp[2][2] = s[1] + s[2]


def main():
    if n < 3:
        print(sum(arr))
        return
    dp = [[0, 0, 0] for _ in range(n + 1)]
    dp[1][0] = 0
    dp[1][1] = arr[1]
    dp[1][2] = 0
    dp[2][0] = arr[1]
    dp[2][1] = arr[2]
    dp[2][2] = arr[1] + arr[2]

    for i in range(3, n + 1):
        dp[i][0] = max(dp[i - 1][0], dp[i - 1][1], dp[i - 1][2])
        dp[i][1] = max(dp[i - 1][0], dp[i - 2][1], dp[i - 2][2]) + arr[i]
        dp[i][2] = dp[i - 1][1] + arr[i]
    # print(dp)
    print(max(dp[-1]))


if __name__ == "__main__":
    main()
