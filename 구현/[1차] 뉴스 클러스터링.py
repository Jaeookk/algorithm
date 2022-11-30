# https://school.programmers.co.kr/learn/courses/30/lessons/17677
import re

def solution(str1, str2):
    str1 = re.sub(r"[^a-zA-Z]"," ", str1).lower()
    str2 = re.sub(r"[^a-zA-Z]"," ", str2).lower()
    A,B = [],[]
    for i in range(len(str1)-1):
        if len(str1[i:i+2].strip()) == 2:
            A.append(str1[i:i+2])
    for j in range(len(str2)-1):
        if len(str2[j:j+2].strip()) == 2:
            B.append(str2[j:j+2])
    
    # A∩B = A+B-A∪B
    total_len = len(A)+len(B)
    intersection, i = 0, 0
    while i<len(A):
        if len(A) == 0 or len(B) == 0:
            break
        if A[i] in B:
            intersection += 1
            B.remove(A[i])
            A.remove(A[i])
            continue
        i+=1

    sum_of_set = total_len-intersection
    
    if sum_of_set == 0:
        return 65536
    else:
        return int(intersection/sum_of_set*65536)
