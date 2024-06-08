import time

# https://school.programmers.co.kr/learn/courses/30/lessons/178871
def solution(players, callings):
    start_time = time.time()

    # 선수 이름을 키로, 현재 등수를 값으로 하는 해시맵 생성
    player_indices = {player: i for i, player in enumerate(players)}

    # callings 배열을 순회하며 등수 업데이트
    for calling in callings:
        # 호출된 선수의 현재 등수
        curr_index = player_indices[calling]

        # 추월 당하는 선수
        prev_player = players[curr_index - 1]

        # 선수 배열에서 위치 변경
        players[curr_index], players[curr_index - 1] = players[curr_index - 1], players[curr_index]

        # 해시맵에서 등수 변경
        player_indices[calling] -= 1
        player_indices[prev_player] += 1

    print(f"Total time : {time.time() - start_time}")

    return players
