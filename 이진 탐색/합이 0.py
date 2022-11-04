## 투 포인터
import sys
from bisect import bisect_left


input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
arr.sort()


cnt = 0
for i in range(n - 2):
    left = i + 1  # 왼쪽 포인터
    right = n - 1  # 오른쪽 포인터
    while left < right:
        _sum = arr[i] + arr[left] + arr[right]
        if _sum == 0:
            if arr[left] == arr[right]:
                cnt += right - left
            else:
                idx = bisect_left(arr, arr[right])
                cnt += right - idx + 1
            left += 1
        elif _sum > 0:
            right -= 1
        else:
            left += 1

print(cnt)
