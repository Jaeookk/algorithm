n = int(input())
A = list(map(int, input().split()))
A.sort()

m = int(input())
data = list(map(int, input().split()))


def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        # 찾은 경우 중간점 인덱스 반환
        if array[mid] == target:
            return 1
        # 중간점의 값보다 찾고자 하는 값이 작은 경우 왼쪽 확인
        elif array[mid] > target:
            end = mid - 1
        # 중간점의 값보다 찾고자 하는 값이 큰 경우 오른쪽 확인
        else:
            start = mid + 1
    # 찾는 target이 없다면 None 리턴
    return 0


for i in data:
    print(binary_search(A, i, 0, n - 1))
