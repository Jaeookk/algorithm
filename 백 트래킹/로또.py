# from itertools import permutations, combinations

# while True:
#     k, *s = map(int, input().split())
#     if k == 0:
#         break
#     for x in combinations(s, 6):
#         print(*x)
#     print()


def dfs(start, count):
    if len(array) == 6:
        print(" ".join(map(str, array)))
        return

    for i in range(start, k):
        if s[i] not in array:
            array.append(s[i])
            # print(f"{'--'*count}start : {start} | i : {i}")
            # print(f"{'--'*count}array : {array}")
            # print(f"{'--'*count}overlap : {overlap}")
            dfs(i + 1, count + 1)
            array.pop()


while True:
    k, *s = list(map(int, input().split()))
    if k == 0:
        break
    array = []
    dfs(0, 0)
    print()
