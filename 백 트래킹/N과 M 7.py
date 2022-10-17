n, m = map(int, input().split())
data = list(map(int, input().split()))
data.sort()

arr = [0] * 10


def dfs(k):
    global arr

    if k == m:
        for i in range(m):
            print(arr[i], end=" ")
        print()
        return

    for i in range(len(data)):
        arr[k] = data[i]
        dfs(k + 1)


dfs(0)
