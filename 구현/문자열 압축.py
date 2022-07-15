def solution(s):
    answer = 0
    words = []
    if len(s) == 1 :
        return 1
    for i in range(1,len(s)//2+1):
        # i : 문자열 자르는 단위
        result = []
        word=''
        for j in range(len(s)//i):
            result.append(s[0+j*i : i+j*i])
            if j == len(s)//i-1:
                result.append(s[i+j*i:])
        cnt=1
        # print(result)
        for k in range(len(result)-1):
            if result[k] == result[k+1]:
                cnt += 1
                continue
            if cnt > 1:
                word += str(cnt)+result[k]
            else:
                word += result[k]
            if k == len(result) -2 :
                word += result[k+1]
            cnt = 1
        # print(word)
        words.append(len(word))
    answer = min(words)
        
    # print(result)
        
    return answer
