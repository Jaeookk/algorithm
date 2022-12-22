# https://school.programmers.co.kr/learn/courses/30/lessons/147354
def solution(data, col, row_begin, row_end):
    answer = 0
    data = sorted(data, key = lambda x: (x[col-1], -x[0]))
    result = []
    
    for i in range(row_begin, row_end+1):
        tmp = 0
        for x in data[i-1]:
            tmp += x % i
        result.append(tmp)
    
    for s in result:
        answer = answer^s
        
    return answer
