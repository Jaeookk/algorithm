# https://school.programmers.co.kr/learn/courses/30/lessons/12936#

from math import factorial

def solution(n, k):
    answer = []
    arr = [i for i in range(1, n+1)]
    
    for i in range(n-1,0,-1):
        idx = (k-1) // factorial(i)
        answer.append(arr.pop(idx))
        k -= idx*factorial(i)
    answer.extend(arr)

    return answer
