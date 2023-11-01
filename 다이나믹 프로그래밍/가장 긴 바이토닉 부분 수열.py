n = int(input())
arr = list(map(int, input().split()))
arr_reverse = list(reversed(arr))

dp = [1] * n
dp_reverse = [1] * n

for i in range(n):
    for j in range(i):
        # 현재 위치(i)보다 이전에 있는 원소(j)가 작은지 확인한다. (크거나 같으면 가장 긴 증가하는 부분 수열이 될 수 없음)
        if arr[i] > arr[j]:
            # 작다면, 현재 위치의 이전 숫자 중, dp 최댓값을 구하고 그 길이에 1을 더해주면 된다.
            dp[i] = max(dp[i], dp[j] + 1)

        if arr_reverse[i] > arr_reverse[j]:
            dp_reverse[i] = max(dp_reverse[i], dp_reverse[j] + 1)

dp_reverse.reverse()

result = 0
for i in range(n):
    result = max(result, dp[i] + dp_reverse[i] - 1)

print(result)
