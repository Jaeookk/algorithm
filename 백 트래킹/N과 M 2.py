n, m = map(int, input().split())

arr = [0] * 10
visited = [False] * 10


def dfs(k):
    global arr, visited

    if k == m:
        for i in range(m):
            print(arr[i], end=" ")
        print()
        return

    for i in range(1, n + 1):
        if not visited[i] and arr[k - 1] < i:
            arr[k] = i
            visited[i] = True
            dfs(k + 1)
            visited[i] = False


dfs(0)
