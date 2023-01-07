# https://school.programmers.co.kr/learn/courses/30/lessons/150369
def solution(cap, n, deliveries, pickups):
    answer = 0
    
    while deliveries or pickups: # 모든 집의 배송/회수가 완료 될 때까지
        if deliveries and deliveries[-1] == 0: # 해당 집에 배송할 택배가 0개이면 제외
            deliveries.pop() 
            continue
            
        if pickups and pickups[-1] == 0: # 해당 집에 회수할 택배가 0개이면 제외
            pickups.pop()
            continue
            
        answer += max(len(deliveries)*2, len(pickups)*2)  # 가장 먼 집 길이구해서 더하기
        
        box = 0 # box 변수가 현재까지 담은 택배의 개수를 의미하기 때문에 cap을 넘지 않을 때 까지 택배를 계속 담을 수 있다.
        while deliveries and box <= cap:
            if deliveries[-1] + box <= cap:
                box += deliveries[-1]
            else: # 배송해야할 택배가 트럭 용량보다 클 경우
                deliveries[-1] -= cap-box
                break
            deliveries.pop()
        
        box = 0
        while pickups and box <= cap:
            if pickups[-1] + box <= cap:
                box += pickups[-1]
            else:
                pickups[-1] -= cap-box
                break
            pickups.pop() 
                 
            
    return answer
