# https://school.programmers.co.kr/learn/courses/30/lessons/131701
def solution(elements):
    answer = 0
    arr = elements*2
    L = len(elements)
    result = []
    for length in range(1,L+1):
        for start in range(L):
            result.append(sum(arr[start:start+length]))
    
    return len(set(result))
