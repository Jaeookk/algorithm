n = int(input())
cards = list(map(int, input().split()))
cards.sort()

m = int(input())
data = list(map(int, input().split()))
print(cards)


def lower_idx(array, target, start, end):
    while start < end:
        mid = (start + end) // 2
        if array[mid] >= target:
            # array[mid]가 target보다 크다는 정보만 가지고 있으면
            # mid가 target이 들어갈 수 있는 가장 왼쪽 위치일 수도 있다는걸 생각
            # ex) 2 4 6 6 6 16 16 16 30 32 35 일때 10이 들어갈 수 있는 가장 왼쪽 위치가 mid, 즉 5번째가 된다.
            #              🔼
            # 그렇기 때문에 end = mid로 변경
            end = mid
        else:
            start = mid + 1
    return start


def upper_idx(array, target, start, end):
    while start < end:
        mid = (start + end) // 2
        if array[mid] > target:
            end = mid
        else:
            start = mid + 1
    return start


for i in data:
    print(upper_idx(cards, i, 0, n) - lower_idx(cards, i, 0, n), end=" ")
