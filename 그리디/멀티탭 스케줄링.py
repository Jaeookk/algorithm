import sys

input = sys.stdin.readline
N, K = map(int, input().split())
use = list(map(int, input().split()))

plugs = []
result = 0
for i in range(K):
    # 이미 플러그에 꽂혀있다면
    if use[i] in plugs:
        continue

    # 플러그에 빈공간이 있다면
    if len(plugs) != N:
        plugs.append(use[i])
        continue

    # 가장 멀리 있는 플러그의 인덱스
    far_one = 0
    temp = 0

    # 현재 꽂혀있는 플러그들 확인
    for plug in plugs:
        # 플러그에 꽂힌 것이 앞으로 사용할 계획에 없으면
        if plug not in use[i:]:
            temp = plug
            break

        # 현재까지 가장 멀리 있는 플러그보다 멀리 있으면
        elif use[i:].index(plug) > far_one:
            far_one = use[i:].index(plug)
            temp = plug

    plugs[plugs.index(temp)] = use[i]
    result += 1

print(result)

# 1. 사용할 플러그가 이미 꽂혀있다면 continue
# 2. 플러그를 꽂을 자리가 있다면 append 해주고 continue
# 3. 다른 플러그를 뽑아야 하는 상황이라면
#     - 꽂혀 있는 플러그를 하나씩 확인한다.
#     - 해당 플러그가 추후 사용해야할 플러그중에 없으면 그자리를 현재 사용할 플러그로 업데이트
#     - 만약 전부 추후 사용해야할 플러그라면 가장 마지막에 사용할 플러그의 인덱스를 구해서 현재 사용할 플러그로 업데이트
#     - result += 1
# 4. result 출력
