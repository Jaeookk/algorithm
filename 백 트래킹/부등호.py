# 백준 2529 실버1


def check(i, j, k):
    if k == "<":
        return i < j
    else:
        return i > j


def dfs(depth, s):
    if depth == k + 1:
        if result["min"] == "":
            result["min"] = s
        else:
            result["max"] = s
        return

    for i in range(10):
        if not visited[i]:
            if depth == 0 or check(s[-1], str(i), op[depth - 1]):
                visited[i] = True
                dfs(depth + 1, s + str(i))
                visited[i] = False


def main():
    dfs(0, "")
    print(result["max"])
    print(result["min"])


if __name__ == "__main__":
    k = int(input())
    op = list(input().split())
    visited = [False] * 10
    result = {"max": "", "min": ""}

    main()
