# 백준 1456 골드5

import sys


if __name__ == "__main__":
    input = sys.stdin.readline

    m, n = map(int, sys.stdin.readline().split())

    check = [True] * (int(n**0.5) + 1)
    check[1] = False

    for i in range(2, int(n**0.5) + 1):
        if check[i]:
            if i * i > int(n**0.5):
                break
            for j in range(i**2, int(n**0.5) + 1, i):
                check[j] = False

    count = 0
    for i in range(1, len(check)):
        if check[i]:
            res = i * i
            while True:
                if res < m:
                    res *= i
                    continue
                if res > n:
                    break
                res *= i
                count += 1

    print(count)
