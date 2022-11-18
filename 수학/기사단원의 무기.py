# https://school.programmers.co.kr/learn/courses/30/lessons/136798
def solution(number, limit, power):
    answer = 0
    
    for i in range(1,number+1):
        cnt = 0
        for j in range(1,int(i**0.5)+1):
            if i % j == 0:
                cnt += 1
                if i // j != j:
                    cnt += 1
        if cnt > limit:
            answer += power
        else:
            answer += cnt
            
        
    return answer
