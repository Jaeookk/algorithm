# 2022 KAKAO BLIND RECRUITMENT

def solution(board, skill):
    answer = 0
    n, m = len(board), len(board[0])
    type_dict = {1:-1, 2:1}
    arr = [[0 for _ in range(m)] for _ in range(n)]
    psum_arr = [[0 for _ in range(m+1)] for _ in range(n+1)]
    
    for t, r1, c1, r2, c2 , degree in skill:
        arr[r1][c1] += type_dict[t]*degree
        if r2+1 < n: arr[r2+1][c1] -= type_dict[t]*degree
        if c2+1 < m: arr[r1][c2+1] -= type_dict[t]*degree
        if r2+1 < n and c2 + 1 < m : arr[r2+1][c2+1] += type_dict[t]*degree
    
    # for i in range(n):
    #     print(*arr[i])
    
    for i in range(1, n+1):
        for j in range(1, m+1):
            psum_arr[i][j] = arr[i-1][j-1] + psum_arr[i-1][j] + psum_arr[i][j-1] - psum_arr[i-1][j-1]
    
    # print("-"*50)
    # for i in range(n+1):
    #     print(*psum_arr[i])
    for i in range(n):
        for j in range(m):
            board[i][j] += psum_arr[i+1][j+1]
            if board[i][j] > 0:
                answer += 1
        
    return answer