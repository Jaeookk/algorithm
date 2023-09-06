import sys

# 문제에서 요구하는 것은 '5개의 연속된 노드 존재 여부'
# 핵심은 연속된 '5개' 이다.


def dfs(x, visited, depth, ret=0):
    if depth == 5:
        return 1

    for node in graph[x]:
        if not visited[node]:
            visited[node] = 1
            ret = dfs(node, visited, depth + 1, ret)
            visited[node] = 0
    return ret


if __name__ == "__main__":
    n, m = map(int, input().split())
    graph = [[] for _ in range(n + 1)]
    answer = 0

    for _ in range(m):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    visited = [0] * (n + 1)
    for i in range(n):
        visited[i] = 1
        if dfs(i, visited, 1):
            answer = 1
            break
        visited[i] = 0
    print(answer)
