# 최소 한 개의 모음(a, e, i, o, u)과 최소 두 개의 자음
l, c = map(int, input().split())
alpha = list(input().split())
alpha.sort()

vowels = ["a", "e", "i", "o", "u"]
visited = [False] * c
result = []


def dfs(k):
    global result

    if len(result) == l:
        count = 0
        for vowel in vowels:
            if vowel in result:
                count += 1
        if 1 <= count and l - count >= 2:
            print("".join(result))
        return

    for i in range(k, c):
        if not visited[i]:
            result.append(alpha[i])
            visited[i] = True
            dfs(i + 1)
            result.pop()
            visited[i] = False


dfs(0)
