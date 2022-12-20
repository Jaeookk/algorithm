# https://school.programmers.co.kr/learn/courses/30/lessons/131127
from collections import Counter


def solution(want, number, discount):
    answer = 0
    dic = dict(zip(want, number))
    
    for i in range(len(discount)-9):
        if dic == Counter(discount[i:i+10]):
            answer += 1
        
    return answer
