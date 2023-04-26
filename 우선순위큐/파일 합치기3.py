# BOJ 13975 골드4

import sys
import heapq


T = int(sys.stdin.readline())
for _ in range(T):
    k = int(sys.stdin.readline())
    arr = list(map(int, sys.stdin.readline().split()))
    heapq.heapify(arr)
    answer = 0
    while len(arr) > 1:
        a = heapq.heappop(arr)
        b = heapq.heappop(arr)
        heapq.heappush(arr, a + b)
        answer += a + b
    print(answer)
