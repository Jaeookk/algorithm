# BOJ 1927
import heapq
import sys

n = int(sys.stdin.readline())
heap = []
for _ in range(n):
    x = int(sys.stdin.readline())
    if x != 0:
        heapq.heappush(heap, x)
    else:
        if heap:
            print(heapq.heappop(heap))
        else:
            print(0)
