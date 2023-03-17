# https://school.programmers.co.kr/learn/courses/30/lessons/12927#
import heapq


def solution(n, works):
    answer = 0
    if sum(works) <= n:
        return 0

    works = [-x for x in works]  # '-'를 붙이게 되면 최솟값이 아닌 최대값 기준으로 정렬
    heapq.heapify(works)
    while n > 0:
        max_v = heapq.heappop(works)
        heapq.heappush(works, max_v + 1)
        n -= 1
    # print(works)
    for w in works:
        answer += w**2
    return answer
