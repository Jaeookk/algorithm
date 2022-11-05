n = int(input())
arr = list(map(int, input().split()))
arr.sort()

cnt = 0
for i in range(n):
    tmp = arr[:i] + arr[i + 1 :]  # target을 제외
    target = arr[i]
    left, right = 0, len(tmp) - 1

    while left < right:
        t = tmp[left] + tmp[right]
        if t == target:
            cnt += 1
            break
        if t < target:
            left += 1  # t 를 증가시켜야 하므로 left 증가
        else:
            right -= 1  # t 를 감소시켜야 하므로 right 감소
print(cnt)
