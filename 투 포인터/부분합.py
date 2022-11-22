n, m = map(int, input().split())
arr = list(map(int, input().split()))

ans = 1e6
end = 0
_sum = arr[0]
for start in range(n):
    while end < n and _sum < m:
        end += 1
        if end != n:
            _sum += arr[end]
    if end == n:
        break
    ans = min(ans, end - start + 1)
    _sum -= arr[start]

if ans == 1e6:
    print(0)
else:
    print(ans)
