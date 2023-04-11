def fibonacci(n):
    for i in range(3, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]


n = int(input())
dp = [0 for _ in range(n + 1)]
dp[1] = dp[2] = 1

fibonacci(n)
print(dp[n], n - 2)  # 코드 1은 재귀로 피보나치를 구할 때 return 1이 몇번 발생했냐 물어보는 것 -> n의 피보나치 수 값
