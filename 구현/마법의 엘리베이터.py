# https://school.programmers.co.kr/learn/courses/30/lessons/148653#
def solution(storey):
    answer = 0
    
    while storey != 0:
        x = storey % 10
        if x < 5:
            answer += x
            storey -= x
        elif x == 5:  # 오른쪽 자리 수가 5일때는 그 왼쪽 자리 수가 4이하일때와 아닐때에 따라서 최소값이 다름.
            # ex) 45일때 45->50->0 은 10개이지만, 45->40->0은 9개이다.
            y = storey//10%10
            if y < 5:
                answer += x
                storey -= x
            else:
                answer += 10-x
                storey += 10-x
        else:
            answer += 10-x
            storey += 10-x
        storey //= 10
            
    return answer
