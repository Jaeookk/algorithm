# 4번째 시도
# 뒤에서 부터 접근해보자.
# 앞에서부토 접근하면 반복문을 순회하며 지나온 개수를 더하고,
# 다음 인덱스와 비교를 하지만,
# 뒤에서 부터 접근한다면 단순히 현재 max값보다 현재 인덱스 값이 더 작다면 그 차이만큼 이익을 더하면 된다.
import sys

T = int(sys.stdin.readline().strip())
for _ in range(T):
    N = int(sys.stdin.readline().strip())
    data = list(map(int, sys.stdin.readline().split()))
    result = 0
    max = 0
    for i in range(len(data) - 1, -1, -1):
        if data[i] > max:
            max = data[i]
        else:
            result += max - data[i]
    print(result)

# 1번째 시도 -> 91%에서 시간초과
# T = int(input())
# for _ in range(T):
#     N = int(input())
#     data = list(map(int, input().split()))
# buy = 0
# while data:
#     max_value = max(data)
#     index = data.index(max_value)
#     # print(max_value, "/", index)
#     buy += max_value * index - sum(data[:index])

#     if index < len(data) - 2:
#         data = data[index + 1 :]
#     else:
#         break
# print(buy)

# 2번째 시도 -> 여전히 시간초과
# T = int(input())
# for _ in range(T):
#     N = int(input())
#     data = list(map(int, input().split()))
#     m = max(data)
#     sum = 0
#     for i in range(N):
#         if data[i] == m:
#             data[i] = 0
#             m = max(data)
#         else:
#             sum += m - data[i]
#             data[i] = 0
#     print(sum)

# 3번째 시도
# import sys

# T = int(sys.stdin.readline().strip())
# for _ in range(T):
#     N = int(sys.stdin.readline().strip())
#     data = list(map(int, sys.stdin.readline().split()))
#     m = max(data)
#     sum = 0
#     for i in range(N):
#         if data[i] == m:
#             data[i] = 0
#             m = max(data)
#         else:
#             sum += m - data[i]
#             data[i] = 0
#     print(sum)
