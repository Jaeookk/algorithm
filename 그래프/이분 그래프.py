# BOJ 1707 골드 4
import sys
from collections import deque

# 정점(노드)들을 이웃 꼭짓점들과 다른 색으로 계속해서 칠해 나가면서,
# 같은 색깔의 꼭짓점이 서로 연결되어 있는 모순이 발생하는지 여부를 확인하면 된다.


def bfs(v):
    global visited

    q = deque([v])
    visited[v] = 1

    while q:
        cur = q.popleft()
        for next in graph[cur]:
            if visited[next] == 0:
                visited[next] = visited[cur] * -1
                q.append(next)
            elif visited[next] == visited[cur]:
                return False
    return True


if __name__ == "__main__":
    input = sys.stdin.readline

    for _ in range(int(input())):
        V, E = map(int, input().split())
        graph = [[] for _ in range(V + 1)]
        visited = [0] * (V + 1)

        for _ in range(E):
            a, b = map(int, input().split())
            graph[a].append(b)
            graph[b].append(a)

        for i in range(1, V + 1):
            if visited[i] == 0:
                if bfs(i) == False:
                    print("NO")
                    break
        else:
            print("YES")
