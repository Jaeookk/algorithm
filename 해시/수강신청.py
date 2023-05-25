# 백준 13414 실버3

import sys


if __name__ == "__main__":
    input = sys.stdin.readline

    K, L = map(int, input().split())
    check = {}
    for i in range(L):
        x = input().rstrip()
        if x in check:  # O(1)
            check.pop(x)  # O(1)
        check[x] = i

    result = list(check.items())
    cnt = 0
    for idx in range(len(result)):
        if cnt == K:
            break
        print(result[idx][0])
        cnt += 1
