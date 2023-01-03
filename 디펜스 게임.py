# https://school.programmers.co.kr/learn/courses/30/lessons/142085
def solution(n, k, enemy):
    start,end = 0,len(enemy)
    while start<=end:
        cnt = k
        soldier = 0
        mid = (start+end)//2
        arr = sorted(enemy[:mid], reverse=True)
        for x in arr:
            if cnt > 0:
                cnt -= 1
                continue
            soldier += x
        if n-soldier >= 0 and cnt >= 0:
            start = mid + 1
        else:
            end = mid - 1
            
    return start-1

# 최소힙을 이용한 풀이
# import heapq as hq
# def solution(n, k, enemy):
#     q = enemy[:k]
#     hq.heapify(q)
#     for idx in range(k,len(enemy)):
#         n -= hq.heappushpop(q,enemy[idx])
#         if n < 0:
#             return idx
#     return len(enemy)
