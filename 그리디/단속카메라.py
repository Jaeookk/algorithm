# https://school.programmers.co.kr/learn/courses/30/lessons/42884

# 가장 간단한 코드
# def solution(routes):
#     routes.sort(key=lambda x: x[0])
#     a = 1
#     m = 30_000
#     for i, j in routes:
#         if i > m:
#             a += 1
#             m = j
#         m = min(m, j)
#     return a
