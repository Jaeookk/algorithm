import sys
from collections import deque


def move_by_bfs(graph, graph_w, row, col, d):
    # BFS로 할까?
    # 1. graph_w에서 i번 값에 대해서 모두 이동 (병사 i의 이동)
    # 2. 이동 하고 난 이후, 다음 좌표 중 하나라도 다른 병사의 값(i번 값과 0이 아닌 값)이 있다면 상호작용
    #   2.1 j번 값에 대해서 모두 이동(병사 j의 이동)
    # 3. 2.1를 반복 언제까지? 상호작용이 일어나지 않을때까지
    # 4. 만약 1~3을 진행하는 동안 하나의 병사라도 맵을 벗어나는 상황이 발생한다면 전부 취소
    # 5. 전체 병사 이동 후 graph와 좌표를 비교하여 벽 좌표와 겹치는 병사가 하나라도 있다면 전부 취소

    value = graph_w[row][col]
    queue = deque([(row, col, value)])

    visited = [[False for _ in range(L)] for _ in range(L)]
    visited[row][col] = True

    direction = [(-1, 0), (0, 1), (1, 0), (0, -1)]  # 방패 범위를 찾기 위한 방향
    mx, my = direction[d][0], direction[d][1]  # 병사가 이동할 방향

    matrix = [[0 for _ in range(L)] for _ in range(L)]  # 임시 그래프

    moved_warrior = set()

    while queue:
        x, y, v = queue.popleft()

        if x + mx < 0 or x + mx >= L or y + my < 0 or y + my >= L:  # 이동한 곳이 범위를 벗어나면 병사 이동 중단
            return graph_w, []

        if graph[x + mx][y + my] == 2:  # 이동한 곳에 벽이 있다면 이동 중단
            return graph_w, []

        matrix[x + mx][y + my] = v  # 병사가 이동한 좌표를 임시 그래프에 기록
        moved_warrior.add(v)

        for i in range(4):
            nx, ny = x + direction[i][0], y + direction[i][1]
            if 0 <= nx < L and 0 <= ny < L and not visited[nx][ny] and graph_w[nx][ny] == v:
                queue.append((nx, ny, v))
                visited[nx][ny] = True

        if graph_w[x + mx][y + my] != v and graph_w[x + mx][y + my] != 0:
            queue.append((x + mx, y + my, graph_w[x + mx][y + my]))
            visited[x + mx][y + my] = True

    for i in range(L):
        for j in range(L):
            if not visited[i][j] and graph_w[i][j] != 0:
                matrix[i][j] = graph_w[i][j]

    return matrix, list(moved_warrior)


def solution(L, N, Q, warriors, graph, graph_w, commands):
    # out_warrior = []
    dmg_per_warrior = {k: 0 for k in range(1, N + 1)}
    result = 0

    for command in commands:
        warrior_num, d = command
        w_r, w_c, w_h, w_w, w_k = warriors[warrior_num - 1]  # TODO : 이동 후 좌표 업데이트 해야함.[v]

        if w_k <= 0:
            continue

        graph_w, moved_warrior = move_by_bfs(graph, graph_w, w_r, w_c, d)

        # 대결 대미지
        # 명령을 받은 병사와, 이동하지 않은 병사는 함정이 있어도 대미지 계산 X!!!
        for i in range(L):
            for j in range(L):
                if graph_w[i][j] in moved_warrior:
                    warriors[graph_w[i][j] - 1][0] = i
                    warriors[graph_w[i][j] - 1][1] = j

                    if graph_w[i][j] != warrior_num and graph[i][j] == 1:
                        warriors[graph_w[i][j] - 1][-1] -= 1
                        dmg_per_warrior[graph_w[i][j]] += 1

        # TODO : 체력이 0 이하인 병사는 체스판에서 사라져야한다...[v]
        for idx in range(N):
            if warriors[idx][-1] <= 0:
                dmg_per_warrior[idx + 1] = -1

        for i in range(L):
            for j in range(L):
                if graph_w[i][j] > 0 and dmg_per_warrior[graph_w[i][j]] == -1:
                    graph_w[i][j] = 0

    # TODO : 생존한 기사들이 총 받은 대미지의 합
    for k, v in dmg_per_warrior.items():
        if v > 0:
            result += v

    return result


if __name__ == "__main__":
    input = sys.stdin.readline

    L, N, Q = map(int, input().split())  # 체스판 크기, 기사의 수, 명령의 수
    graph = [list(map(int, input().split())) for _ in range(L)]  # 0:빈칸, 1:함정, 2:벽

    # (r,c,h,w,k) 위치(r,c), 방패(h,w), 체력
    warriors = [[r - 1, c - 1, h, w, k] for r, c, h, w, k in [list(map(int, input().split())) for _ in range(N)]]
    graph_w = [[0 for _ in range(L)] for _ in range(L)]

    commands = [tuple(map(int, input().split())) for _ in range(Q)]  # (i,d) i번 기사에서 방향 d로 한칸 이동. d:(0,1,2,3) 북동서남

    for i, (r, c, h, w, k) in enumerate(warriors):
        for row in range(r, r + h):
            for col in range(c, c + w):
                graph_w[row][col] = i + 1

    print(solution(L, N, Q, warriors, graph, graph_w, commands))
