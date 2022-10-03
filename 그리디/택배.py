n, c = map(int, input().split())
m = int(input())
arr = []
for _ in range(m):
    arr.append(tuple(map(int, input().split())))

# 박스를 최대한 꽉 채워서 가면서 배송할 수 있는 박스 수를 최대화하려면 늦게 도착하는 박스보다 일찍 도착하는 박스를 우선으로 배송.
arr.sort(key=lambda x: x[1])
print(arr)

village = [0] * (n + 1)  # i번째 마을까지 갈때 트럭에 실린 박스 개수
result = 0

# 박스를 추가할 때마다 (시작마을) ~ (도착 마을 - 1)까지 추가된 박스 수를 더해준다.
# 왜냐하면 일찍 도착하는 박스 순으로 정렬했으므로, 해당 박스가 해당하는 마을에 도착할 때 까진 트럭에 실려있기때문.
for start, end, box in arr:
    temp = box
    for i in range(start, end):
        if village[i] + temp >= c:  # 트럭의 용량을 넘는다면
            temp = c - village[i]  # 최대로 실을 수 있는 박스 개수 구하기
    for i in range(start, end):
        village[i] += temp
    result += temp

print(result)
