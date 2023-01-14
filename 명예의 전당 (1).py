# https://school.programmers.co.kr/learn/courses/30/lessons/138477
def solution(k, score):
    answer = []
    for i in range(len(score)):
        tmp = list(sorted(score[:i+1], reverse=True))[:k]
        answer.append(tmp[-1])
            
    return answer
