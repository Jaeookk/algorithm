n, m = map(int, input().split())
data = list(map(int, input().split()))
data.sort()

arr = [0] * (m + 1)


def dfs(k):
    global arr, visited

    if k == m:
        print(*arr[:-1])
        return

    temp = 0
    for i in range(n):
        if temp != data[i] and arr[k - 1] <= data[i]:
            arr[k] = data[i]
            temp = data[i]
            dfs(k + 1)


dfs(0)
