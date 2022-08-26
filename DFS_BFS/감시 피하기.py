import sys
f = sys.stdin.readline

n = int(f())

graph = []
teacher = 0
for _ in range(n):
    graph.append(list(f().split()))
    teacher += graph[-1].count('T')

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def check(x, y):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        while nx >= 0 and nx < n and ny >= 0 and ny < n and graph[nx][ny] != 'O':
            if graph[nx][ny] == 'S':
                return True # 학생 찾기 가능
            else:
                nx += dx[i]
                ny += dy[i]
    return False # 학생 찾기 불가능
    
def dfs(count):
    global result
    if count == 3:
        cnt = 0
        for i in range(n):
            for j in range(n):                 
                if graph[i][j] == 'T':
                    if not check(i,j):          
                        cnt+=1
        # 모든 선생님이 감시가 불가능할 때
        if cnt == teacher:
              result = True
        return
    
    for i in range(n):
        for j in range(n):
            if graph[i][j] == 'X':
                graph[i][j] = 'O'
                count += 1
                dfs(count)
                graph[i][j] = 'X'
                count -= 1

result = False
dfs(0)
if result:
    print('YES')
else:
    print('NO')
