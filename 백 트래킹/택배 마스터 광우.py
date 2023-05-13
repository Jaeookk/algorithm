# 소프티어 레벨3
# 순열(permutations)를 백트래킹으로 직접 구현

import sys
from itertools import permutations


def my_permutations(level):
    if level == n:
        perm_result.append(tmp[:])  # tmp[:] 안하면 tmp가 바뀔대마다 perm_result에 들어가있는 것도 계속 바뀜...
        return

    for i in range(n):
        if not check[i]:
            check[i] = True
            tmp.append(rails[i])
            my_permutations(level + 1)
            check[i] = False
            tmp.pop()


input = sys.stdin.readline
n, m, k = map(int, input().split())
rails = list(map(int, input().split()))

result = sys.maxsize
# rail_perm = permutations(rails, n)
tmp = []
perm_result = []
check = [False] * n

my_permutations(0)

for possible in perm_result:
    rail = list(possible)

    i = 0
    bucket = 0
    work = 0
    count = 0

    while work != k:  # 작업의 수만큼만 반복
        if bucket + rail[i] <= m:  # m: 바구니 무게
            bucket += rail[i]
            rail.append(rail[i])
            i += 1
        else:
            count += bucket
            bucket = 0
            work += 1

    result = min(result, count)

print(result)

# import sys
# from itertools import permutations


# input = sys.stdin.readline

# n, m, k = map(int, input().split())
# rails = list(map(int, input().split()))

# rail_perm = permutations(rails, n)

# tmp = []
# perm_test = []
# check = [False] * n


# def my_permutations(level):
#     if level == n:
#         perm_test.append(tmp)
#         return
#     for i in range(n):
#         if not check[i]:
#             check[i] = True
#             tmp.append(rails[i])
#             my_permutations(level + 1)
#             check[i] = False
#             tmp.pop()


# result = sys.maxsize

# for possible in rail_perm:
#     rails = list(possible)

#     i = 0
#     bucket = 0
#     work = 0
#     count = 0

#     while work != k:  # 작업의 수만큼만 반복
#         if bucket + rails[i] <= m:  # m: 바구니 무게
#             bucket += rails[i]
#             rails.append(rails[i])
#             i += 1
#         else:
#             count += bucket
#             bucket = 0
#             work += 1

#     result = min(result, count)

# print(result)
