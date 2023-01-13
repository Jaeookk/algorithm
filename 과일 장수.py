# https://school.programmers.co.kr/learn/courses/30/lessons/135808
def solution(k, m, score):
    answer = 0
    stack = []
    score.sort()
    idx = 0
    while score:
        stack.append(score.pop())
        if len(stack) == m:
            answer += stack[-1]*m
            stack = []
            idx = 0
        idx += 1
        
    return answer
