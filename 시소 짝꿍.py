# https://school.programmers.co.kr/learn/courses/30/lessons/152996

from collections import defaultdict

def solution(weights):
    answer = 0
    dic = defaultdict(set)
    for i, weight in enumerate(weights):
        dic[weight].add(i)
    for weight in tuple(dic.keys()):
        L = len(dic[weight])
        for a,b,c in ((2,3,4), (3,4,2), (4,2,3)):
            if (tmp := weight * a / b) in dic:
                answer += len(dic[tmp]) * L
            if (tmp := weight * a / c) in dic:
                answer += len(dic[tmp]) * L
        if L > 1:
            answer += L * (L-1) //2
        del dic[weight]
    return answer
