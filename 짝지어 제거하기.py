def solution(s):
    tmp = [s[0]]
    
    for i in range(1, len(s)):
        if not tmp:
            tmp.append(s[i])
            continue
        if tmp[-1] != s[i]:
            tmp.append(s[i])
        else:
            tmp.pop()
    if tmp:
        return 0
    return 1
