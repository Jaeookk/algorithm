# https://school.programmers.co.kr/learn/courses/30/lessons/131704
def solution(order):
    temp = []
    idx = 0
    belt = 1
    while belt <= len(order):
        temp.append(belt)
        while temp[-1] == order[idx]:
            idx += 1
            temp.pop()
            if len(temp) == 0:
                break
        belt += 1
            
            
    return idx
