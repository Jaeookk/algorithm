import sys


def solve(depth, index, N, skill, visited, a_skill, b_skill, result):
    if depth == N // 2:
        a_team = 0
        b_team = 0
        for i in range(N):
            if visited[i]:
                a_team += a_skill[i]
            else:
                b_team += b_skill[i]

        return min(abs(a_team - b_team), result)

    for i in range(index, N):
        visited[i] = True
        result = solve(depth + 1, i + 1, N, skill, visited, a_skill, b_skill, result)
        visited[i] = False

    return result

def main():
    N = int(sys.stdin.readline().strip())
    skill = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(N)]

    visited = [0]*N

    a_skill = [sum(row) for row in skill]
    b_skill = [sum(col) for col in zip(*skill)]

    print(solve(0, 0, N, skill, visited, a_skill, b_skill, 9e9))


if __name__ == "__main__":
    main()
