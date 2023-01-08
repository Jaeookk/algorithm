# https://school.programmers.co.kr/learn/courses/30/lessons/150368
from itertools import product

def solution(users, emoticons):
    answer = [0,0]
    discounts = [10, 20, 30, 40]
    products = list(product(discounts, repeat = len(emoticons)))
    
    for p in products:
        result = [0,0]
        for user in users:
            sum = 0
            for i in range(len(emoticons)):
                if p[i] >= user[0]:
                    sum += emoticons[i]*(1-p[i]/100)
            if sum >= user[1]:
                result[0] += 1
            else:
                result[1] += sum
        answer = max(answer, result)
                
    return answer
