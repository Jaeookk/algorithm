# https://school.programmers.co.kr/learn/courses/30/lessons/132265#
from collections import Counter

def solution(topping):
    cheolsu=Counter(topping)
    brother=set()
    answer=0
    for i in topping:
        cheolsu[i]-=1 # 철수꺼에서 토핑 하나씩 빼기
        brother.add(i) # 뺀거를 동생에게 주기
        
        if cheolsu[i]==0:  # 한 종류의 토핑이 모두 다 빠졌다면
            cheolsu.pop(i) # 제거
            
        if len(cheolsu)==len(brother): # 철수와 동생의 토핑 종류 개수가 같다면
            answer+=1
    
    return answer
