# https://school.programmers.co.kr/learn/courses/30/lessons/68645
# n=4일때               n = 5일때
# 1  0  0  0           1  0  0  0  0
# 2  9  0  0           2  12 0  0  0
# 3  10 8  0           3  13 11 0  0
# 4  5  6  7           4  14 15 10 0
#                      5  6  7  8  9

# 1. n만큼 방향을 바꾼다. 이때 방향은 총 3방향이 존재한다. 
#    ex) n=4일때 아래, 오른쪽, 위, 아래 순으로 바뀜
# 2. 방향을 바꿀때까지 걸리는 횟수는 1회씩 작아진다.
#    ex) n=4일때 4,7,9일때 바뀌고, n=5일때 5,9,12,14에서 바뀌는 식.

def solution(n):
    answer = []
    array = [[0]*n for _ in range(n)] # n x n 맵 만들기
    x, y = -1, 0 # 처음엔 무조건 아래로 내려가야 하기 때문에 x=-1
    num = 1
    
    for i in range(n): # 방향 
        for _ in range(i,n): # 좌표구하기
            if i % 3 == 0: # 아래
                x += 1
            elif i % 3 == 1: # 오른쪽
                y += 1
            elif i % 3 == 2: # 위로
                x-=1
                y-=1
            array[x][y] = num
            num += 1
    for i in array:
        for j in i:
            if j:
                answer.append(j)
    
    return answer
