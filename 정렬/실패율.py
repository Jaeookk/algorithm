# https://school.programmers.co.kr/learn/courses/30/lessons/42889
def solution(N, stages):
    answer = []
    rate=[]
    stage_info = [0]*(N+2)  
    
    for stage in stages: # 각 스테이지에 있는 유저의 수
        stage_info[stage] += 1 
        
    for i in range(N):
        not_clear = stage_info[i+1]
        each_stage_user = sum(stage_info[i+1:]) # 스테이지를 클리어한 유저 수
        if each_stage_user == 0:
            rate.append((i+1,0))
        else:
            rate.append((i+1, not_clear/each_stage_user))
            
    answer = list(map(lambda x: x[0], sorted(rate, key=lambda x:x[1], reverse=True)))
    
    return answer
