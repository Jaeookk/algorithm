from collections import deque


n, w, L = map(int, input().split())  # n은 트럭의 수, w는 다리의 길이, L은 다리의 최대 하중

trucks = deque(map(int, input().split()))
bridge = []
time = 0
while True:
    if len(trucks) == 0:
        break
    bridge.append(0)
    if len(bridge) > w:
        bridge.pop(0)
    if sum(bridge) + trucks[0] <= L:
        truck = trucks.popleft()
        bridge[-1] = truck
    time += 1

print(time + w)
