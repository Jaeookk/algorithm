N = int(input())
graph = [list(map(int,input())) for _ in range(N)]


def dfs(x, y):
    global count
    if x <= -1 or x >= N or y <= -1 or y >= N:
        return False
    if graph[x][y] == 1:
        graph[x][y] = 2
        count += 1
        dfs(x - 1, y)
        dfs(x + 1, y)
        dfs(x , y - 1)
        dfs(x , y + 1)
        return True
    return False

total = 0
house_arr = []
for i in range(N):
    for j in range(N):
        count = 0
        if dfs(i,j):
            total += 1
        if count != 0:
            house_arr.append(count)
house_arr.sort()
print(total)
for i in house_arr:
    print(i)
        