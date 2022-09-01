import sys
from collections import deque

n, k = map(int, sys.stdin.readline().split())
count = [0] * 100001  # 각 index는 K를 찾아가는 과정의 숫자이고, 그 value는 이제까지의 연산 횟수이다.


def bfs(v):
    queue = deque()
    queue.append(v)
    while queue:
        v = queue.popleft()
        if v == k:
            print(count[v])
            break

        for next_v in (v - 1, v + 1, 2 * v):
            if (
                0 <= next_v <= 100000 and count[next_v] == 0
            ):  # count[next_v] != 0이라는 소리는 이미 한번 i를 계산했다는 의미이므로 중복 계산 방지.
                queue.append(next_v)
                count[next_v] = count[v] + 1


bfs(n)
