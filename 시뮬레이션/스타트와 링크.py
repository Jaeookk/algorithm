def dfs(depth, team, idx):
    global result
    if depth == n // 2:
        temp = 0
        for i in range(len(team)):
            for j in range(i, len(team)):
                temp += ability[team[i]][team[j]] + ability[team[j]][team[i]]
        result.append(temp)
        return

    for i in range(idx, n):
        if i not in team:
            team.append(i)
            dfs(depth + 1, team, i+1)
            team.pop()


if __name__ == "__main__":
    n = int(input())
    ability = [list(map(int, input().split())) for _ in range(n)]

    team = []
    result = []
    answer = []

    dfs(0, team,0)
    for i in range(len(result) // 2):
        answer.append(abs(result[i] - result[len(result) - i - 1]))
    print(min(answer))

# 시간초과
# def dfs(depth, team):
#     global result
#     if depth == n // 2:
#         temp = 0
#         team_b = [x for x in [i for i in range(0, n)] if x not in team]
#         for i in range(len(team)):
#             for j in range(i, len(team)):
#                 temp += ability[team[i]][team[j]] + ability[team[j]][team[i]]
#                 temp -= (
#                     ability[team_b[i]][team_b[j]]
#                     + ability[team_b[j]][team_b[i]]
#                 )
#         result = min(result, abs(temp))
#         return

#     for i in range(0, n):
#         if i not in team:
#             team.append(i)
#             dfs(depth + 1, team)
#             team.pop()


# dfs(0, team)
# print(result)
