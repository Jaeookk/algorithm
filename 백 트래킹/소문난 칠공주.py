def dfs(result, num_Y):
    global visited, answer

    if num_Y >= 4:
        return

    if len(result) == 7:
        result = tuple(sorted(result))
        if result not in answer:
            answer.add(result)
        return

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    for x, y in result:
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx and nx < 5 and 0 <= ny and ny < 5:
                if visited[nx][ny] == False:
                    visited[nx][ny] = True
                    result.append((nx, ny))
                    if graph[nx][ny] == "Y":
                        dfs(result, num_Y + 1)
                    else:
                        dfs(result, num_Y)
                    visited[nx][ny] = False
                    result.pop()


if __name__ == "__main__":
    graph = [list(input()) for _ in range(5)]

    visited = [[False for _ in range(5)] for _ in range(5)]
    result = []
    answer = set()

    for i in range(5):
        for j in range(5):
            visited[i][j] = True
            result.append((i, j))
            if graph[i][j] == "Y":
                dfs(result, 1)
            else:
                dfs(result, 0)
            visited[i][j] = False
            result.pop()

    print(len(answer))
