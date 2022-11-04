n = int(input())
array = list(map(int, input().split()))


def binary_search(arr, current, start, end):
    global res
    right = 0
    while start <= end:
        mid = (start + end) // 2
        temp = arr[mid] + current
        if abs(temp) < res:
            res = abs(temp)
            right = mid

        if temp < 0:
            start = mid + 1
        else:
            end = mid - 1
    return right


res = 1e10
for i in range(n - 1):
    result = binary_search(array, array[i], i + 1, n - 1)
    if result != 0:
        right = result
        left = i
print(array[left], array[right])


### 투 포인터 풀이
# n = int(input())
# array = list(map(int, input().split()))

# left = 0
# right = n - 1
# ans_L = 0
# ans_R = 0
# min = 1e10

# while left < right:
#     _sum = array[left] + array[right]

#     if abs(_sum) < min:
#         ans_L = left
#         ans_R = right
#         min = abs(_sum)

#     if _sum > 0:
#         right -= 1
#     elif _sum < 0:
#         left += 1
#     else:
#         break

# print(array[ans_L], array[ans_R])
