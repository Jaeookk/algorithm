# https://school.programmers.co.kr/learn/courses/30/lessons/49993
def solution(skill, skill_trees):
    answer = 0
    for s in skill_trees:
        idx = 0
        for i in s:
            if i in skill:
                if i == skill[idx]:
                    idx += 1
                else:
                    break
        else:
            answer += 1
            
                
    return answer
