# BOJ 2617 골드4
import sys


def dfs(graph, v, visited, count):
    for next in graph[v]:
        if not visited[next]:
            visited[next] = True
            count = dfs(graph, next, visited, count + 1)
    return count


def main():
    input = sys.stdin.readline

    answer = 0
    n, m = map(int, input().split())
    max_graph = [[] for _ in range(n + 1)]
    min_graph = [[] for _ in range(n + 1)]

    for _ in range(m):
        a, b = map(int, input().split())
        max_graph[a].append(b)
        min_graph[b].append(a)

    for i in range(1, n + 1):
        visited = [False] * (n + 1)
        if dfs(max_graph, i, visited, 0) >= (n + 1) // 2:
            answer += 1
        if dfs(min_graph, i, visited, 0) >= (n + 1) // 2:
            answer += 1
    print(answer)

    return 0


if __name__ == "__main__":
    main()
