from itertools import combinations

n, m = map(int, input().split())

houses, chicken_house = [], []
for row in range(n):
    data = list(map(int, input().split()))
    for col in range(n):
        if data[col] == 1:
            houses.append((row,col))
        elif data[col] == 2:
            chicken_house.append((row,col))
            

def solution():
    result = []
    for chickens in list(combinations(chicken_house, m)): # 치킨집의 각 조합에 대하여
        distance = 0
        # 모든 집에 대하여 각 치킨집과의 최단거리 조사
        for house in houses:
            dis = 1e9
            for chicken in chickens:
                tmp = abs(house[0]-chicken[0])+abs(house[1]-chicken[1])
                dis = min(dis, tmp)
            distance += dis
        result.append(distance)
    return min(result)

print(solution())