# https://school.programmers.co.kr/learn/courses/30/lessons/12980
def solution(n):
    ans = 1
    while True:
        if n == 1:
            break
        x = n % 2
        if x == 0:
            n = n // 2
        else:
            n = n - 1
            ans += 1
    return ans
