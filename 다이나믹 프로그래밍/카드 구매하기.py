n = int(input())
card = [0] + list(map(int, input().split()))

# dp[i] = 카드 i개 구매하는 최대 가격
# card[k] = k개가 들어있는 카드팩 가격 이라고 했을때
# 점화식
# dp[i] = dp[i-k] + card[k] (단, 0 < k <= i)
dp = [0] * (n + 1)

for i in range(1, n + 1):
    for k in range(1, i + 1):
        dp[i] = max(dp[i], dp[i - k] + card[k])

print(dp[-1])
