# https://school.programmers.co.kr/learn/courses/30/lessons/178870
from collections import deque


def solution(sequence, k):
    answer = []
    sequence += [0]

    q = deque()
    sum = 0
    start, end = 0, 0
    result = len(sequence)
    for i in range(len(sequence)):
        while sum > k:
            temp = q.popleft()
            sum -= temp
            start += 1
        if sum == k and end - start < result:
            answer = [start, end]
            result = end - start

        q.append(sequence[i])
        sum += sequence[i]
        end = i

    return answer


# def solution(sequence, k): # 투 포인터 풀이
#     n = len(sequence)

#     max_sum = 0
#     end = 0
#     interval = n

#     for start in range(n):
#         while max_sum < k and end < n:
#             max_sum += sequence[end]
#             end += 1
#         if max_sum == k and end-1-start < interval:
#             res = [start, end-1]
#             interval = end-1-start
#         max_sum -= sequence[start]

#     return res
