# BOJ 1043 골드4
# Union Find를 이용해서 푸는 문제라더라.. 나는 몰랐다... Union Find로 풀어보자..
#
# BFS를 사용해서 푼 핵심 아이디어는 다음과 같다.
# 1. 파티를 조사해서 파티에서 만나는 사람들은 무방향 인접행렬 방식으로 이어주자.
#   1.1 만약 파티에 진실을 아는 사람이 있다?
#   1.2 인접행렬을 조사해서 해당 사람과 만난 사람들도 진실을 알게 됨
# 2. 진실을 아는 사람들과, 이를 통해 진실을 알게 되는 사람들을 모두 조사하여 리스트에 저장
# 3. 다시 입력으로 주어진 파티를 조사하면서, 해당 파티에 진실을 아는 사람이 있는지 없는지 본다.


import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())  # N:사람의수, M:파티의 수
K, *T = map(int, input().split())  # K : 진실을 아는 사람의 수, T: 그 번호

meet_graph = [[0 for _ in range(N + 1)] for _ in range(N + 1)]
know_people = [0] * (N + 1)  # 진실을 아는 사람들의 번호에 해당하는 인덱스 => 1
party = []
q = deque()


def bfs():
    visited = [False] * (N + 1)
    while q:
        cur = q.popleft()
        visited[cur] = True
        know_people[cur] = 1  # 큐에 있는 사람들은 모두 진실을 아는 사람들

        for i in range(1, N + 1):
            if meet_graph[cur][i] == 1 and not visited[i]:
                # 진실을 아는 사람과 같은 파티에 있고, 아직 방문하지 않았다면
                know_people[i] = 1
                q.append(i)  # 새로 진실을 알게 된 사람 큐에 넣기


def main():
    result = 0

    for i in range(K):
        q.append(T[i])  # 진실을 아는 사람들은 큐에 담기.

    for i in range(M):  # 각 파티마다
        num, *temp = map(int, input().split())  # 파티에 참석하는 사람의 수, 그 번호
        party.append(temp)

        for j in range(num):  # i번째 파티에 참가하는 사람들을 기록
            for k in range(num):
                if j != k:
                    meet_graph[party[i][j]][party[i][k]] = 1  # i번째 파티의 j번과 k번은 만나므로 1로 표시

    bfs()

    for i in range(M):
        for j in range(len(party[i])):
            if know_people[party[i][j]]:  # i번째 파티의 j사람이 진실을 아는 사람이라면
                break
        else:  # i번째 파티에 진실을 아는 사람이 없다면
            result += 1
    print(result)


if __name__ == "__main__":
    main()
