# https://school.programmers.co.kr/learn/courses/30/lessons/43105

def solution(triangle):
    answer = 0
    dp = []
    for i in range(1,len(triangle)):
        for j in range(len(triangle[i])):
            if j==0:
                triangle[i][j] = triangle[i-1][j] + triangle[i][j]
            elif j == len(triangle[i])-1:
                triangle[i][j] = triangle[i-1][j-1] + triangle[i][j] 
            else: 
                triangle[i][j] = max(triangle[i-1][j-1], triangle[i-1][j]) + triangle[i][j]
            
    return max(triangle[-1])
