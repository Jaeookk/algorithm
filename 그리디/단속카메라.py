# https://school.programmers.co.kr/learn/courses/30/lessons/42884

# 처음 틀린 코드
# def solution(routes):
#     answer = 0
#     routes.sort(key=lambda x: x[0])
#     camera = 30000
#     for start, end in routes:
#         if start >= camera:
#             answer += 1
#             camera = end
#         camera = min(camera, end)
#     return answer


def solution(routes):
    answer = 0
    routes.sort(key=lambda x: x[0])
    camera = 30000
    for start, end in routes:
        if start > camera:
            answer += 1
            camera = end
        camera = min(camera, end)
    return answer + 1


print(solution([[-2, -1], [1, 2], [-3, 0]]))  # 2
print(solution([[0, 0]]))  # 1
print(solution([[0, 1], [0, 1], [1, 2]]))  # 1
print(solution([[0, 1], [2, 3], [4, 5], [6, 7]]))  # 4
print(solution([[-20, -15], [-14, -5], [-18, -13], [-5, -3]]))  # 2
print(solution([[-20, 15], [-14, -5], [-18, -13], [-5, -3]]))  # 2
print(solution([[-20, 15], [-20, -15], [-14, -5], [-18, -13], [-5, -3]]))  # 2
