# https://school.programmers.co.kr/learn/courses/30/lessons/64064
# 완탐, 순열, dfs, 백트래킹

from itertools import permutations


def check(users, banned_id):
    for i in range(len(banned_id)):
        if len(users[i]) != len(banned_id[i]):
            return False
        else:
            for u, b in zip(users[i], banned_id[i]):
                if b == "*":
                    continue
                if u != b:
                    return False
    return True


def solution(user_id, banned_id):
    user_permutation = list(permutations(user_id, len(banned_id)))
    possible = []

    for users in user_permutation:
        if not check(users, banned_id):
            continue
        else:
            users = set(users)
            if users not in possible:
                possible.append(users)

    return len(possible)


### DFS를 이용한 풀이...
# answer = []

# def dfs(ban_dict, banned_id, depth, id_set):
#     if depth == len(banned_id):
#         if set(id_set) not in answer:
#             answer.append(set(id_set))
#         return

#     now = banned_id[depth]
#     for i in range(len(ban_dict[now])):     # now에 해당하는 banned_id의 후보군을 하나씩 조사
#         if ban_dict[now][i] in id_set:      # 이미 id_set에 추가했다면 패스
#             continue
#         id_set.append(ban_dict[now][i])     # id_set에 추가하고 다음 dfs로 넘어가기
#         dfs(ban_dict,banned_id, depth+1, id_set)
#         id_set.pop()    # 조사를 했으니 id_set에서 빼기
# # 즉, id_set이 -> [frodo] -> [frodo, crodo] -> [frodo, crodo, abc123] -> [frodo, crodo, frodoc]

# def solution(user_id, banned_id):
#     banned_dict = {}  # 제재 아이디 목록 후보

#     for b in banned_id :
#         banned_dict[b] = []  # banned_id가 Key인 딕셔너리 만들기

#     for bi in banned_id :
#         for ui in user_id :
#             # banned_id에 대하여 모든 user_id를 조사하여 후보군을 banned_dict에 넣기
#             # 1. 길이가 같아야 하고
#             # 2. *을 제외한 부분 글자가 같아야함
#             if len(bi) != len(ui):
#                 continue
#             for idx in range(len(bi)) :
#                 if bi[idx] == '*':
#                     continue
#                 if bi[idx] != ui[idx] :
#                     break
#             else :
#                 if ui not in banned_dict[bi]:
#                     banned_dict[bi].append(ui)

#     # banned_id에 해당하는 후보 user_id를 모두 구하였다면 dfs를 통해서 경우의수 찾기.
#     # ex).
#     # user_id = ["frodo", "fradi", "crodo", "abc123", "frodoc"]
#     # banned_id = ["*rodo", "*rodo", "******"]
#     # 위 코드를 통해서 banned_dict = {"*rodo" : ["frodo", "crodo"], "******" : ["abc123", "frodoc"]}

#     dfs(banned_dict,banned_id,0,[])

#     return len(answer)
