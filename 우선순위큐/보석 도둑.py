# BOJ 1202 골드 2
# 무게가 가장 작은 가방에 들어가는 가장 비싼 보석을 그리디로 채우기
from collections import deque
import sys
import heapq

input = sys.stdin.readline

n, k = map(int, input().split())  # n
jewel = [list(map(int, input().rstrip().split())) for _ in range(n)]
jewel = deque(sorted(jewel, key=lambda x: x[0]))

bag = [int(input().rstrip()) for _ in range(k)]
bag.sort()  # 가방은 최대 무게가 가장 작은 가방부터.

max_heap = []
answer = 0
for i in range(k):
    while jewel and bag[i] >= jewel[0][0]:  # 가방에 들어갈 수 있는 모든 보석을 최대힙에 넣기
        price = -jewel.popleft()[1]
        heapq.heappush(max_heap, price)

    if max_heap:
        answer -= heapq.heappop(max_heap)
        # i번째 가방에 들어갈 수 있는 가장 높은 가격의 보석을 담은 후,
        # i+1번째 가방에 들어갈 수 있는 보석보다
        # i번째 가방에 들어갈 수 있었던 두 번째로 높은 가격의 보석이 있을 수 있다.
        # 이는 여전히 최대힙에 저장되어 있기 때문에 문제없다.

print(answer)
