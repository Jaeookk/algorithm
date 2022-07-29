from collections import deque
import sys
f = sys.stdin.readline

# 땅 크기, 인구 차이 [L, R]
n, l, r = map(int, f().split())

# 각 나라의 인구
graph = []
for _ in range(n):
    graph.append(list(map(int, f().split())))


dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(x,y):
    united = [(x,y)] # 연합
    check[x][y] = 1 
    queue = deque()
    queue.append((x, y))
    population = graph[x][y] # 인구수
    while queue:
        a, b = queue.popleft()
        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]
            if 0 <= nx < n and 0 <= ny < n and check[nx][ny] == 0:
                if l <= abs(graph[a][b] - graph[nx][ny]) <= r: # 국경선 열기
                    queue.append((nx, ny))
                    united.append((nx,ny)) # 연합에 추가
                    check[nx][ny] = 1 # 이 나라는 확인했으니 1로 표시
                    population += graph[nx][ny] # 총 인구에 추가

    for i,j in united:
        graph[i][j] = population // len(united)
                
    return

result = 0

# 인구 이동이없을 때까지 지속
while True:
    check = [[0]*n for _ in range(n)] # 각 나라를 확인했는지 체크하기 위한 리스트
    cnt = 0
    for i in range(n):
        for j in range(n):
            if check[i][j] == 0:
                bfs(i,j)
                cnt += 1
    # 더이상 인구 이동이 안일어난다 == 연합이 하나도 없다.
    # --> check 리스트가 모두 0이므로 종료조건으로 사용.
    if cnt == n * n:
        break
    
    result += 1

print(result)
