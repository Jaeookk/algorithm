# https://softeer.ai/practice/info.do?idx=1&eid=395&sw_prbl_sbms_sn=220303
import sys


def solution(w, n, arr):
    answer = 0
    arr.sort(key=lambda x: -x[1])

    cur_weight = 0
    for i in range(len(arr)):
        if cur_weight + arr[i][0] <= w:
            answer += arr[i][0] * arr[i][1]
            cur_weight += arr[i][0]
        elif cur_weight + arr[i][0] > w:
            answer += (w - cur_weight) * arr[i][1]
            break
    print(answer)


if __name__ == "__main__":
    input = sys.stdin.readline
    w, n = map(int, input().split())  # 무게, 종류
    arr = []
    for _ in range(n):
        a, b = map(int, input().split())
        arr.append((a, b))
    solution(w, n, arr)
