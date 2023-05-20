# https://school.programmers.co.kr/learn/courses/30/lessons/12971#


def solution(sticker):
    # dp 사용
    # sticker배열은 원형으로 주어지므로
    # 처음을 뽑았을때는 마지막을 뽑으면 안되고
    # 처음을 안뽑았을 때는 마지막을 뽑아도 된다.
    # 이를 고려해 0번 인덱스에서 시작, 1번 인덱스에서 시작하는 dp를 2개 만들어주자.

    if len(sticker) == 1:
        return sticker[0]

    # dp[i][0] = i번째 선택, dp[i][1] = i번째 선택 X
    dp0 = [[0, 0] for _ in range(len(sticker) - 1)]  # 0번째 인덱스를 선택할 때
    dp1 = [[0, 0] for _ in range(len(sticker))]  # 1번째 인덱스를 선택할 때
    dp0[0][0] = sticker[0]
    dp1[1][0] = sticker[1]

    for i in range(1, len(sticker) - 1):
        dp0[i][0] = dp0[i - 1][1] + sticker[i]
        dp0[i][1] = max(dp0[i - 1][1], dp0[i - 1][0])

    for i in range(2, len(sticker)):
        dp1[i][0] = dp1[i - 1][1] + sticker[i]
        dp1[i][1] = max(dp1[i - 1][1], dp1[i - 1][0])

    answer = max(max(dp0[-1]), max(dp1[-1]))
    return answer
