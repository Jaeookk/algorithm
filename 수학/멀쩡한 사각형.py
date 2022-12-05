# https://school.programmers.co.kr/learn/courses/30/lessons/62048#
def solution(w,h):
    answer = 0 
    if w == 1 or h == 1:
        return 0
    elif w==h:
        return w*h-w
    
    for i in range(w):
        answer += int(h*i/w)*2 # 원래 h/w*i 순서로 했는데 에러가 났다.. 나눗셈이 정확하지 않을때가 있나봄..
        
    return answer
