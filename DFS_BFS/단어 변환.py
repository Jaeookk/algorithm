# https://school.programmers.co.kr/learn/courses/30/lessons/43163
from collections import deque

def solution(begin, target, words):
    answer = 0
    queue = deque()
    queue.append((begin,0))
    visited = [False] * len(words)
    while queue:
        w, cnt = queue.popleft()
        if w == target:
            return cnt
        
        for idx, word in enumerate(words):
            not_equal = 0
            for i in range(len(word)):
                if w[i] != word[i]:
                    not_equal += 1
            if not_equal == 1 and visited[idx] == False:
                queue.append((word,cnt+1))
                visited[idx] = True
    return 0
