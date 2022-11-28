# https://school.programmers.co.kr/learn/courses/30/lessons/12936#

from math import factorial

def solution(n, k):
    answer = []
    arr = [i for i in range(1, n+1)]
    
    for i in range(n-1,0,-1):
        q = (k - 1) // factorial(i)
        idx = q % len(arr)

        answer.append(arr.pop(idx))

    answer.extend(arr)

    return answer
