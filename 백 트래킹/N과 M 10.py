n, m = map(int, input().split())
data = list(map(int, input().split()))
data.sort()

arr = [0] * (m + 1)
visited = [False] * n


def dfs(k):
    global arr, visited

    if k == m:
        print(*arr[:-1])
        return

    temp = 0
    for i in range(n):
        if not visited[i] and temp != data[i] and arr[k - 1] <= data[i]:
            arr[k] = data[i]
            visited[i] = True
            temp = data[i]
            dfs(k + 1)
            visited[i] = False


dfs(0)
