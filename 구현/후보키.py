# https://school.programmers.co.kr/learn/courses/30/lessons/42890
from itertools import combinations

def solution(relation):
    answer = 0
    col = len(relation[0])
    combination = [] # 가능한 후보 키 조합 구해놓기
    
    for c in range(1,col+1): 
        combination.extend(list(combinations(range(col),c)))
    
    Candidate_Key = []
    
    for possible_keys in combination: # 가능한 후보 키 하나씩 검증
        result = []
        for r in range(len(relation)):
            temp = ""
            for c in possible_keys:
                temp += relation[r][c]
            result.append(temp)
            
        if len(result) == len(set(result)): # 유일성 검증
            for keys in Candidate_Key: # 최소성 검증
                cnt = 0
                for k in keys:
                    if k in possible_keys:
                        cnt += 1
                if cnt == len(keys):
                    break
            else:
                answer += 1
                Candidate_Key.append(possible_keys) # 유일성, 최소성 통과한 키를 후보키에 보관.
        
    return answer
