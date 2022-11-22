n = int(input())
arr = list(map(int, input().split()))

cnt, end = 0, 0
visited = [0] * 100001
for start in range(n):
    while end < n:
        if visited[arr[end]] == 1:
            break
        visited[arr[end]] = 1
        end += 1
    cnt += end - start
    visited[arr[start]] = 0

print(cnt)

# 1. start = 0, end = 0으로 초기화합니다.
# 2. start를 n까지 for문 순회합니다.
# 3. start값부터 시작하여 처음 같은 숫자가 나올 때까지 end를 증가시킵니다.
# 4. end가 더 이상 진전할 수 없다면, end - start를 결괏값에 더해줍니다. (같은 숫자가 나오기 전까지 모든 경우의 수)
# +) 만약에 1, 2, 3, 4, 5라는 수열이라면, start가 0일 때 end는 5까지 진행됩니다.
# +) 따라서 1, 12, 123, 1234, 12345의 5개의 수열이 생성될 수 있기 때문에 end - start를 더해줍니다.
# 5. 현재 start값에 대한 모든 판단이 끝났다면, start값에 대한 방문처리를 해제해줍니다. (start~end까지 arr[start]와 중복된 것이 있었다면 이를 해제)
# 6. 다음 start값에 대해 3~5 반복
