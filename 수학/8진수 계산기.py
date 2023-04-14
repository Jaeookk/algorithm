# https://level.goorm.io/exam/173337/8%EC%A7%84%EC%88%98-%EA%B3%84%EC%82%B0%EA%B8%B0/quiz/1

# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
n = int(input())
x = sum(map(int, input().split()))

s = []
while x >= 8:
    # x를 8로 나눈 몫이 8보다 작아질 때까지 실행
    # 그 과정에서 나머지는 저장 -> 진수의 값이 될것임
    s.append(x % 8)
    x //= 8

s.append(x)  # 8보다 작아진 몫을 저장
s = s[::-1]  # 뒤집기
print("".join(list(map(str, s))))
