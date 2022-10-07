t, w = map(int, input().split())
arr = [0] + [int(input()) for _ in range(t)]

dp = [[0] * (w + 1) for _ in range(t + 1)]
# dp[i][j] : i초에 j번 움직여서 받을 수 있는 자두의 최대 개수, 주인공은 1번위치에서 시작.

for i in range(1, t + 1):
    # 주인공이 한 번도 움직이지 않았다면 ([i][0]일때)
    if arr[i] == 1:
        dp[i][0] = dp[i - 1][0] + 1
    else:
        dp[i][0] = dp[i - 1][0]

    for j in range(1, w + 1):
        if j > i:
            break  # 매번 움직여도 j <= i 이므로

        if arr[i] == 1 and j % 2 == 0:
            # j가 짝수면은 1의 위치에 있는거니까
            # 그대로 있어서 받아먹기(dp[i-1][j]+1) or 2->1로 와서 받아먹기 (dp[i-1][j-1]+1)
            dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - 1]) + 1

        elif arr[i] == 2 and j % 2 == 1:
            # j가 홀수면은 2의 위치에 있는거니까
            # 그대로 있어서 받아먹기(dp[i-1][j]+1) or 1->2로 와서 받아먹기 (dp[i-1][j-1]+1)
            dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - 1]) + 1

        else:
            # 움직이지 않아서 자두를 먹지 못하는 경우
            dp[i][j] = dp[i - 1][j]

print(max(dp[-1]))
