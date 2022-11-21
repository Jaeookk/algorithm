# https://school.programmers.co.kr/learn/courses/30/lessons/17687
def solution(n, t, m, p):
    result = "0"
    k = {10:"A", 11:"B", 12:"C", 13:"D", 14:"E", 15:"F"}
    
    for i in range(t*m):
        tmp = ""
        while i > 0: # i가 n보다 크거나 같으면
            x = i%n
            if x >= 10: tmp += k[x]
            else: tmp += str(x)
            i //= n
        
        for j in range(len(tmp)-1,-1,-1):
            result += tmp[j]

    return result[p-1:t*m:m]
