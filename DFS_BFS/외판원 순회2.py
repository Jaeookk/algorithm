import sys

N = int(sys.stdin.readline())

graph = []
for arrive in range(N):
    graph.append(list(map(int, sys.stdin.readline().split())))

visited = [False] * N
count_arr = []
result = sys.maxsize


def dfs(v, start, visited):
    global result
    if len(count_arr) == N - 1:
        if graph[start][v] != 0:
            count = sum(count_arr) + graph[start][v]
            result = min(result, count)
        return
    else:
        for arrive in range(N):
            if arrive not in visited and graph[start][arrive] != 0:
                visited.append
                count_arr.append(graph[start][arrive])
                dfs(v, arrive)
                visited.pop()
                count_arr.pop()


for i in range(N):
    dfs(i, i, [i])

print(result)
