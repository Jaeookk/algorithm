# https://school.programmers.co.kr/learn/courses/30/lessons/12987

import heapq


def solution(A, B):
    answer = 0
    A.sort()

    heapq.heapify(B)

    for a in A:
        while B:
            b = heapq.heappop(B)
            if a < b:
                answer += 1
                break
    return answer


# def solution(A, B):
#     answer = 0
#     A.sort()
#     B.sort()
#     j = 0

#     for i in range(len(A)):
#         if A[j] < B[i]:
#             answer = answer + 1
#             j = j+1

#     return answer
