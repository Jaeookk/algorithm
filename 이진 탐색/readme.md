## 이진 탐색 알고리즘  

이진 탐색에 대해 알아보기 전에 가장 기본 탐색 방법인 순차 탐색에 대해 먼저 이해할 필요가 있다.
* 순차 탐색 : 리스트 안에 있는 특정한 **데이터를 찾기 위해 앞에서부터 데이터를 하나씩 확인** 하는 방법.
  *  보통 정렬되지 않은 리스트에서 데이터를 찾아야 할 때 사용
* 이진 탐색 : 정렬되어 있는 리스트에서 **탐색 범위를 절반씩 좁혀가며 데이터를 탐색** 하는 방법.
  * 이진 탐색은 시작점, 끝점, 중간점을 이용해서 탐색 범위를 설정
  * 찾으려는 데이터와 중간점 위치에 있는 데이터를 반복적으로 비교해서 원하는 데이터를 찾는 것이 이진 탐색 과정이다.
<br/>

## 이진 탐색 동작 예시
* 이미 정렬된 10개의 데이터 중에서 값이 4인 원소를 찾는 예시를 살펴보자.  
![image](https://user-images.githubusercontent.com/78528903/181243480-435b8ce2-a90c-4352-95f8-e24d75a62743.png)

* **[Step 1]**  
시작점과 끝점을 확인한 다음 둘 사이에 중간점을 정한다. 중간점이 실수일 때는 소수점 이하를 버린다.  
그림에서 각각의 **인덱스는 시작점: [0], 끝점: [9], 중간점: [4] (소수점 이하 제거)이다.**  
다음으로 중간점 [4]의 데이터 8과 찾으려는 데이터 4를 비교한다. 중간점의 데이터 8이 더 크므로 중간점 이후의 값은 확인할 필요가 없다. 끝점을 [4]의 이전인 [3]으로 옮긴다.   
![image](https://user-images.githubusercontent.com/78528903/181243875-280855ce-4389-4162-a6ee-d391da2bfa0a.png)

* **[Step 2]**  
시작점은 [0], 끝점은 [3], 중간점은 [1]이다.  
중간점에 위치한 데이터 2는 찾으려는 데이터 4보다 작으므로 이번에는 값이 2 이하인 데이터는 더이상 확인할 필요가 없다.  
따라서 시작점을 [2]로 변경한다.  
![image](https://user-images.githubusercontent.com/78528903/181244206-00648d09-9aa6-409a-979f-c1c36a7b1c3f.png)
  
* **[Step 3]**  
시작점은 [2], 끝점은 [3]이다. 이때 중간점은 [2]이다.(2.5에서 소수점 이하를 버리기 때문)  
중간점에 위치한 데이터 4는 찾으려는 데이터 4와 동일하므로 이 시점에서 탐색을 종료한다.  
![image](https://user-images.githubusercontent.com/78528903/181244364-e37f60b6-2535-4a71-8b02-13733dceeef9.png)

<br/>  

## 이진 탐색의 시간 복잡도
* 단계마다 탐색 범위를 2로 나누는 것과 동일하므로 **연산 횟수는 $log_{2}N$에 비례** 한다.
* 예를 들어 초기 데이터 개수가 32개일 때, 이상적으로 1단계를 거치면 16개 가량의 데이터만 남는다.
  * 2단계를 거치면 8개 가량의 데이터만 남는다.
  * 3단계를 거치면 4개 가량의 데이터만 남는다.
* 다시 말해 이진 탐색은 탐색 범위를 절반씩 줄이며, **시간 복잡도는 $O(logN)$을 보장** 한다.  
<br/>

> 재귀 함수로 구현한 이진 탐색 소스코드
```python
def binary_search(array, target, start, end):
    if start > end: # 탐색하고자 하는 범위에 데이터가 존재하지 않음
        return None
    mid = (start + end) // 2
    # 찾은 경우 중간점 인덱스 반환
    if array[mid] == target:
        return mid
    # 중간점의 값보다 찾고자 하는 값이 작은 경우 왼쪽 확인
    elif array[mid] > target:
        return binary_search(array, target, start, mid - 1)
    # 중간점의 값보다 찾고자 하는 값이 큰 경우 오른쪽 확인
    else:
        return binary_search(array, target, mid + 1, end)
        
	
# n(원소의 개수)과 target(찾고자 하는 문자열)을 입력받기
n, target = list(map(int, input().split()))
# 전체 원소 입력받기
array = list(map(int, input().split()))

# 이진 탐색 수행 결과 출력
result = binary_search(array, target, 0, n - 1)
if result == None:
    print("원소가 존재하지 않습니다.")
else:
    print(result + 1)
    
>>>
10 7
1 3 5 7 9 11 13 15 17 19
4
>>>
10 7
1 3 5 6 9 11 13 15 17 19
원소가 존재하지 않습니다.
```
<br/>

> 반복문으로 구현한 이진 탐색 소스코드
```python
def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        # 찾은 경우 중간점 인덱스 반환
        if array[mid] == target:
            return mid
        # 중간점의 값보다 찾고자 하는 값이 작은 경우 왼쪽 확인
        elif array[mid] > target:
            end = mid - 1
        # 중간점의 값보다 찾고자 하는 값이 큰 경우 오른쪽 확인
        else:
            start = mid + 1
    return None
    
# n(원소의 개수)과 target(찾고자 하는 문자열)을 입력받기
n, target = list(map(int, input().split()))
# 전체 원소 입력받기
array = list(map(int, input().split()))

# 이진 탐색 수행 결과 출력
result = binary_search(array, target, 0, n - 1)
if result == None:
    print("원소가 존재하지 않습니다.")
else:
    print(result + 1)
```
<br/>


> **Lower bound**
```python
def lower_bound(target, len):
    start = 0
    end = len
    while start < end:
        mid = (start + end) // 2
        if arr[mid] >= target:
            end = mid
        else:
            start = mid + 1
    return start
```
arr[mid]가 target보다 크다는 정보만 가지고 있으면 **mid가 target이 들어갈 수 있는 가장 왼쪽 위치**일 수도 있다는걸 생각해야 한다.

만약 예를 들어 arr[3] = 6, arr[4] = 6, target = 10이라고 한다면, 10이 들어갈 수 있는 가장 왼쪽 위치가 mid, 즉 5번째가 된다. 

그렇기 때문에 **arr[mid] >= target일 때에는 end = mid**로 변경해야 한다.

즉, 그림으로 나타내자면 아래와 같다.

![image](https://github.com/Jaeookk/algorithm/assets/78528903/7ce9ebd4-5750-4dc2-8d96-fd58cab28111)

arr[mid] >= target일 때에는 초록색 구간으로, end = mid가 되고, arr[mid] < target일 때에는 하늘색 구간으로, start = mid + 1이 된다.

<br/>

> **Upper bound**
```python
def upper_bound(target, len):
    start = 0
    end = len
    while start < end:
        mid = (start + end) // 2
        if arr[mid] > target:
            end = mid
        else:
            start = mid + 1
    return start
```
**가장 오른쪽 위치를 구하는 것**은 가장 왼쪽의 위치를 구할때랑 형태는 비슷한데, **arr[mid] = target일 때에만 달라진다.**

![image](https://github.com/Jaeookk/algorithm/assets/78528903/7cb2d3e7-9338-4645-bfc3-38d3117e335f)

가장 오른쪽 위치를 구할 때에는 **arr[mid] = target일 때 하늘색 구간**이 된다.
왜냐하면 **가장 오른쪽 위치는 target보다 큰 수가 최초로 나온 위치**이기 때문이다.

<br/>

## 코딩 테스트에서의 이진 탐색

단순히 앞의 코드를 보고 이진 탐색이 단순하다고 느낄 수 있지만, 정작 참고할 소스코드가 없는 상태에서 이진 탐색의 소스코드를 구현하는 것은 상당히 어려운 작업이 될 수 있다.  
코드가 짧으니 이진 탐색을 처음 접한다면, 자연스럽게 외워보자.  
이진 탐색은 코딩 테스트에서 단골로 나오는 문제이니 가급적 외워버리자!  

코딩 테스트의 이진 탐색 문제는 **탐색 범위가 큰 상황에서의 탐색** 을 가정하는 문제가 많다.  
따라서 탐색 범위가 **2,000만을 넘어가면** 이진 탐색으로 문제에 접근해보길 권한다.  
처리해야 할 데이터의 개수나 값이 **1,000만 단위 이상으로 넘어가면 이진 탐색과 같이 $O(logN)$** 의 속도를 내야 하는 알고리즘을 떠올려야 문제를 풀 수 있는 경우가 많다!!

<br/>

## 파이썬 이진 탐색 라이브러리
* `bisect_left(a, x)` : 정렬된 순서를 유지하면서 배열 a에 x를 삽입할 가장 왼쪽 인덱스를 반환
* `bisect_right(a, x)` : 정렬된 순서를 유지하면서 배열 a에 x를 삽입할 가장 오른쪽 인덱스를 반환  
![image](https://user-images.githubusercontent.com/78528903/181248035-98096035-6d56-4cdf-8d19-9ca0fd9df25f.png)

> 값이 특정 범위에 속하는 데이터 개수 구하기
```python
from bisect import bisect_left, bisect_right

# 값이 [left_value, right_value]인 데이터의 개수를 반환하는 함수
def count_by_range(a, left_value, right_value):
		right_index = bisect_right(a, right_value)
		left_index = bisect_left(a, left_value)
		return right_index - left_index

# 리스트 선언 
a = [1, 2, 3, 3, 3, 3, 4, 4, 8, 9]

# 값이 4인 데이터 개수 출력
print(count_by_range(a, 4, 4))

# 값이 [-1, 3] 범위에 있는 데이터 개수 출력
print(count_by_range(a, -1, 3))

>>>
2
6
```
<br/>

## 파라메트릭 서치 (Parametric Search)
* **파라메트릭 서치** 란 조건을 만족하는 최소/최대값을 구하는 문제(**최적화 문제**)를 **결정 문제**('예' 혹은 '아니오')로 바꾸어 해결하는 기법이다.
  * 예시: 특정한 조건을 만족하는 가장 알맞은 값을 빠르게 찾는 최적화 문제
* 일반적으로 코딩 테스트에서 파라메트릭 서치 문제는 **이진 탐색을 이용하여 해결** 할 수 있다.

<br/>

[**BOJ 1654번 : 랜선 자르기**](https://www.acmicpc.net/problem/1654)  
> * (최적화 문제) N개를 만들 수 있는 랜선의 **최대** 길이  
> * (결정 문제) 랜선의 길이가 X일 때 랜선이 N개 **이상인가 아닌가?**  
> [풀이](https://github.com/Jaeookk/algorithm/blob/main/%EC%9D%B4%EC%A7%84%20%ED%83%90%EC%83%89/%EB%9E%9C%EC%84%A0%20%EC%9E%90%EB%A5%B4%EA%B8%B0.py)

이 문제의 상황은 **N개를 만들 수 있는 랜선의 최대 길이** 를 구하는 **최적화 문제** 이다.  
이걸 **결정 문제** 로 바꾸면 반대로 우리가 **구해야 하는 답** 이 **인자** 로 들어가고, **조건의 참/거짓 여부를 판단하는 문제** 로 만들 수 있다.  
<br/>

![image](https://user-images.githubusercontent.com/78528903/209121468-980ff7e8-6015-4fc6-8b77-02bd8ab2b7e2.png)  
랜선의 길이가 줄어들수록 개수가 많아지는건 당연한 사실이니까 간단하게 그래프를 그려보면 **랜선의 길이가 x축** 에 놓이고 **개수가 y축** 에 놓이게 된다.    

그리고 그래프는 **x가 커질수록 y가 감소하는 형태** 이다. 그래프에서 답은 표시한 지점으로, 개수가 N개 이상인 지점들 중에서 가장 길이가 긴 곳입니다.   

이 답을 기점으로 왼쪽은 개수가 N 이상이고 오른쪽은 N 미만입니다. 랜선의 길이는 최소 1, 최대 $2^{31} - 1$ 인데, 우리는 여기서 이분탐색으로 답을 빠르게 찾아낼 수 있습니다.  
<br/>

![image](https://user-images.githubusercontent.com/78528903/209122217-29458b2c-9e61-432a-b3fa-437f658048b8.png)  
이렇게 st, mid, en을 놓고 범위를 줄여가며 답을 찾아보자. 

랜선의 길이가 mid일 때 랜선이 N개 미만이다. 그러면 mid 이상은 절대 답이 될 수 없으니 en = mid - 1로 바꾼다. 만약 랜선의 길이가 mid일 때 랜선이 N개 이상이었다면 st = mid로 바꿔주면 된다. 

이렇게 최대 길이를 구해야하는 문제에서 랜선의 길이가 X일 때 조건을 만족하는지 확인하는 문제로 변환해서 풀이를 해낼 수 있다. 이 문제의 경우, 랜선의 길이를 X로 두고나면 조각의 개수를 구하는건 $O(K)$이고 랜선의 길이로 가능한 범위는 $2^{31}$이어서 시간복잡도는 $O(log(2^{31})K) = O(31K)$입니다.  
<br/>

![image](https://user-images.githubusercontent.com/78528903/209122858-19914402-0b2c-40fb-834b-96daac3f52f6.png)  
여기서 주의해야하는건, 지금처럼 이분탐색을 수행할 변수를 가지고 함수를 세웠을 때 그 함수가 **감소함수** 이거나 **증가함수**여야 한다.
만약 이 그래프처럼 함수가 감소 혹은 증가함수 형태가 아니라 뒤죽박죽이면 이분탐색 자체가 불가능하다. 

그래서 parametric search를 할 때에는 **최적화 문제를 결정 문제로 바꿀 수 있는지** 생각하고 그 **결정 문제로 얻어낸 함수가 감소 혹은 증가함수인지** 를 따져봐야 합니다. 

문제에서 **최소 혹은 최대 얘기** 가 있고 **범위가 무지막지하게 크거나** , 뭔가 **시간복잡도에서 값 하나를 로그로 어떻게 잘 떨구면** 될 것 같을 때 **parametric search 풀이가 가능하지는 않을까** 고민을 해볼 필요가 있습니다. 


<br/>

## 트리 자료 구조


<br/>

## 이진 탐색 트리


<br/>

## 빠르게 입력받기

