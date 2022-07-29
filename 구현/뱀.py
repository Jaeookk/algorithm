n = int(input())
k = int(input())

# 보드
Map = [[0]*n for _ in range(n)]
for _ in range(k):
    a, b = map(int, input().split())
    Map[a-1][b-1] = 1 # 사과 : 1, 빈칸 : 0
    
# 방향전환
info = []
l = int(input())
for _ in range(l):
    a, b = input().split()
    info.append((a,b))

# 동,남,서,북
dx = [0,1,0,-1] # 행
dy = [1,0,-1,0] # 열

    
def solution():
    x, y = 0, 0  # 현재 뱀의 머리 위치
    Map[x][y] = 2 # 뱀이 있으면 : 2
    rotate_info = 0
    body = [(0,0)] # 뱀의 전체 위치
    time = 0
    indices = 0
    while True:
        if indices < l and time == int(info[indices][0]):
            if info[indices][1] == 'L':
                rotate_info -= 1
                rotate_info %= 4
            elif info[indices][1] == 'D':
                rotate_info += 1
                rotate_info %= 4
            indices += 1
        time += 1
        nx = x + dx[rotate_info]
        ny = y + dy[rotate_info]
        if nx >= 0 and nx <= n-1 and ny >= 0 and ny <= n-1:
            # 사과가 있을 경우
            if Map[nx][ny] == 1:
                Map[nx][ny] = 2
                body.append((nx, ny))
                x, y = nx, ny
            # 사과가 없을 경우
            elif Map[nx][ny] == 0:
                Map[nx][ny] = 2
                body.append((nx,ny))
                a, b = body.pop(0)
                Map[a][b] = 0
                x , y = nx, ny
            # 꼬리가 있을 경우
            elif Map[nx][ny] == 2:
                return time
        else:
            return time
        
print(solution())
