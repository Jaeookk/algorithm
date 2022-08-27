T = int(input())


def dfs(v):
    visited[v] = 1
    next = graph[v]
    if not visited[next]:
        dfs(next)


for i in range(T):
    answer = 0
    N = int(input())
    graph = [0] + list(map(int, input().split()))
    visited = [0] * (N + 1)

    for i in range(1, N + 1):
        if not visited[i]:
            dfs(i)
            answer += 1
    print(answer)
