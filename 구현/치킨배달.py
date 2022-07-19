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
    for chickens in list(combinations(chicken_house, m)):
        print(chickens)
        distance = 0
        # 치킨집과 각 집들의 거리 구하기
        for house in houses:
            dis = 2*n
            for chicken in chickens:
                tmp = abs(house[0]-chicken[0])+abs(house[1]-chicken[1])
                dis = min(dis, tmp)
            distance += dis
        
        result.append(distance)
    print(result)
    return min(result)

print(solution())
