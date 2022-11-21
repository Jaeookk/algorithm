# https://school.programmers.co.kr/learn/courses/30/lessons/12923
def solution(begin, end):
    answer = []
    
    # 각 도로의 숫자 블록 값은 약수 중 자기 자신을 제외한 가장 큰 값
    # 근데 만약 그 값이 1e7을 넘는다? 그럼 그 것 보다 작은 값을 다시 찾는다.
    for i in range(begin, end+1):
        flag = False
        if i == 1:
            answer.append(0)
            continue

        for j in range(2,int(i**0.5)+1):
            if i%j == 0:
                if i // j <= 1e7:
                    answer.append(i//j)
                    break
                else:
                    continue
        else:
            answer.append(1)
        
    return answer
