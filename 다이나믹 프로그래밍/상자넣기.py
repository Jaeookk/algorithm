n = int(input())
arr = list(map(int, input().split()))

dp = [1 for _ in range(n)]

for i in range(n - 1):
    for j in range(i + 1, n):
        if arr[i] < arr[j]:
            dp[j] = max(dp[j], dp[i] + 1)

print(max(dp))
