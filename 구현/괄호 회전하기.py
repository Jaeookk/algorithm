# https://school.programmers.co.kr/learn/courses/30/lessons/76502
def check(s):
    dic = {"}":"{", ")":"(", "]":"["}
    stack = []
    for i in s:
        if i in dic.keys():
            if not stack:
                return False
            if dic[i] == stack[-1]:
                stack.pop()
        else:
            stack.append(i)
    if stack: return False
    else: return True
            
def solution(s):
    answer = 0
    for i in range(len(s)):
        if check(s[i:]+s[:i]) == True:
            answer += 1
        
    return answer
