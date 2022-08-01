from bisect import bisect_left, bisect_right

def count(a, left, right):
    right_index = bisect_right(a, right)
    left_index = bisect_left(a, left)
    return right_index - left_index

def solution(words, queries):
    answer = []
    array = [[] for _ in range(10001)] # 모든 단어를 길이마다 나누어서 저장하기 위한 리스트
    reversed_array = [[] for _ in range(10001)] # 모든 단어를 길이마다 나누어서 뒤집어 저장하기 위한 리스트
    
    for word in words: # 모든 단어를 접미사 와일드카드 배열, 접두사 와일드카드 배열에 각각 삽입
        array[len(word)].append(word) # 단어를 삽입
        reversed_array[len(word)].append(word[::-1]) # 단어를 뒤집어서 삽입
        
    for i in range(10001): # 이진 탐색을 수행하기 위해 각 단어 리스트 정렬 수행
        array[i].sort()
        reversed_array[i].sort()
        
    for q in queries:
        if q[0] != '?': # 접미사에 와일드카드가 붙은 경우
            res = count(array[len(q)], q.replace('?','a'), q.replace('?','z'))
        else: # 접두사에 와일드카드가 붙은 경우
            res = count(reversed_array[len(q)], q[::-1].replace('?','a'), q[::-1].replace('?','z'))
        answer.append(res)
    return answer
