from collections import defaultdict, deque
import copy


def rotate(lst):
    n = len(lst)
    result = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            result[j][n - 1 - i] = lst[i][j]
    return result


def bfs(graph, start_x, start_y, num):
    n = len(graph)
    dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
    ret = [(0, 0)]
    q = deque()
    q.append((start_x, start_y, 0, 0))
    graph[start_x][start_y] = -1
    while q:
        x, y, ret_x, ret_y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            n_ret_x, n_ret_y = ret_x + dx[i], ret_y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and graph[nx][ny] == num:
                graph[nx][ny] = -1
                q.append((nx, ny, n_ret_x, n_ret_y))
                ret.append((n_ret_x, n_ret_y))
    return ret


def solution(game_board, table):
    answer = 0

    n = len(game_board)

    # 빈칸 모양 찾기
    blanks = defaultdict(int)
    for i in range(n):
        for j in range(n):
            if not game_board[i][j]:  # 빈칸이라면
                game_board[i][j] = -1
                blanks[tuple(bfs(game_board, i, j, 0))] += 1
    # print(blanks)

    # 회전시켜 blanks 맞추기
    for _ in range(4):
        table = rotate(table)
        rotated_table = copy.deepcopy(table)

        for i in range(n):
            for j in range(n):
                if rotated_table[i][j] == 1:  # 퍼즐조각이라면
                    rotated_table[i][j] = -1  # 퍼즐조각을 일단 제외시킴
                    block = tuple(bfs(rotated_table, i, j, 1))  # 퍼즐조각을 일단 제외시킴
                    if block in blanks:
                        answer += len(block)
                        blanks[block] -= 1  # 빈칸을 지움
                        if not blanks[block]:  # 만약 특정 모양의 빈칸의 개수가 0개라면 지우기
                            del blanks[block]
                        table = copy.deepcopy(
                            rotated_table
                        )  # 퍼즐을 하나 썼으니, 다음 회전때 반영시키기 위함
                    else:
                        rotated_table = copy.deepcopy(table)  # 퍼즐을 안썼으니, 다시 채워 넣기

    return answer
