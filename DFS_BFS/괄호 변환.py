# 이 문제는 DFS 문제는 아니지만, DFS 알고리즘의 핵심이 되는 재귀 함수 구현을 요구한다는 점에서 DFS 연습 목적의 문제로 DFS/BFS 파트에서 다룬다

def seperation(p):
    u, v = '', ''
    cnt = 0
    for indices, i in enumerate(p):
        if not u:
            u += i
            cnt += 1
            continue
        if i == u[0]:
            u += i
            cnt += 1
        else:
            u += i
            cnt -= 1
        if cnt == 0:
            v += p[indices+1:]
            break
    return u,v

def isright(u):
    if u[0] == ')': return 0
    stack = []
    for indices, i in enumerate(u):
        if i == '(': stack.append(i)
        elif i == ')' and not stack: return 0
        else : stack.pop()
        
        if not stack and indices == len(u)-1:
            return 1
    return 0

def solution(p):
    # 1. 입력이 빈 문자열인 경우, 빈 문자열을 반환합니다.
    if not p:
        return ''
    
    # 2. 문자열 w를 두 "균형잡힌 괄호 문자열" u, v로 분리합니다. 단, u는 "균형잡힌 괄호 문자열"로 더 이상 분리할 수 없어야 하며, v는 빈 문자열이 될 수 있습니다. 
    u,v = seperation(p)
    
    # 3. 문자열 u가 "올바른 괄호 문자열" 이라면 문자열 v에 대해 1단계부터 다시 수행합니다. 
    # 3-1. 수행한 결과 문자열을 u에 이어 붙인 후 반환합니다
    if isright(u): return u+solution(v)

    # 4. 문자열 u가 "올바른 괄호 문자열"이 아니라면 아래 과정을 수행합니다. 
    else:
        # 4-1. 빈 문자열에 첫 번째 문자로 '('를 붙입니다. 
        # 4-2. 문자열 v에 대해 1단계부터 재귀적으로 수행한 결과 문자열을 이어 붙입니다. 
        # 4-3. ')'를 다시 붙입니다.
        tmp = '(' + solution(v) + ')'
        
        # 4-4. u의 첫 번째와 마지막 문자를 제거하고, 나머지 문자열의 괄호 방향을 뒤집어서 뒤에 붙입니다. 
        u = u[1:-1]
        for i in u:
            if i == '(' : tmp += ')'
            else: tmp += '('
            
    # 4-5. 생성된 문자열을 반환합니다.
    return tmp
