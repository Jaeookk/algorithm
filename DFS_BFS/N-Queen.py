def is_promising(x,y,n,row):
    for i in range(x): # 현재 row index 이전의 모든 row에 대하여
        if y == row[i] or abs(y - row[i]) == abs(x-i): # 같은 열에 위치 하지 않고 대각선에도 위치 하지 않는지 체크
            return False
    return True

def dfs(x, n, row):
    """
    x : 행 인덱스
    n : 체스판 크기
    row : 배치 좌표 리스트 
    """
    if x == n:
        return 1
    
    count = 0
    for y in range(n): # y는 column index
        if is_promising(x,y,n,row):
            row[x] = y # x행 y열에 퀸 배치
            count += dfs(x+1, n, row) # 행 1칸 증가하여 재호출
                                      # 만약 n개의 퀸이 모두 배치가 완료되면 count에 +1

    return count

def solution(n):
    answer = 0
    row = [0]*n  # row[i]=k 이면 (i,k)에 퀸이 위치한다는 의미.
                 # 즉, i는 퀸이 위치한 행의 인덱스고, k는 열의 인덱스이다.  
    answer += dfs(0,n,row)
    return answer
  
# 좀 더 간단한 코드
#   def dfs(queen, n, row):
#     count = 0
    
#     if n == row:
#         return 1
    
#     # 가로로 한번만 진행
#     for col in range(n):
#         queen[row] = col

#         # for-else구문
#         for x in range(row):
#             # 세로로 겹치면 안됨
#             if queen[x] == queen[row]: 
#                 break
                
#             # 대각선으로 겹치면 안됨
#             if abs(queen[x]-queen[row]) == (row-x):
#                 break
#         else:
#             count += dfs(queen, n, row+1)
            
#     return count

# def solution(n):
#     queen = [0]*n
        
#     return dfs(queen, n, 0)
