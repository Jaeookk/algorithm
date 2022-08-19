from collections import deque


def solution(rectangle, characterX, characterY, itemX, itemY):
    answer = 0
    MAX = 102  # 맵을 두배로 늘리기 때문에 최대 100까지 맵을 만들어야함
    # 테두리 그리기
    # 테두리는 1, 내부는 0으로 표시
    # 테두리와 내부가 겹칠경우 0으로 표시
    field = [[5] * MAX for _ in range(MAX)]  # 5는 맨처음 땅
    for rec in rectangle:
        x1, y1, x2, y2 = map(lambda x: x * 2, rec)
        for i in range(x1, x2 + 1):
            for j in range(y1, y2 + 1):
                if x1 < i < x2 and y1 < j < y2:  # 내부일 때
                    field[i][j] = 0
                elif field[i][j] != 0:  # 테두리일 때 그리고 이미 내부가 아닐 때
                    field[i][j] = 1  # 테두리랑 내부랑 겹치면 그건 내부

    # 길 찾기 (최단거리는 BFS)
    q = deque()
    q.append([characterX * 2, characterY * 2])
    visited = [[-1] * MAX for _ in range(MAX)]
    visited[characterX * 2][characterY * 2] = 0
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    while q:
        x, y = q.popleft()
        if x == itemX * 2 and y == itemY * 2:
            answer = visited[x][y] // 2
            break
            
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if visited[nx][ny] == -1 and field[nx][ny] == 1: # 처음 방문 & 테두리라면
                q.append([nx, ny])
                visited[nx][ny] = visited[x][y] + 1

    return answer
