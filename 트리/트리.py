# 백준 4803 골드4
# 트리의 기본 개념(싸이클, 루프란? 정점(노드)가 하나 혹은 아예 없을때도 트리인가?) 다시 복습하기.

import sys
from collections import defaultdict, deque


def check_tree(v):
    res = True
    q = deque([v])
    while q:
        cur = q.popleft()
        if visited[cur] == 1:
            # 이 때, 뽑은 노드의 visited가 이미 1인 경우는 사이클이 존재한다는 것을 의미.
            # 예를 들어, 1-2, 2-3, 3-1인 사이클이 있다고 생각해보자.
            # 1에서 2와 3을 큐에 넣고, visited = [0, 1, 0, 0]이 된다.
            # 그 다음 2를 큐에서 뽑고, visited[2] = 1 이므로 visited = [0, 1, 1, 0], 3을 큐에 넣는다.
            # 그 다음 1에서 넣은 3을 큐에서 뽑고 visited = [0, 1, 1, 1].
            # 이제 큐에는 2에서 넣은 3이 아직 남아있다. 이 것을 뽑았을 때
            # visited[3]이 이미 1이므로 사이클로 판정
            res = False

        visited[cur] = 1

        for next in dic[cur]:
            if next == cur:  # 루프인지 확인
                res = False
            if visited[next] == 0:
                q.append(next)

    return res


if __name__ == "__main__":
    input = sys.stdin.readline
    case = 0

    while True:
        n, m = map(int, input().split())
        if n == 0 and m == 0:
            break

        case += 1
        dic = defaultdict(list)
        visited = [0] * (n + 1)
        ans = 0

        for _ in range(m):
            a, b = map(int, input().split())
            dic[a].append(b)
            dic[b].append(a)

        # visited가 0인 모든 노드를 돌면서
        # 가능한 모든 연결 요소(연결 그래프)를 순회함
        for node in range(1, n + 1):
            if visited[node] == 1:  # 방문을 했었다면
                continue
            if check_tree(node):
                ans += 1

        # 1번 예제는 정점 1-2-3-4가 하나의 트리, 정점 5가 하나의 트리, 정점 6이 하나의 트리로 트리가 총 3개
        if ans > 1:
            print("Case %d: A forest of %d trees." % (case, ans))
        elif ans == 1:
            print("Case %d: There is one tree." % case)
        else:
            print("Case %d: No trees." % case)
