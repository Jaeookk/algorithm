# 백준 10974 실버 3


def dfs(depth):
    if depth == n:
        print(*temp)
        return

    for i in range(1, n + 1):
        if not visited[i]:
            visited[i] = True
            temp.append(i)
            dfs(depth + 1)
            visited[i] = False
            temp.pop()


n = int(input())
visited = [False] * (n + 1)
temp = []
dfs(0)
