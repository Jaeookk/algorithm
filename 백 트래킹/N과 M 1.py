n, m = map(int, input().split())

array = [0] * 10
visited = [False] * 10


def dfs(k):
    if k == m:
        for i in range(m):
            print(array[i], end=" ")
        print()
        return
    for i in range(1, n + 1):
        if not visited[i]:
            array[k] = i
            visited[i] = True
            dfs(k + 1)
            visited[i] = False


dfs(0)
