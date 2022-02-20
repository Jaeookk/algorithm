def solution(dartResult):
    answer = 0
    result = []
    for i in range(len(dartResult)):
        a = dartResult[i]
        if a == '0' and dartResult[i-1]=='1':
            continue
        if a.isnumeric():
            if dartResult[i+1] == '0':
                result.append(10)
                i += 1
            else:
                result.append(int(a))
                continue
        if a == 'D':
            result[-1] = result[-1]**2
        elif a == 'T':
            result[-1] = result[-1]**3
        elif a == '*':
            if len(result) > 1:
                result[-2] = result[-2]*2
                result[-1] = result[-1]*2
            else:
                result[-1] = result[-1]*2
        elif a == '#':
            result[-1] = result[-1]*(-1)
    answer = sum(result)
            
    return answer
