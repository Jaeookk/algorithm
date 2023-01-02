# https://school.programmers.co.kr/learn/courses/30/lessons/148652
def solution(n, l, r):
    answer = r-l+1 # 구간 길이를 구하고 0인 경우를 제외시키자.
    
    for x in range(l-1,r):
        while x>=1:
            a = x//5
            b = x%5
            if a==2 or b==2: # 0인 경우. 0은 
                answer -= 1
                break
            x = a
            
    return answer
