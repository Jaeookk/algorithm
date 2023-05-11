# 소프티어 레벨3
# 그리디, 우선순위큐
import sys
import heapq

input = sys.stdin.readline

n = int(input())
arr = []

for _ in range(n):
    start, end = map(int, input().split())
    heapq.heappush(arr, (end, start))

ans = 0
end = 0


for i in range(0, n):
    x = heapq.heappop(arr)
    if end <= x[1]:
        ans += 1
        end = x[0]
print(ans)
