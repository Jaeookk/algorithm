# https://softeer.ai/practice/info.do?idx=1&eid=407
import sys


if __name__ == "__main__":
    input = sys.stdin.readline

    K, P, N = map(int, input().split())

    def main(K, P, N):
        temp = 1
        for i in range(N):
            temp *= P
            temp %= 1000000007

        return K * temp % 1000000007

    print(main(K, P, N))
