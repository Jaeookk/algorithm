def bubble_sort(arr):
    length = len(arr) - 1
    for i in range(length):
        isSort = False
        for j in range(length - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                isSort = True
        print(arr)
        if isSort == False:
            break

    return arr


def selection_sort(array):
    for i in range(len(array)):
        min_index = i  # 가장 작은 원소의 인덱스
        for j in range(i + 1, len(array)):
            if array[min_index] > array[j]:
                min_index = j
        array[i], array[min_index] = array[min_index], array[i]  # 스와프
        print(array)


def insertion_sort(array):
    for i in range(1, len(array)):
        for j in range(i, 0, -1):  # 인덱스 i부터 1까지 감소하며 반복
            if array[j] < array[j - 1]:  # 한 칸씩 왼쪽으로 이동
                array[j], array[j - 1] = array[j - 1], array[j]
            else:  # 자기보다 작은 데이터를 만나면 그 위치에서 멈춤
                break
        print(array)


def quick_sort(array):
    # 리스트가 하나 이하의 원소만을 담고 있다면 종료
    if len(array) <= 1:
        return array
    pivot = array[0]  # 피벗은 첫 번째 원소
    tail = array[1:]  # 피벗을 제외한 리스트

    left_side = [x for x in tail if x <= pivot]  # 분할된 왼쪽 부분
    right_side = [x for x in tail if x > pivot]  # 분할된 오른쪽 부분

    print(f"pivot : {pivot}")
    print(left_side + [pivot] + right_side)
    # 분할 이후 왼쪽 부분과 오른쪽 부분에서 각각 정렬 수행하고, 전체 리스트 반환
    return quick_sort(left_side) + [pivot] + quick_sort(right_side)


if __name__ == "__main__":
    array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]
    print("before: ", array)
    # bubble_sort(array)
    # selection_sort(array)
    # insertion_sort(array)
    # array = quick_sort(array)
    print("after: ", array)
