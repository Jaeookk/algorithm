# dp[i] = i를 표현할 수 있는 제곱수 항의 최소 개수
#
# 점화식
# dp[i] = min(dp[i], dp[i-num^2]+1)
# 1부터 시작하여 조사를 시작.
# 만약 2를 조사할때 2^2 = 4 이므로, dp[i]는 dp[i-4]를 만드는 경우의 수 + 1 이다.
# 왜냐하면 만약 i가 6이면 2 + 4 = 6 이므로 2를 만드는 경우의 수 + 1을 하면 된다.
import math
import sys

n = int(sys.stdin.readline())
dp = [i for i in range(n + 1)]

k = int(n ** (1 / 2))
for x in range(2, k + 1):
    for i in range(x * x, n + 1):
        if dp[i] > dp[i - x * x] + 1:
            dp[i] = dp[i - x * x] + 1
        # dp[i] = min(dp[i], dp[i - x * x] + 1)
print(dp[n])
