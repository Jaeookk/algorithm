# https://school.programmers.co.kr/learn/courses/30/lessons/134239
def get_area(a,b,arr):
    sum = 0
    for i in range(a,b):
        sum += (arr[i]+arr[i+1])/2
    return sum

def solution(k, ranges):
    answer = []
    arr = [k]
    cnt = 0
    while k != 1:
        if k % 2 == 0:
            k /= 2
        else:
            k = k*3+1
        cnt += 1
        arr.append(k)
    
    for a,b in ranges:
        b += cnt
        if a>b:
            answer.append(-1.0)
            continue
        answer.append(get_area(a,b,arr))
        
    return answer
