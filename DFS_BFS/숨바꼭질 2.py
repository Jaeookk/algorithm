import sys
from collections import deque

n, k = map(int, sys.stdin.readline().split())
count = [0] * 100001  # 각 index는 K를 찾아가는 과정의 숫자이고, 그 value는 이제까지의 연산 횟수이다.

cnt = 0


def bfs(v):
    global cnt
    queue = deque()
    queue.append(v)
    count[v] = 1
    while queue:
        v = queue.popleft()
        if v == k:
            cnt += 1

        for next_v in (v - 1, v + 1, 2 * v):
            if 0 <= next_v <= 100000:
                if count[next_v] == 0 or count[next_v] >= count[v] + 1:
                    queue.append(next_v)
                    count[next_v] = count[v] + 1


bfs(n)
print(count[k] - 1)
print(cnt)
