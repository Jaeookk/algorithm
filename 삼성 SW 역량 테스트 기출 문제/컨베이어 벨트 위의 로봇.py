# BOJ 20055
import sys
from collections import deque


N, K = map(int, sys.stdin.readline().split())
belt = deque(list(map(int, sys.stdin.readline().split())))
robots = deque([0 for _ in range(N)])
step = 0

while True:
    step += 1

    # 1. 벨트 회전
    belt.appendleft(belt.pop())
    robots.pop()
    robots.appendleft(0)
    if robots[-1] == 1:
        robots[-1] = 0

    # 2. 로봇 이동
    for i in range(N - 2, -1, -1):
        if robots[i] == 1:
            if robots[i + 1] != 1 and belt[i + 1] >= 1:
                robots[i + 1] = 1
                robots[i] = 0
                belt[i + 1] -= 1

    # 3. 로봇 올리기
    if belt[0] != 0:
        robots[0] = 1
        belt[0] -= 1

    # 4. 내구도가 0인 칸이 K개 이상이면 종료
    if belt.count(0) >= K:
        print(step)
        break
