# https://school.programmers.co.kr/learn/courses/30/lessons/118667#
from collections import deque

def solution(queue1, queue2):
    answer = 0
    sum_1 = sum(queue1)
    sum_2 = sum(queue2)
    target = (sum_1 + sum_2) // 2
    q1 = deque(queue1)
    q2 = deque(queue2)
    
    cnt = 0
    while cnt < len(queue1)*4:
        if sum_1 < sum_2:
            tmp = q2.popleft()
            sum_1 += tmp
            sum_2 -= tmp
            q1.append(tmp)
            answer+=1
            cnt +=1
        elif sum_1 > sum_2:
            tmp = q1.popleft()
            sum_2 += tmp
            sum_1 -= tmp
            q2.append(tmp)
            answer += 1
            cnt += 1
        else:
            return answer
    return -1
