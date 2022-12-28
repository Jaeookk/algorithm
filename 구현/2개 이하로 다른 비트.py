# https://school.programmers.co.kr/learn/courses/30/lessons/77885
# 짝수 -> 1더하기
# 홀수 -> 오른쪽에서부터 처음 나오는 0을 1로 바꿔주는 작업 ex) 101 -> 110, 1011 -> 1101
def solution(numbers):
    answer = []
    for num in numbers:
        if num%2 == 0:
            answer.append(num+1)
        else:
            x = list(format(num,'b'))
            for i in range(len(x)-1,-1,-1):
                if x[i] == "0":
                    x[i] = "1"
                    x[i+1] = "0"
                    break
            else:
                x = ["1"] + x
                x[1] = "0"
                
            answer.append(int(''.join(x),2))
    return answer
