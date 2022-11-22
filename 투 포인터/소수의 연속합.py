n = int(input())

if n == 1:
    print(0)
    exit()

# 1. 소수 구하기
array = [True for _ in range(n + 1)]
arr = []
for i in range(2, int(n**0.5) + 1):
    if array[i] == True:  # i가 소수인 경우
        j = 2
        while i * j <= n:
            array[i * j] = False
            j += 1
for i in range(2, len(array)):
    if array[i] == True:
        arr.append(i)

# 2. 투 포인터
end = 0
cnt = 0
_sum = arr[0]
for start in range(len(arr)):
    while end < len(arr) and _sum < n:
        end += 1
        if end != len(arr):
            _sum += arr[end]
    if end == len(arr):
        break
    if _sum == n:
        cnt += 1
    _sum -= arr[start]
print(cnt)
