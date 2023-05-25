# 백준 11478 실버3

import sys


if __name__ == "__main__":
    input = sys.stdin.readline

    s = input().rstrip()

    L = len(s)
    check = {}

    for i in range(L):
        for j in range(i, L):
            check[s[i : j + 1]] = 1

    print(len(check))
