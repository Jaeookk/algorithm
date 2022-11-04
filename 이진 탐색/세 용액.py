import sys


n = int(input())
array = list(map(int, input().split()))
array.sort()


def binary_search(arr, x, y, start, end):
    global res
    right = 0
    while start <= end:
        mid = (start + end) // 2
        temp = arr[mid] + x + y
        if abs(temp) < res:
            res = abs(temp)
            right = mid

        if temp < 0:
            start = mid + 1
        else:
            end = mid - 1
    return right


res = sys.maxsize
for i in range(n - 2):
    for j in range(i + 1, n - 1):
        result = binary_search(array, array[i], array[j], j + 1, n - 1)
        if result != 0:
            right = result
            left = i
            mid = j
print(array[left], array[mid], array[right])


# ## 투 포인터
# import sys

# input = sys.stdin.readline

# n = int(input())
# arr = list(map(int, input().split()))
# arr.sort()

# res = sys.maxsize  # 임의의 max값
# result = []

# for i in range(n - 2):
#     left = i + 1  # 왼쪽 포인터
#     right = n - 1  # 오른쪽 포인터
#     while left < right:
#         _sum = arr[i] + arr[left] + arr[right]
#         if abs(_sum) < res:  # 기준값보다 작으면
#             result = [arr[i], arr[left], arr[right]]  # 세 용액 업데이트
#             res = abs(_sum)  # 결과값 업데이트
#         if _sum < 0:
#             left += 1
#         elif _sum > 0:
#             right -= 1
#         else:
#             break
# print(*result)
