# 백준 18869 골드4

from collections import defaultdict


m, n = map(int, input().split())

universes = defaultdict(int)

for i in range(m):
    universe = list(map(int, input().split()))
    tmp = sorted(set(universe))  # 중복 제거 후 정렬
    k = {tmp[i]: i for i in range(len(tmp))}  # 행성 : 인덱스 형태로 저장(오름차순)
    s = ""
    for x in universe:
        s += str(k[x])
    universes[s] += 1

print(universes)
print(sum(list(map(lambda x: x * (x - 1) // 2, universes.values()))))  # 구성이 같은데 순서만 다른 우주의 쌍은 한 번만 센다.
