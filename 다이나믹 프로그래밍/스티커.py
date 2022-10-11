# dp[i][j] = i번째 행의 j번째 열 스티커를 뗐을 때 점수의 최대 합
# dp[i][j] = max(dp[*i][j-1]+dp[i][j], dp[i][j-2]+dp[i][j], dp[*i][j-2]+dp[i][j])
# ( *i : i의 반대 )

t = int(input())
for _ in range(t):
    n = int(input())
    sticker = [[0] + list(map(int, input().split())) for _ in range(2)]
    dp = [[0] * (n + 1) for _ in range(2)]
    # print(sticker)
    # print(dp)
    dp[0][1] = sticker[0][1]
    dp[1][1] = sticker[1][1]
    for i in range(2, n + 1):
        dp[0][i] = max(
            dp[1][i - 1] + sticker[0][i],
            dp[0][i - 2] + sticker[0][i],
            dp[1][i - 2] + sticker[0][i],
        )
        dp[1][i] = max(
            dp[0][i - 1] + sticker[1][i],
            dp[1][i - 2] + sticker[1][i],
            dp[0][i - 2] + sticker[1][i],
        )
    result = 0
    for x in dp:
        tmp = max(x)
        result = max(result, tmp)
    print(result)
