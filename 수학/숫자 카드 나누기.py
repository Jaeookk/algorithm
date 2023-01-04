# https://school.programmers.co.kr/learn/courses/30/lessons/135807
import math

def solution(arrayA, arrayB):
    answer = 0
    gcd_A = arrayA[0]
    gcd_B = arrayB[0]
    for i in range(1,len(arrayA)):
        gcd_A = math.gcd(gcd_A, arrayA[i])
        gcd_B = math.gcd(gcd_B, arrayB[i])
    
    for i in range(len(arrayA)):
        if gcd_B != 0 and arrayA[i] % gcd_B == 0:
            gcd_B = 0
        if gcd_A != 0 and arrayB[i] % gcd_A == 0:
            gcd_A = 0
        
    return max(gcd_A, gcd_B)
