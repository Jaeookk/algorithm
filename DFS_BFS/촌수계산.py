n = int(input())
target_a, target_b = map(int, input().split())
m = int(input())

graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)


def dfs(graph, v, visited, target, count):
    global result
    if v == target_b:
        result = count
        return

    for next in graph[v]:
        if not visited[next]:
            visited[next] = True
            count += 1
            dfs(graph, next, visited, target, count)
            visited[next] = False
            count -= 1


result = 0
visited = [False] * (n + 1)
dfs(graph, target_a, visited, target_b, 0)

if result == 0:
    print(-1)
else:
    print(result)
