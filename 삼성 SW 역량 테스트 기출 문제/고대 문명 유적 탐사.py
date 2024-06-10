import sys
import copy
import time
from collections import deque


def rotate_90(matrix):
    return [list(row) for row in zip(*matrix[::-1])]


def extract_and_rotate_submatrix(matrix, center_row, center_col, degree):
    # 3x3 부분 배열 선택
    submatrix = [row[center_col - 1 : center_col + 2] for row in matrix[center_row - 1 : center_row + 2]]
    if degree == 90:
        return rotate_90(submatrix)
    elif degree == 180:
        return rotate_90(rotate_90(submatrix))
    elif degree == 270:
        return rotate_90(rotate_90(rotate_90(submatrix)))
    return submatrix


def apply_submatrix(matrix, submatrix, center_row, center_col):
    for i in range(3):
        for j in range(3):
            matrix[center_row - 1 + i][center_col - 1 + j] = submatrix[i][j]


def bfs(row, col, matrix, visited):
    queue = deque([(row, col)])
    visited[row][col] = True
    value = matrix[row][col]
    loc = [(row, col)]

    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    while queue:
        x, y = queue.popleft()
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < 5 and 0 <= ny < 5 and not visited[nx][ny] and matrix[nx][ny] == value:
                queue.append((nx, ny))
                visited[nx][ny] = True
                loc.append((nx, ny))

    return loc if len(loc) >= 3 else []


def get_treasure(matrix, location, treasure):
    global turn_score

    location.sort(key=lambda x: (x[1], -x[0]))
    turn_score += len(location)
    for row, col in location:
        matrix[row][col] = treasure.pop(0)


def solution():
    global graph, treasure, turn_score

    # 3x3 격자 선택
    best_score = -1
    best_graph = None
    best_rotation = (0, 0, 0)

    for col in range(1, 4):
        for row in range(1, 4):
            for degree in [90, 180, 270]:  # 90, 180, 270도 회전
                temp_graph = [row[:] for row in graph]
                submatrix = extract_and_rotate_submatrix(temp_graph, row, col, degree)
                apply_submatrix(temp_graph, submatrix, row, col)

                visited = [[False] * 5 for _ in range(5)]
                current_score = 0

                for i in range(5):
                    for j in range(5):
                        if not visited[i][j]:
                            bfs_result = bfs(i, j, temp_graph, visited)
                            current_score += len(bfs_result)

                if current_score > best_score:
                    best_score = current_score
                    best_graph = [row[:] for row in temp_graph]
                    best_rotation = (row, col, degree)
                elif current_score == best_score and degree < best_rotation[2]:
                    best_score = current_score
                    best_graph = [row[:] for row in temp_graph]
                    best_rotation = (row, col, degree)

    if best_score == 0:
        return False

    # 유물 1차획득
    # TODO : 상하좌우로 인접한 같은 종류의 유물 조각(3개이상)을 어떻게 사라지게 할 것 인가.

    # 우선 best_rotation에 따라 그래프를 회전시키자.
    row, col, degree = best_rotation
    submatrix = extract_and_rotate_submatrix(graph, row, col, degree)
    apply_submatrix(graph, submatrix, row, col)

    # 상하좌우로 인접한 같은 종류의 유물 조각의 위치들을 파악
    visited = [[False] * 5 for _ in range(5)]
    loc = []
    for i in range(5):
        for j in range(5):
            if not visited[i][j]:
                result = bfs(i, j, graph, visited)
                loc.extend(result)

    # 유물의 가치를 카운트하고, 유적의 벽면에 써져있는 숫자로 교체.
    get_treasure(graph, loc, treasure)

    # 유물 연쇄 획득
    while True:
        visited = [[False] * 5 for _ in range(5)]
        loc = []
        for i in range(5):
            for j in range(5):
                if not visited[i][j]:
                    result = bfs(i, j, graph, visited)
                    loc.extend(result)

        if not loc:
            break

        get_treasure(graph, loc, treasure)

    return True


input = sys.stdin.readline
K, M = map(int, input().split())  # 각각 [탐사 반복 횟수, 유물 조각의 개수]
graph = [list(map(int, input().split())) for i in range(5)]
treasure = list(map(int, input().split()))  # 벽면에 적힌 유물 조각
turn_results = []

for _ in range(K):
    turn_score = 0
    if not solution():
        break
    turn_results.append(turn_score)

print(" ".join(map(str, turn_results)))
