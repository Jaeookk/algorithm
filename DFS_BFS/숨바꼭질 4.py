import sys
from collections import deque

n, k = map(int, sys.stdin.readline().split())
count = [(0, 0) for _ in range(100001)]
cnt = 0


def bfs(v):
    global cnt
    queue = deque()
    queue.append(v)
    count[v] = (1, 0)
    while queue:
        v = queue.popleft()
        # if v == k:
        #     print(count[k][0] - 1)
        #     break

        for next_v in (v - 1, v + 1, 2 * v):
            if 0 <= next_v <= 100000:
                if count[next_v][0] == 0 or count[next_v][0] >= count[v][0] + 1:
                    queue.append(next_v)
                    count[next_v] = (count[v][0] + 1, v)


bfs(n)
print(count[k][0] - 1)
result = [k]
while True:
    if k == n:
        break
    temp = count[k][1]
    result.append(temp)
    k = temp

for i in range(len(result) - 1, -1, -1):
    print(result[i], end=" ")


# print(count[k] - 1)
# print(cnt)
