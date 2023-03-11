# https://school.programmers.co.kr/learn/courses/30/lessons/161990
def solution(wallpaper):
    answer = []
    x_min = 1000
    y_min = 1000
    x_max = 0
    y_max = 0
    for x, row in enumerate(wallpaper):
        for y, target in enumerate(row):
            if target == "#":
                x_min = min(x, x_min)
                x_max = max(x, x_max)
                y_min = min(y, y_min)
                y_max = max(y, y_max)

    return [x_min, y_min, x_max + 1, y_max + 1]
