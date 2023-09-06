import sys

sys.setrecursionlimit(100000)


def dfs(x, visited, L):
    visited[x] = L
    for node in graph[x]:
        if not visited[node]:
            L = dfs(node, visited, L + 1)
    return L


if __name__ == "__main__":
    n, m, r = map(int, input().split())
    graph = [[] for _ in range(n + 1)]
    for _ in range(m):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)
        graph[a].sort()
        graph[b].sort()

    visited = [0] * (n + 1)
    dfs(r, visited, 1)
    for i in range(1, n + 1):
        print(visited[i])
