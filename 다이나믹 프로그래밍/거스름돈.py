# https://school.programmers.co.kr/learn/courses/30/lessons/12907

# Dynamic Programming
# 1. 가장 작은 가치의 동전으로 n원을 만들 수 있는 경우의 수를 구한다.
# 2. 그 다음 동전으로 경우의 수를 구해야 하는데,
# 만약 (n-money)를 만들 수 있다면 -> n원을 만들 수 있다. (money를 더하면 i원 이니까...)
# 즉, dp[i]를 (money)로 i원을 만드는 경우의 수라고 하면
# dp[i] += dp[i-coin] 이다.
# 이미 구한 작은 가치의 화폐의 경우의 수(기존의 dp[i])에 그 이후의 가치의 화폐의 경우의수를 더한다.
# 백준 동전 문제와 같음.


def solution(n, money):
    answer = 0
    dp = [0] * (n + 1)
    dp[0] = 1
    for m in money:
        for i in range(m, n + 1):
            dp[i] = (dp[i] + dp[i - m]) % 1000000007
    return dp[-1]
