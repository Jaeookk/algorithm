# BOJ 11279
import heapq
import sys

n = int(sys.stdin.readline())
heap = []
for _ in range(n):
    x = int(sys.stdin.readline())
    if x != 0:
        heapq.heappush(heap, (-x, x))
    else:
        if heap:
            print(heapq.heappop(heap)[1])
        else:
            print(0)
