def DFS(y, x, sum, depth):
    global answer
    if depth == 4:
        answer = max(answer, sum)
        return
    visit[y][x] = 1  # 중복 체크
    for i in range(4):
        yy = y + dy[i]
        xx = x + dx[i]
        if 0 <= yy < n and 0 <= xx < m and visit[yy][xx] == 0:
            DFS(yy, xx, sum + arr[yy][xx], depth + 1)
    visit[y][x] = 0  # 다른 모양의 테트로미노를 확인할 때 잘못된 중복체크를 막기


def T(y, x):
    """
    O X O
      O
    위 그림처럼 X의 위치를 입력 받고 (y,x)
    상,하,좌,우 중 하나만 제외시키고 좌표를 이동시키면, 회전가능한 "ㅗ" 모양의 모든 경우(4가지)를 구할 수 있다.
    """
    global answer
    for k in range(4):
        sum = arr[y][x]
        check = 1
        for i in range(4):
            if i == k: # 상하좌우 중 하나씩 제외시키기.
                continue
            yy = y + dy[i]
            xx = x + dx[i]
            if yy < 0 or xx < 0 or yy >= n or xx >= m: # 범위를 벗어나면
                check = 0
                break
            sum += arr[yy][xx]
        if check:
            answer = max(answer, sum)


if __name__ == "__main__":
    answer = 0
    n, m = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]
    visit = [[0 for _ in range(m)] for _ in range(n)]
    dy = [0, 1, 0, -1]
    dx = [1, 0, -1, 0]
    for i in range(n):
        for j in range(m):
            DFS(i, j, 0, 0)
            T(i, j)
    print(answer)

    # 모든 도형들이 4칸으로 이루어져 있고, 회전 및 대칭이 가능하기 때문에
    # 보드판의 모든 정점에서부터 깊이를 4로 제한한 DFS를 돌릴 수 있다.
    # 즉, 임의의 점에서부터 이미 방문한 점은 방문하지 않고 4칸을 움직여 가장 큰 수들을 밟는 방법이다.
    #
    # 하지만 DFS 전략은 모든 도형이 한 붓 그리기 가 가능한 형태의 도형일 때만 가능하다.
    # "ㅗ" 모양의 블럭의 경우 모든 칸을 방문하려면 반드시 한 번은 뒤로 되돌아가서 이미 방문한 칸을 방문해야 하기 때문에 DFS 로 해결이 불가능하다.
    #
    # 따라서 DFS 전략을 쓰되, "ㅗ" 모양 블럭의 경우를 따로 처리해야 한다.

    # 물론 완전탐색을 사용하여, 가능한 도형의 모양을 미리 정의하고 해도 된다.
