def rotate(m, d):
    """
    input:
       m: 회전하고자 하는 2차원 배열. 입력이 정방형 행렬이라고 가정한다.
       d: 90도씩의 회전 단위. -1: -90도, 1: 90도, 2: 180도, ...
    """
    N = len(m)
    # 'ret = [[0] * N] * N'과 같이 하지 않는 이유 :
    # [[0] * N] 부분이 N번 얕은복사가 되어 [0][0]을 바꾸면 [1][0], [2][0] ...이 모두 바뀐다.
    ret = [[0] * N for _ in range(N)] 

    if d % 4 == 1:
        for r in range(N):
            for c in range(N):
                ret[c][N-1-r] = m[r][c]
    elif d % 4 == 2:
        for r in range(N):
            for c in range(N):
                ret[N-1-r][N-1-c] = m[r][c]
    elif d % 4 == 3:
        for r in range(N):
            for c in range(N):
                ret[N-1-c][r] = m[r][c]
    else:
        for r in range(N):
            for c in range(N):
                ret[r][c] = m[r][c]

    return ret

def check(m):
    length = len(m) // 3
    for i in range(length):
        for j in range(length):
            if m[length + i][length + j] != 1:
                return False
    return True

def solution(key, lock):
    # 3배 확장된 lock 만들기
    x, y = len(lock), len(key)
    expand_lock = [[0] * (x * 3) for _ in range(x * 3)]
    for i in range(x):
        for j in range(x):
            expand_lock[x + i][x + j] = lock[i][j]
    # print(expand_lock)
    
    # 각 회전에 대하여 모두 확인
    for i in range(4):
        new_key = rotate(key,i)
        
        for j in range(x * 2):
            for k in range(x * 2):
                # 자물쇠에 열쇠 끼워 넣기
                for p in range(y):
                    for q in range(y):
                        expand_lock[j+p][k+q] += new_key[p][q]
                 
                if check(expand_lock) == True:
                    return True
                # 열쇠가 맞지 않다면, 다시 빼기
                for p in range(y):
                    for q in range(y):
                        expand_lock[j+p][k+q] -= new_key[p][q]

    return False
