import sys


n = int(input())
arr = list(map(int, input().split()))


def binary_search(arr, current, start, end):
    global res
    answer = None
    while start <= end:
        mid = (start + end) // 2
        temp = current + arr[mid]
        if abs(temp) < res:
            res = abs(temp)
            answer = temp
        if temp < 0:
            start = mid + 1
        elif temp > 0:
            end = mid - 1
        else:
            break
    return answer


res = sys.maxsize
for i in range(n - 1):
    temp = binary_search(arr, arr[i], i + 1, n - 1)
    if temp != None:
        ans = temp
print(ans)


# ## 투 포인터
# n = int(input())
# arr = list(map(int, input().split()))

# left = 0
# right = n - 1
# res = sys.maxsize
# while left < right:
#     temp = arr[left] + arr[right]
#     if abs(temp) < res:
#         res = abs(temp)
#         ans = temp

#     if temp > 0:
#         right -= 1
#     elif temp < 0:
#         left += 1
#     else:
#         break
# print(ans)
