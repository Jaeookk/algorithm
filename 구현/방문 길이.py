# https://school.programmers.co.kr/learn/courses/30/lessons/49994
def solution(dirs):
    temp = []
    x,y = 0,0
    move = {'U':(0,1), 'D':(0,-1), 'L':(-1,0), 'R':(1,0)}
    
    for i in dirs:
        nx = x + move[i][0]
        ny = y + move[i][1]
        if abs(nx) > 5 or abs(ny) > 5:
            continue
        temp.append((x,y,nx,ny))
        temp.append((nx,ny,x,y))
        x , y = nx, ny
    temp = set(temp)
        
    return len(temp)//2
