# https://school.programmers.co.kr/learn/courses/30/lessons/142086
def solution(s):
    answer = []
    for i in range(len(s)):
        str = s[i]
        for j in range(i-1,-1,-1):
            if s[j] == str:
                answer.append(i-j)
                break
        else:
            answer.append(-1)
        
    return answer
