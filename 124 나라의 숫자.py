def solution(n):
    answer = ''
    result = []
    
    while n:
        x = n % 3
        if x == 0:
            x = 3
            n -= 1
        result.append(x)
        n //= 3
    
    result.reverse()

    for i in result:
        if i == 3:
            answer += "4"
        else:
            answer+=str(i)
            
    return answer
