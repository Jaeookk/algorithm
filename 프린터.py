from collections import deque

def solution(priorities, location):
    answer = 0
    q = deque(priorities)
    cnt=0
    j=0
    while q:     
        if q[0] != max(q):
            q.append(q.popleft())
            if location==0:
                location = len(q)-1
            elif location!=0:
                location-=1
            continue
        elif q[0] == max(q):
            q.popleft()
            cnt +=1
            if location == 0:
                return cnt
            else: location -=1
