# https://school.programmers.co.kr/learn/courses/30/lessons/169198?language=python3
def solution(m, n, startX, startY, balls):
    answer = []
    # 선대칭과 점대칭을 이용
    # 목표 공이 벽에 안 붙어 있는 경우 -> 최소 거리를 위한 시작 공 위치(-startX, startY) or (startX, -startY)
    # 목표 공이 벽에 붙어 있는 경우 -> (startX + (m - startX) * 2, startY) or (startX, startY + (n - startY) * 2)
    targets = [(-startX, startY), (startX, 2 * n - startY), (2 * m - startX, startY), (startX, -startY)]
    for ball in balls:
        new_targets = [targets[0], targets[1], targets[2], targets[3]]
        if startX == ball[0]:
            new_targets = (
                [targets[0], targets[1], targets[2]] if startY > ball[1] else [targets[0], targets[3], targets[2]]
            )
        if startY == ball[1]:
            new_targets = (
                [targets[1], targets[2], targets[3]] if startX > ball[0] else [targets[0], targets[1], targets[3]]
            )
        answer.append(
            min(list(map(lambda target: (ball[0] - target[0]) ** 2 + (ball[1] - target[1]) ** 2, new_targets)))
        )
    return answer
