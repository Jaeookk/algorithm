# 가장 긴 증가수열을 찾되 연속된 수를 가진 증가수열을 찾으면 문제를 해결할 수 있다.
import sys

N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))

dp = [0] * (N+1) # dp[n] = n번호일때까지 연속된 증가수열의 개수
mx = -1

for i in range(N):
    idx = arr[i]
    dp[idx] = dp[idx-1]+1
    mx = max(dp[idx], mx)

print(N-mx)