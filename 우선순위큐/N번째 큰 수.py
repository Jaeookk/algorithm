# BOJ 2075
import sys
import heapq

n = int(sys.stdin.readline())
heap = []
for _ in range(n):
    for x in list(map(int, sys.stdin.readline().split())):
        heapq.heappush(heap, x)
        if len(heap) > n:
            heapq.heappop(heap)
print(heapq.heappop(heap))
