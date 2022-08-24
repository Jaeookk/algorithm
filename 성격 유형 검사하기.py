# https://school.programmers.co.kr/learn/courses/30/lessons/118666
from collections import defaultdict

def solution(survey, choices):
    answer = ''
    personality = [('R','T'),('C','F'),('J','M'),('A','N')]
    result_dict = defaultdict(int)
    for s,c in zip(survey, choices):
        if c < 4:
            result_dict[s[0]] += 4 - c
        else:
            result_dict[s[1]] += c - 4
            
    for i in personality:
        if result_dict[i[0]] >= result_dict[i[1]]: # 값이 같으면 사전순이므로
            answer += i[0]
        else: answer += i[1]
        
    return answer
