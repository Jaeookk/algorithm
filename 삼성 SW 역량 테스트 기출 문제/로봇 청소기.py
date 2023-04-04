import sys

input = sys.stdin.readline

n, m = map(int, input().split())
graph = []
visited = [[0] * m for _ in range(n)]
r, c, d = map(int, input().split())
# 로봇 청소기가 있는 칸의 좌표 (r, c)와 바라보는 방향 d가 주어진다.
# d가 0인 경우에는 북쪽을, 1인 경우에는 동쪽을, 2인 경우에는 남쪽을, 3인 경우에는 서쪽을 바라보고 있는 것

# d => 0,3,2,1 (북동남서) 순서로 돌아야한다.
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

for _ in range(n):
    graph.append(list(map(int, input().split())))

# 처음 시작하는 곳 방문 처리
visited[r][c] = 1
cnt = 1

while True:
    flag = False
    # 4방향 확인
    for _ in range(4):
        # 0,3,2,1 순서 만들어주기위한 식
        d = (d + 3) % 4
        nx = r + dx[d]
        ny = c + dy[d]
        # 한번 돌았으면 그 방향으로 작업시작
        if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 0:
            if visited[nx][ny] == 0:
                visited[nx][ny] = 1
                cnt += 1
                r, c = nx, ny
                # 청소 한 방향이라도 했으면 다음으로 넘어감
                flag = True
                break
    if flag == False:  # 4방향 모두 청소가 되어 있을 때,
        if graph[r - dx[d]][c - dy[d]] == 1:  # 후진했는데 벽
            print(cnt)
            break
        else:  # 후진했는데 벽이 아닐때
            r, c = r - dx[d], c - dy[d]
