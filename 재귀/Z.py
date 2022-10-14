# N = 3일 때 r = 2, c = 2인 곳을 몇 번째로 방문할까?
# (힌트, N = 2일 때 r = 2, c = 2인 곳은 12번에 방문한다)
# 이 문제에서는 번호가 배열을 4등분한 후에 1,2,3,4 순으로 진행이 된다.
# 그리고 각 사각형 안에서는 N=2일 때의 움직임을 그대로 따라가니 r = 2, c = 2인 곳은 12번째로 방문.

# 그렇다면 N = 3일 때, r = 6, c = 2인 곳은 몇 번째로 방문할까?
# 이 곳을 방문하기 전에 분명 1번과 2번 사각형 내의 모든 칸을 다 방문했을 것이다.
# 즉, 3번 사각형이 시작되기 전 이미 32개의 칸을 방문했고, 3번 사각형 내에서는 12번째로 방문되니
# 최종적으로 32 + 12 = 44번째라는 것을 알 수 있다.

# 즉!! N = k일 때의 결과를 가지고 N = k + 1의 결과를 구할 수 있다는 것이다.

# 1. 함수의 정의
#     def func(n, r, c) -> 2^n x 2^n 배열에서 (r,c)를 방문하는 순서를 반환하는 함수
# 2. base condition
#     n = 0일 때 return 0
# 3. 재귀식
#     (r,c)가 1번 사각형일 때 return func(n-1, r, c)
#     (r,c)가 2번 사각형일 때 return half * half + func(n-1, r, c - half)
#     (r,c)가 3번 사각형일 때 return 2 * half * half + func(n-1, r - half, c)
#     (r,c)가 4번 사각형일 때 return 3 * half * half + func(n-1, r - half, c - half)


def func(n, r, c):
    if n == 0:
        return 0
    half = 2 ** (n - 1)
    if r < half and c < half:
        return func(n - 1, r, c)
    elif r < half and c >= half:
        return half * half + func(n - 1, r, c - half)
    elif r >= half and c < half:
        return 2 * half * half + func(n - 1, r - half, c)
    else:
        return 3 * half * half + func(n - 1, r - half, c - half)


n, r, c = map(int, input().split())
print(func(n, r, c))
