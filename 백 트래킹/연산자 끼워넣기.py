# 백준 14888 실버1

import sys


def dfs(i, value, add, sub, mul, div):
    # 모든 연산자를 다 사용한 경우, 최솟값과 최댓값 업데이트
    if i == n:
        result["min_value"] = min(result["min_value"], value)
        result["max_value"] = max(result["max_value"], value)

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


def main():
    dfs(1, data[0], add, sub, mul, div)

    print(result["max_value"])
    print(result["min_value"])


if __name__ == "__main__":
    input = sys.stdin.readline
    n = int(input())
    data = list(map(int, input().split()))
    add, sub, mul, div = map(int, input().split())

    result = {"max_value": -1e9, "min_value": 1e9}
    main()
