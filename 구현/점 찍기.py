# https://school.programmers.co.kr/learn/courses/30/lessons/140107
def solution(k, d):
    answer = 0
    x, y = 0, d//k*k
    
    while x <= d//k * k:
        if x**2 + y**2 <= d**2:
            answer += y//k + 1
            x += k
        else:
            y -= k
        
    return answer
