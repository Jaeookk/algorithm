# d[i] = i번째 타일을 채우는 가장 작은 경우의 수
# d[i] = d[i-1] --> n-1길이의 타일에서 2x1 타일을 채우는 경우
# d[i] = d[i-2] --> n-2길이의 타일에서 1x2 타일 2개를 채우는 경우
# d[i] = d[i-2] --> n-2 길이의 타일에서 2x2 타일 1개를 채우는 경우
import sys

input = sys.stdin.readline

n = int(input())
d = [0] * 1001

def main():
    # 초기값 지정
    d[0] = 1
    d[1] = 1

    # 점화식에 따른 경우의 수 계산
    for i in range(2, n + 1):
        d[i] = (d[i - 1] + 2 * d[i - 2]) % 10007

    print(d[n])

if __name__ == "__main__":
    main()