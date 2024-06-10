import sys
from collections import deque


def go_to_south(arr):
    flag = True
    while True:  # 계속 남쪽으로 이동
        for row, col in arr[1:4]:  # 동, 남, 서
            if row == R + 2:  # 이미 가장 남쪽으로 이동했다면 False를 반환(회전 고려 필요 X)
                return False
            if graph[row + 1][col] != 0:  # 한칸 아래에 골렘이 이미 있다면 멈추고 회전을 해야함
                flag = False
                break

        if not flag:
            break

        for row in arr:  # 이동할 수 있다면 한칸 아래로 이동
            row[0] += 1

    return True  # 회전을 해야함


def go_to_west(arr):
    global e

    flag = True
    idx = [0, 2, 3]
    for i in idx:  # 북, 남, 서
        row, col = arr[i]
        if col == 0:  # 서쪽으로 갈 수 없다면 멈춤
            flag = False
            break
        if graph[row][col - 1] != 0:  # 골렘이 이미 서쪽에 있어도 멈춤
            flag = False
            break

    if flag:  # 서쪽으로 이동할 수 있을 때
        for row, col in arr[2:4]:
            if graph[row + 1][col - 1] != 0:  # 남쪽으로 이동 할 수 있는지 조사. 남쪽으로 이동도 가능해야 회전이 이루어지기 때문.
                flag = False

    if not flag:
        return False
    else:
        for row in arr:  # 회전이 가능하다면
            row[1] -= 1  # 서쪽 한칸 이동
        e = (e - 1) % 4  # 출구 좌표 회전

        return True


def go_to_east(arr):
    global e

    flag = True
    for row, col in arr[:3]:  # 북, 동, 남
        if col == C - 1:  # 동쪽으로 갈 수 없다면 멈춤
            flag = False
            break
        if graph[row][col + 1] != 0:  # 골렘이 이미 동쪽에 있어도 멈춤
            flag = False
            break

    if flag:  # 동쪽으로 이동할 수 있을 때
        for row, col in arr[1:3]:
            if graph[row + 1][col + 1] != 0:  # 남쪽으로 이동 할 수 있는지 조사. 남쪽으로 이동도 가능해야 회전이 이루어지기 때문.
                flag = False

    if not flag:
        return False
    else:
        for row in arr:  # 회전이 가능하다면
            row[1] += 1  # 동쪽 한칸 이동
        e = (e + 1) % 4  # 출구 좌표 회전

        return True


def move(arr):
    while go_to_south(arr):  # True : 회전 조사 필요 / False : 최남단 도착
        if not go_to_west(arr):  # 서쪽 회전
            if not go_to_east(arr):  # 서쪽회전이 안된다면 동쪽회전
                break
        # 회전 이후 다시 남쪽으로 이동

    return 0


def bfs(matrix, row, col):
    value = graph[row][col]
    if value == 0:  # 현재 좌표가 골렘의 몸이 아니라면 BFS 종료
        return 0

    queue = deque([(row, col, value)])
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    visited = [[False for _ in range(C)] for _ in range(R + 3)]
    visited[row][col] = True
    max_row = 0

    while queue:
        x, y, cur_v = queue.popleft()
        for dx, dy in directions:
            nx, ny = x + dx, y + dy

            # 골렘의 몸이 숲에 다 들어온 상태이고, 방문하지 않았으며, 다음 좌표가 골렘의 일부일때 조사 시작
            if 3 <= nx < R + 3 and 0 <= ny < C and not visited[nx][ny] and graph[nx][ny] != 0:
                next_v = graph[nx][ny]

                # 다음 좌표가 현재 내가 있는 골렘의 몸 일부이거나, 현재 내가 있는 곳이 나갈 수 있는 출구라면 다음 좌표로 이동 가능.
                if cur_v == abs(next_v) or (cur_v < 0):
                    queue.append((nx, ny, next_v))
                    visited[nx][ny] = True

        max_row = max(max_row, x)

    return max_row - 2


def solution():
    global graph, e

    count = 0
    golem_num = 1

    for c, e in jinny:
        # c, e : 출발하는 열, 출구 방향 정보
        golem = [[0, c - 1], [1, c], [2, c - 1], [1, c - 2], [1, c - 1]]  # 골렘 위치(북동남서), 가운데

        # 남쪽으로 내려가기
        move(golem)

        for i in range(5):
            row, col = golem[i]
            if row < 3:  # 골렘의 몸 일부가 여전히 숲을 벗어난 상태 ~> 그래프 초기화 후 재시작
                graph = [[0 for _ in range(C)] for _ in range(R + 3)]
                golem_num = 0
                break

            if i != e:
                graph[row][col] = golem_num
            else:
                graph[row][col] = -golem_num  # 출구는 골렘 넘버의 음수로 지정.

        golem_num += 1

        # print(golem, e)
        # for row in graph[3:]:
        #     print(row)

        # TODO : 이동하기(출구는 현재 골렘의 출구만 이용하여 다른 골렘으로 이동 가능...) [V]
        res = bfs(graph, *golem[-1])

        # TODO : 점수 계산하기[V]
        count += res

    print(count)


if __name__ == "__main__":
    input = sys.stdin.readline
    R, C, K = map(int, input().split())  # 행, 열, 정령의 수
    jinny = [list(map(int, input().split())) for _ in range(K)]  # 출발하는 열, 출구 방향 정보
    graph = [[0 for _ in range(C)] for _ in range(R + 3)]  # 골렘의 몸 일부가 여전히 숲을 벗어난 상태를 확인하기 위해 3칸을 행에 더 추가.

    solution()
