def binary_search(target):
    left = 0
    right = len(dp) - 1

    while left < right:
        mid = (left + right) // 2
        if dp[mid] < target:
            left = mid + 1
        else:
            right = mid
    return right


n = int(input())
array = list(map(int, input().split()))

dp = [array[0]]

for i in array:
    if dp[-1] < i:
        dp.append(i)
    else:
        dp[binary_search(i)] = i

print(len(dp))
