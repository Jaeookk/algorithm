n, m, l = map(int, input().split())  # 현재 휴게소 개수, 추가할 휴게소 개수, 고속도로 길이
# 6 7 800
# 622 411 201 555 755 82

rest = [0] + list(map(int, input().split())) + [l]
rest.sort()
# 휴게소 양끝에는 설치할수없으므로 추가 + 정렬해주기

start, end = 1, l - 1

while start <= end:
    mid = (start + end) // 2
    cnt = 0
    for i in range(1, len(rest)):
        if rest[i] - rest[i - 1] > mid:
            cnt += (rest[i] - rest[i - 1] - 1) // mid  # 같은자리에 휴게소를 지을 수 없으므로 -1

    # 특정구간의 휴게소가 몇개 설치할수 있는지 count를 통해 구해줌
    if cnt > m:
        start = mid + 1
    else:
        ans = mid
        end = mid - 1  # 정답은 휴게소갯수가 우리가 원하는 것보다
        # 많아질경우 그 전경우가 우리의 답이된다.
print(ans)
