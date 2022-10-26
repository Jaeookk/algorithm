n = int(input())
# 연산을 수행하고자 하는 수 리스트
data = list(map(int, input().split()))
# 덧셈, 뺄셈, 곱셈, 나눗셈 연산자 개수
add, sub, mul, div = map(int, input().split())

min_value = 1e9
max_value = -1e9


def dfs(i, value, add, sub, mul, div):
    global min_value, max_value
    # 모든 연산자를 다 사용한 경우, 최솟값과 최댓값 업데이트
    if i == n:
        min_value = min(min_value, value)
        max_value = max(max_value, value)

    else:
        # 각 연산자에 대하여 재귀적으로 수행
        if add:
            dfs(i + 1, value + data[i], add - 1, sub, mul, div)
        if sub:
            dfs(i + 1, value - data[i], add, sub - 1, mul, div)
        if mul:
            dfs(i + 1, value * data[i], add, sub, mul - 1, div)
        if div:
            dfs(i + 1, int(value / data[i]), add, sub, mul, div - 1)


dfs(1, data[0], add, sub, mul, div)

print(max_value)
print(min_value)
