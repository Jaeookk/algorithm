# https://softeer.ai/practice/info.do?idx=1&eid=584
<<<<<<< HEAD
import sys

if __name__ == "__main__":
    input = sys.stdin.readline

    n, m = map(int, input().split())
    limit = [0] * 101
    answer = 0

    now = 1
    for _ in range(n):
        a, b = map(int, input().split())  # 구간, 제한속도
        for i in range(now, now + a):
            limit[i] = b
        now += a

    now = 1
    for _ in range(m):
        a, b = map(int, input().split())  # 운행길이, 속도
        for j in range(now, now + a):
            answer = max(answer, b - limit[j])
        now += a

    print(answer)
=======
>>>>>>> 574e77ee67793f6b6bcd6f59386393c527066173
