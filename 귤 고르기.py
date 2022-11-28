# https://school.programmers.co.kr/learn/courses/30/lessons/138476
def solution(k, tangerine):
    answer = 0
    cnt = [0] * (max(tangerine) + 1)
    for x in tangerine:
        cnt[x] += 1
    cnt.sort(reverse = True)
    
    for i in range(len(cnt)):
        if k <= 0 :
            break
        k -= cnt[i]
        answer += 1

        
    return answer
