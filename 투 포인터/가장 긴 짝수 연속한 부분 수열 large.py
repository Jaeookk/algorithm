n, k = map(int, input().split())
arr = list(map(int, input().split()))


end, odd_cnt, even_cnt, res = 0, 0, 0, 0
for start in range(n):
    while end < n and odd_cnt <= k:
        if arr[end] % 2 == 1:
            odd_cnt += 1
        else:
            even_cnt += 1
        end += 1
        if start == 0 and end == n:  # 홀수개수가 k개 미만
            res = even_cnt
            break
    if odd_cnt == k + 1:
        res = max(even_cnt, res)

    if arr[start] % 2 == 1:
        odd_cnt -= 1
    else:
        even_cnt -= 1

print(res)
