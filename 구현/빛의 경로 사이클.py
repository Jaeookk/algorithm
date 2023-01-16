# https://school.programmers.co.kr/learn/courses/30/lessons/86052

def solution(grid):
    answer = []
    R, C = len(grid), len(grid[0])
    dr, dc = (1,0,-1,0), (0,-1,0,1) # 아래, 왼쪽, 위, 오른쪽
    # (r,c) 격자로 빛이 들어올때 (아래,왼쪽,위,오른쪽) 중 어디서 들어왔는지 파악하기 위한 배열
    visited = [[[0,0,0,0] for _ in range(C)] for _ in range(R)]
    
    # 모든 좌표에 대해서 조사
    for r in range(R):
        for c in range(C):
            for dir in range(4): # 각 좌표마다 4 방향 탐색
                if visited[r][c][dir] == 0:  # 해당 좌표로 향한 방향이 없다면       
                    cnt = 0
                    while not visited[r][c][dir]:
                        visited[r][c][dir] = 1
                        if grid[r][c] == "L": dir = (dir-1) % 4 # 반시계방향
                        elif grid[r][c] == "R": dir = (dir+1) % 4 # 시계방향
                        # 그리드를 넘어가면 안되므로 나머지를 이용해서 처음으로 돌아가게 함.
                        r, c = (r + dr[dir]) % R, (c + dc[dir]) % C
                        cnt += 1
                    answer.append(cnt)

    return sorted(answer)
