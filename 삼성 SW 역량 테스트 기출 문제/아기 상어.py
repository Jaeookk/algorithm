from collections import deque

N = int(input())

dx = [-1, 0, 0, 1]  # 상 좌 우 하
dy = [0, -1, 1, 0]
graph = [list(map(int, input().split())) for _ in range(N)]
sharksize = 2
sharkeat = 0

for i in range(N):
    for j in range(len(graph[i])):
        if graph[i][j] == 9:
            graph[i][j] = 0
            shark_x, shark_y = i, j


def finding_fish(sx, sy):
    """
    입력으로는 현재 아기 상어의 위치를 주고,
    출력으로는 후보를 리스트를 반환 해야한다.
    """
    global sharksize
    q = deque()
    q.append([sx, sy])

    visited = [[0 for _ in range(N)] for _ in range(N)]
    visited[sx][sy] = 1
    can_eat_fish = []

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < N and 0 <= ny < N:
                if graph[nx][ny] <= sharksize and not visited[nx][ny]:  # 이동이 가능하면
                    visited[nx][ny] = visited[x][y] + 1
                    q.append([nx, ny])

                    if graph[nx][ny] < sharksize and graph[nx][ny] != 0:  # 물고기가 있고 그걸 먹을 수 있다면
                        can_eat_fish.append([nx, ny, visited[nx][ny] - 1])

    can_eat_fish.sort(key=lambda x: (x[2], x[0], x[1]))  # 정렬은 거리, x(위아래), y(좌우) 오름차순으로
    return can_eat_fish


if __name__ == '__main__':
    ans = 0

    # 맨 앞의 먹이(가장 가까운)만 먹고 이동후 다시 BFS 돌리기
    while True:
        fishlist = finding_fish(shark_x, shark_y)

        if len(fishlist) == 0:  # 먹을 수 있는 물고기가 없다면
            print(ans)
            exit(0)

        shark_x, shark_y, move_time = fishlist[0]

        sharkeat += 1
        if sharksize == sharkeat:  # 먹은 물고기수와 사이즈가 같다면
            sharkeat = 0
            sharksize += 1

        graph[shark_x][shark_y] = 0  # 물고기 먹은 자리는 빈칸으로 바꿈
        ans += move_time
