import sys
import heapq

input = sys.stdin.readline
N = int(input().strip())
time = []
h = []
for _ in range(N):
    s, t = map(int, input().split())
    time.append((s, t))
time = sorted(time, key=lambda x: (x[0], x[1]))

# 최소힙에 가장 빠르게 시작하고 가장 빠르게 끝나는 수업의 종료시간 넣기
heapq.heappush(h, time[0][1])

for i in range(1, N):
    # 다음 수업의 시작 시간이 이전 수업의 종료시간보다 작으면
    if time[i][0] < h[0]:
        heapq.heappush(h, time[i][1])
    # 다음 수업의 시작 시간이 이전 수업의 종료시간보다 크다면
    else:
        heapq.heappop(h)
        heapq.heappush(h, time[i][1])
print(len(h))

# 1   3
#   2    4
#     3    5
