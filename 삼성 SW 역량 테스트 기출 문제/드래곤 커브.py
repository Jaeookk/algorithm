# [endpoint 기준] 아래->왼쪽, 왼쪽->위, 위->오른쪽, 오른쪽->아래
# 즉, 아래->오른쪽->아래->왼쪽 이면, 회전 후 왼쪽->아래->왼쪽->위 이고, endpoint 기준으로 +1씩 해주면 된다.

n = int(input())
graph = [[0] * 101 for _ in range(101)]

# 하 좌 상 우
dx, dy = [1, 0, -1, 0], [0, -1, 0, 1]

for _ in range(n):
    x, y, d, g = map(int, input().split())
    direction = [d]
    graph[x][y] = 1
    for i in range(g):  # 세대 모양 조사
        temp = []
        for d in reversed(direction):   # endpoint 기준으로 생각해야 하므로 direction 뒤집기
            temp.append((d + 1) % 4)    # [endpoint 기준] 아래->왼쪽, 왼쪽->위, 위->오른쪽, 오른쪽->아래 로 바꿔주기
        direction = direction + temp    # 회전시킨 모양을 전 세대의 endpoint에 붙이기

    for d in direction:
        # 시작점을 기준으로 방향에 따라 1씩 더해서 모양 만들기
        x = x + dx[d]
        y = y + dy[d]
        graph[x][y] = 1

result = 0
for i in range(100):
    for j in range(100):
        if graph[i][j]*graph[i + 1][j]*graph[i][j + 1]*graph[i + 1][j + 1] == 1:
            result = result + 1
print(result)
