# 항상 가장 작은 크기의 두 카드 묶음을 합쳤을 때 최적의 해가 나온다.
# 이를 위해 최소힙을 이용한다.
import sys
import heapq
f = sys.stdin.readline

n = int(f())
data = []
for _ in range(n):
    data.append(int(f()))

heapq.heapify(data)
answer = 0
while len(data) > 1:
    a = heapq.heappop(data)
    b = heapq.heappop(data)
    answer += a + b
    heapq.heappush(data, a+b)
    
print(answer)
