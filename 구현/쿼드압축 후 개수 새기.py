# https://school.programmers.co.kr/learn/courses/30/lessons/68936
def solution(arr):
    answer = [0,0]
    
    def quad(x,y,size):
        target = arr[x][y]
        for dx in range(size):
            for dy in range(size):
                if arr[x+dx][y+dy] != target:
                    quad(x, y, size//2) # 4등분한거의 첫번째
                    quad(x+size//2, y, size//2) # 4등분한거의 두번째
                    quad(x, y+size//2, size//2) # 4등분한거의 세번째
                    quad(x+size//2, y+size//2, size//2) # 4등분한거의 네번째
                    return  # 4등분하여 조사를 완료했으니, 바로 종료.
        answer[target]+=1
        
    quad(0,0,len(arr))
        
    return answer
