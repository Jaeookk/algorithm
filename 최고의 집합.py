# https://school.programmers.co.kr/learn/courses/30/lessons/12938
def solution(n, s):
    answer = []
    if s // n == 0:
        return [-1]
    
    while n >= 1:
        answer.append(s // n)
        s -= s // n
        n -= 1
    return answer
