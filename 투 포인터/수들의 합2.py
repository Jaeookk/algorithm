n, m = map(int, input().split())
arr = list(map(int, input().split()))

end = 0
cnt = 0
_sum = arr[0]
for start in range(n):
    while end < n and _sum < m:
        end += 1
        if end != n:
            _sum += arr[end]
    if end == n:
        break
    if _sum == m:
        cnt += 1
    _sum -= arr[start]
print(cnt)
