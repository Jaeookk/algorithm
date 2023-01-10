# https://school.programmers.co.kr/learn/courses/30/lessons/147355
def solution(t, p):
    answer = 0
    L = len(p)
    for i in range(len(t)-L+1):
        if int(t[i:i+L]) <= int(p):
            answer += 1
    return answer
