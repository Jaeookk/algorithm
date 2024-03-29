## 📌 정렬(Sorting)
* **정렬(Sorting)** : 데이터를 특정한 기준에 따라서 순서대로 나열하는 것

정렬 알고리즘은 이진 탐색의 전처리 과정이기도 하니 제대로 알아야 한다.  
일반적으로 문제에서 요구하는 조건에 따라서 적절한 정렬 알고리즘이 공식처럼 사용된다.  
상황에 적절하지 못한 정렬 알고리즘을 이용하면 당연히 프로그램은 비효율적으로 동작하며 필요 이상으로 시간을 많이 소요한다.  
그래서 정렬 알고리즘을 공부하다 보면 자연스럽게 **알고리즘 효율의 중요성** 을 깨닫는다.  

<br/>

## 📌 선택 정렬
* 처리되지 않은 데이터 중에서 **가장 작은 데이터를 선택해 맨 앞에 있는 데이터와 바꾸는 것을 반복**  
<br/>

**선택 정렬 동작 예시**  
* 정렬할 데이터를 준비  
![image](https://user-images.githubusercontent.com/78528903/180970551-28ba84e2-4d2a-4373-a0f3-63b6d30d238d.png)

* **[Step 0]** 처리되지 않은 데이터 중 가장 작은 '0'을 선택해 가장 앞의 '7'과 바꾼다.  
![image](https://user-images.githubusercontent.com/78528903/180970488-5dcca07d-b831-4a20-a8ae-af91f8c13107.png)

* **[Step 1]** 정렬된 첫 번째는 제외하고 이후 처리되지 않은 데이터 중 가장 작은 '1'을 선택해 처리되지 않은 데이터 중 가장 앞의 '5'와 바꾼다.  
![image](https://user-images.githubusercontent.com/78528903/180970909-a48e7bea-37ab-4cf2-8936-4c17e04b0a7c.png)

* **[Step 2]** 정렬된 첫 번째는 제외하고 이후 처리되지 않은 데이터 중 가장 작은 '2'을 선택해 처리되지 않은 데이터 중 가장 앞의 '9'와 바꾼다.  
![image](https://user-images.githubusercontent.com/78528903/180971007-82abb7d6-bd0d-4e32-9180-eb524c37e6da.png)

* **[Step 3]** 정렬된 첫 번째는 제외하고 이후 처리되지 않은 데이터 중 가장 작은 '3'을 선택해 처리되지 않은 데이터 중 가장 앞의 '7'와 바꾼다.  
![image](https://user-images.githubusercontent.com/78528903/180971103-943c87e0-863a-4555-8a4b-fa96b56df6b5.png)  
.  
.  
.  
* **[Step 9]** 가장 작은 데이터를 앞으로 보내는 과정을 9번 반복한 상태는 다음과 같으며 마지막 데이터는 가만히 두어도 이미 정렬된 상태이다. 따라서 이 단계에서 정렬을 마칠 수 있다.  
![image](https://user-images.githubusercontent.com/78528903/180971441-9f9b9df9-8160-42be-a3a1-cb7b78355ee4.png)

이처럼 **선택 정렬** 은 가장 작은 데이터를 앞으로 보내는 과정을 **N - 1번** 반복하면 정렬이 완료되는 것을 알 수 있다.  
<br/>  
> 선택 정렬 소스코드 
```python
array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(len(array)):
    min_index = i # 가장 작은 원소의 인덱스
    for j in range(i + 1, len(array)):
        if array[min_index] > array[j]:
        min_index = j
    array[i], array[min_index] = array[min_index], array[i] # 스와프
  
print(array)

>>>
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
```  
<br/>

**선택 정렬의 시간 복잡도**  
* 선택 정렬은 N번 만큼 가장 작은 수를 찾아서 맨 앞으로 보내야 한다.
* 구현 방식에 따라서 사소한 오차가 있을 수 있지만, 전체 연산 횟수는 다음과 같다.  
<div align="center">
$N + (N - 1) + (N - 2) + ... + 2$
</div>    
<br/>  

* 이는 $(N^2 + N - 2) / 2$로 표현할 수 있는데, 빅오 표기법에 따라서 $O(N^2)$ 이라고 작성한다.

<br/>

## 📌 삽입 정렬
* 처리되지 않은 데이터를 하나씩 골라 **적절한 위치에 삽입** 하는 방법.
* 선택 정렬에 비해 구현 난이다고 높은 편이지만, 일반적으로 더 효율적으로 동작.
* 삽입 정렬은 특정한 데이터가 적절한 위치에 들어가기 이전에, 그 앞까지의 데이터는 이미 정렬되어 있다고 가정한다.
* 정렬되어 있는 데이터 리스트에서 적절한 위치를 찾은 뒤에, 그 위치에 삽입된다는 점이 특징이다.

<br/>

**삽입 정렬 동작 예시**
* **[Step 0]** 첫 번째 데이터 '7'은 그 자체로 정렬이 되어 있다고 판단하고, 두 번째 데이터인 '5'가 어떤 위치로 들어갈지 판단한다. '7'의 왼쪽으로 들어가거나 오른쪽으로 들어가거나 두 경우만 존재. 지금은 카드를 오름차순으로 정렬하고자 하므로 '7'의 왼쪽에 삽입한다.  
![image](https://user-images.githubusercontent.com/78528903/180974670-df71877b-36cd-4979-bb64-1d783c0e20db.png)

* **[Step 1]** 이어서 '9'가 어떤 위치로 들어갈지 판단한다. 삽입될 수 있는 위치는 총 3가지이며 현재 '9'는 '5'와 '7'보다 크기 때문에 원래 자리 그대로 둔다.  
![image](https://user-images.githubusercontent.com/78528903/180975254-9751b65d-7948-416c-af47-e6792cfc01c5.png)

* **[Step 2]** 이어서 '0'이 어떤 위치에 들어갈지 판단한다. '0'은 '5', '7', '9'와 비교했을 때 가장 작기 때문에 첫 번째 위치에 삽입한다.  
![image](https://user-images.githubusercontent.com/78528903/180975357-117acea6-d51e-4444-8479-40b75607018e.png)

* **[Step 3]** 이어서 '3'이 어떤 위치에 들어갈지 판단한다. '0'과 '5' 사이에 삽입한다.  
![image](https://user-images.githubusercontent.com/78528903/180975449-d8db98fa-5c4f-4fc1-8de8-f734461c5fa8.png)  
.  
.  
.  
* **[Step 7]**  
![image](https://user-images.githubusercontent.com/78528903/180975577-29847d8d-40f8-4867-96f0-01b6a2ac1e68.png)

* **[Step 8]**  
![image](https://user-images.githubusercontent.com/78528903/180975608-e3b38acb-1019-403b-a0ac-8b107e01153a.png)

* **[Step 9]** 이와 같이 적절한 위치에 삽입하는 과정을 N - 1번 박복하게 되면 다음과 같이 모든 데이터가 정렬된 것을 확인할 수 있다.  
![image](https://user-images.githubusercontent.com/78528903/180975731-8724e8e1-7bc5-4e37-9b6c-5005441c39b5.png)

삽입 정렬은 재밌는 특징이 있는데, 정렬이 이루어진 원소는 항상 오른차순(혹은 내림차순)을 유지하고 있다는 점이다.  
이러한 특징 때문에 삽입 정렬에서는 특정한 데이터가 삽입될 위치를 선정할 때(삽입될 위치를 찾기 위하여 왼쪽으로 한 칸씩 이동할 때), 삽입될 데이터보다 작은 데이터를 만나면 그 위치에서 멈추면 된다.  

예를 들어 [step 3]을 다시 살펴보자.  
![image](https://user-images.githubusercontent.com/78528903/180976159-24dbad39-6da6-4c6d-99a7-b4753a9eabef.png)  
[step 3]에서 '3'은 한 칸씩 왼쪽으로 이동하다가 자신보다 작은 '0'을 만났을 때 그 위치에 삽입된다.
다시 말해 특정한 데이터의 왼쪽에 있는 데이터들은 이미 정렬이 된 상태이므로 자기보다 작은 데이터를 만났다면 더 이상 데이터를 살펴볼 필요 없이 그 자리에 삽입되면 되는 것이다.

<br/>

> 삽입 정렬 
```python
array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(1, len(array)):
    for j in range(i, 0, -1): # 인덱스 i부터 1까지 감소하며 반복
        if array[j] < array[j - 1]: # 한 칸씩 왼쪽으로 이동
            array[j], array[j - 1] = array[j - 1], array[j]
        else: # 자기보다 작은 데이터를 만나면 그 위치에서 멈춤
            break

print(array)

>>>
[1, 2, 3, 4, 5, 6, 7, 8, 9]
```
<br/>

**삽입 정렬의 시간 복잡도**  
* 삽입 정렬의 시간 복잡도는 $O(N^2)$ 이며, 선택 정렬과 마찬가지로 반복문이 두 번 중첩되어 사용된다.
* 삽입 정렬은 **현재 리스트의 데이터가 거의 정렬되어 있는 상태라면 매우 빠르게 동작한다.**
    * 최선의 경우 $O(N)$의 시간 복잡도를 가진다.

<br/>

## 📌 퀵 정렬
* **기준 데이터를 설정** 하고 그 **기준보다 큰 데이터와 작은 데이터의 위치를 바꾸는 방법**
* 일반적인 상황에서 가장 많이 사용되는 정렬 알고리즘 중 하나
* 병합 정렬과 더불어 대부분의 프로그래밍 언어의 정렬 라이브러리의 근간이 되는 알고리즘
* 가장 기본적인 퀵 정렬은 호어 분할(Hoare Partition) 방식인 **첫 번째 데이터를 기준 데이터(Pivot)로 설정**
* **기준을 설정한 다음 큰 수와 작은 수를 교환한 후 리스트를 반으로 나누는 방식으로 동작**

<br/>

**퀵 정렬 동작 예시**   
다음과 같은 초기 데이터가 있다고 가정해보자.  
![image](https://user-images.githubusercontent.com/78528903/180999488-767dce7f-53e1-4af8-81cd-9cfca0d0c758.png)  
퀵 정렬은 전체를 3개의 파트로 나눠서 보는 게 편하다. $I$, $II$, $III$ 파트로 나눠서 보자.

> $I$ 파트
* **[Step 0]**  
리스트의 첫 번째 데이터를 피벗으로 설정하므로 피벗은 '5'이다.  
이후에 **왼쪽에서부터 '5'보다 큰 데이터를 선택** 하므로 '7'이 선택되고, **오른쪽에서부터 '5'보다 작은 데이터를 선택** 하므로 '4'가 선택된다.  
이제 이 두 데이터의 위치를 서로 변경한다.  
![image](https://user-images.githubusercontent.com/78528903/181000140-43b30556-0b2b-4cc0-9f0f-eac612e42450.png)

* **[Step 1]**  
그 다음 다시 피벗보다 큰 데이터와 작은 데이터를 각각 찾는다.  
찾은 뒤에는 두 값의 위치를 서로 변경하는데, 현재 '9'와 '2'가 선택되었으므로 이 두 데이터의 위치를 서로 변경한다.  
![image](https://user-images.githubusercontent.com/78528903/181000252-a0eae6b8-513a-4264-bb2c-57c5441dc029.png)

* **[Step 2]**  
그 다음 다시 피벗보다 큰 데이터와 작은 데이터를 찾는다.  
단, **현재 왼쪽에서부터 찾는 값과 오른쪽에서부터 찾는 값의 위치가 서로 엇갈린 것** 을 알 수 있다.  
이렇게 **두 값이 엇갈린 경우** 에는 **'작은 데이터'와 '피벗'의 위치를 서로 변경** 한다.  
즉, 작은 데이터은 '1'과 피벗인 '5'의 위치를 서로 변경하여 분할을 수행한다.  
![image](https://user-images.githubusercontent.com/78528903/181000533-0c4e42e3-c80e-4143-a10c-b5bed6d666c5.png)

* **[Step 3]** **분할 완료**  
이와 같이 피벗이 이동한 상태에서 왼쪽 리스트와 오른쪽 리스트를 살펴보자.  
이제 '5'의 왼쪽에 있는 데이터는 모두 '5'보다 작고, 오른쪽에 있는 데이터는 모두 '5'보다 크다는 특징이 있다.  
이렇게 피벗의 왼쪽에는 피벗보다 작은 데이터가 위치하고, 피벗의 오른쪽에는 피벗보다 큰 데이터가 위치하도록 하는 작업을 분할(Devide) 혹은 파티션(Partition) 이라고 한다.  
![image](https://user-images.githubusercontent.com/78528903/181000786-50f80080-b55b-4bf5-a807-907499c66f72.png)  
왼쪽 리스트와 오른쪽 리스트에서도 각각 피벗을 설정하여 동일한 방식으로 정렬을 수행하면 전체 리스트에 대하여 모두 정렬이 이루어질 것이다.  

> $II$ 파트  

왼쪽 리스트에서는 다음 그림과 같이 정렬이 진행되며 구체적인 정렬 과정은 동일하다.  
![image](https://user-images.githubusercontent.com/78528903/181001386-15e6aa04-a0af-41ac-bd15-3dff31d05f96.png)

> $III$ 파트  

오른쪽 리스트에서는 다음 그림과 같이 정렬이 진행되며 구체적인 정렬 과정은 동일하다.  
![image](https://user-images.githubusercontent.com/78528903/181001396-71cca18b-1654-4146-a995-1a928a8b1d2b.png)

**퀵 정렬이 빠른 이유: 직관적인 이해**  
* 이상적인 경우 분할이 절반씩 일어난다면 전체 연산 횟수로는 $O(NlogN)$를 기대할 수 있다.
    * **너비 X 높이** = $N \times logN = NlogN$  
![image](https://user-images.githubusercontent.com/78528903/181002122-a91ea7be-308a-428f-a10f-6df1aa70642a.png)

**퀵 정렬의 시간 복잡도**  
* 퀵 정렬은 평균의 경우 $O(NlogN)$의 시간 복잡도를 가진다.
* 이상적인 경우 분할이 절반씩 일어난다면 전체 연산 횟수로는 $O(NlogN)$를 기대할 수 있다.  
![image](https://user-images.githubusercontent.com/78528903/181002773-55a5341f-3425-4656-8713-a293eb7c1243.png)
  * 다시 말해 분할이 이루어지는 횟수가 기하급수적으로 감소하게 되는 것이다.
* 하지만 최악의 경우 $O(N^2)$의 시간 복잡도를 가진다.
    * 첫 번째 원소를 피벗으로 삼을 때, 이미 정렬된 배열에 대해서 퀵 정렬을 한다면?

<br/>

> 일반적인 방식
```python
array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]

def quick_sort(array, start, end):
    if start >= end: # 원소가 1개인 경우 종료
        return
    pivot = start # 피벗은 첫 번째 원소
    left = start + 1
    right = end
    while(left <= right):
        # 피벗보다 큰 데이터를 찾을 때까지 반복
        while(left <= end and array[left] <= array[pivot]):
            left += 1
        while(right > start and array[right] >= array[pivot]):
            right -= 1
        if(left > right): # 엇갈렸다면 작은 데이터와 피벗을 교체
            array[right], array[pivot] = array[pivot], array[right]
        else: # 엇갈리지 않았다면 작은 데이터와 큰 데이터를 교체
            array[left], array[right] = array[right], array[left]
    # 분할 이후 왼쪽 부분과 오른쪽 부분을 각각 정렬 수행
    quick_sort(array, start, right - 1)
    quick_sort(array, right + 1, end)
    
quick_sort(array, 0, len(array) - 1)
print(array)

>>>
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
```
<br/>

> 파이썬의 장점을 살린 방식
```python
array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]

def quick_sort(array):
    # 리스트가 하나 이하의 원소만을 담고 있다면 종료
    if len(array) <= 1:
        return array
    pivot = array[0] # 피벗은 첫 번째 원소
    tail = array[1:] # 피벗을 제외한 리스트
    
    left_side = [x for x in tail if x <= pivot] # 분할된 왼쪽 부분
    right_side = [x for x in tail if x > pivot] # 분할된 오른쪽 부분
    
    # 분할 이후 왼쪽 부분과 오른쪽 부분에서 각각 정렬 수행하고, 전체 리스트 반환
    return quick_sort(left_side) + [pivot] + quick_sort(right_side)
    
print(quick_sort(array))

>>>
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
```

<br/>

## 📌 계수 정렬
* 특정한 조건이 부합할 때만 사용할 수 있지만 **매우 빠르게 동작하는** 정렬 알고리즘
    * 계수 정렬은 **데이터의 크기 범위가 제한되어 정수 형태로 표현할 수 있을 때** 사용 가능
    * 예를 들어 데이터의 값이 무한한 범위를 가질 수 있는 실수형 데이터가 주어지는 경우 계수 정렬은 사용하기 어렵다.
    * 일반적으로 가장 큰 데이터와 가장 작은 데이터의 차이가 1,000,000을 넘지 않을 때 효과적으로 사용할 수 있다.
* 데이터의 개수가 N, 데이터(양수) 중 최댓값이 K일 때 최악의 경우에도 수행 시간 $O(N + K)$를 보장!!

<br/>

**계수 정렬 동작 예시**  
* **[Step 0]** 계수정렬은 먼저 가장 작은 데이터부터 가장 큰 데이터까지의 범위가 모두 담길 수 있도록 하나의 리스트를 생성한다.  
정렬할 데이터: 7 5 9 0 3 1 6 2 9 1 4 8 0 5 2  
![image](https://user-images.githubusercontent.com/78528903/181006214-5b371678-fc5b-4e16-9cdd-df5cb6f8f94f.png)

* **[Step 1]** 데이터를 하나씩 확인하며 데이터의 값과 동일한 인덱스의 데이터를 1씩 증가시킨다.  
![image](https://user-images.githubusercontent.com/78528903/181006484-86e56d7a-e788-4099-9d70-85c428b3172b.png)

* **[Step 2]** 데이터를 하나씩 확인하며 데이터의 값과 동일한 인덱스의 데이터를 1씩 증가시킨다.  
![image](https://user-images.githubusercontent.com/78528903/181006585-270de41b-0871-4be8-b109-437f5fe2718d.png)

* **[Step 3]** 데이터를 하나씩 확인하며 데이터의 값과 동일한 인덱스의 데이터를 1씩 증가시킨다.  
![image](https://user-images.githubusercontent.com/78528903/181006635-f5cd71de-25a8-4af9-8fbd-e417fc7a12ab.png)  
.  
.  
.  
* **[Step 15]** 결과적으로 최종 리스트에는 각 데이터가 몇 번씩 등장했는지 그 횟수가 기록된다.  
![image](https://user-images.githubusercontent.com/78528903/181006716-8069bddc-2f65-4ff3-8670-7a9570b10af3.png)

* **[Step 16]** 결과를 확인할 때는 리스트의 첫 번째 데이터부터 하나씩 그 값만큼 반복하여 인덱스를 출력한다.  
![image](https://user-images.githubusercontent.com/78528903/181006881-baf941f4-2117-4f12-9be0-c5a6721231de.png)

<br/>

> 계수 정렬 소스코드
```python
# 모든 원소의 값이 0보다 크다고 가정
array = [7, 5, 9, 0, 3, 1, 6, 2, 9, 1, 4, 8, 0, 5, 2]
# 모든 범위를 포함하는 리스트 선언(모든 값은 0으로 초기화)
count = [0] * (max(array) + 1)

for i in range(len(array)):
    count[array[i]] += 1 # 각 데이터에 해당하는 인덱스의 값 증가
    
for i in range(len(count)): # 리스트에 기록된 정렬 정보 확인
    for j in range(count[i]):
        print(i, end=' ')

>>>
0 0 1 1 2 2 3 4 5 5 6 7 8 9 9
```
<br/>

**계수 정렬의 복잡도 분석**
* 계수 정렬의 시간 복잡도와 공간 복잡도는 모두 $O(N + K)$ 이다.
* 계수 정렬은 때에 따라서 심각한 비효율성을 초래할 수 있다.
    * 데이터가 0과 999,999로 단 2개만 존재하는 경우...
* 계수 정렬은 **동일한 값을 가지는 데이터가 여러 개 등장할 때** 효과적으로 사용할 수 있다.
    * 성적의 경우 100점을 맞은 학생이 여러 명일 수 있기 때문에 계수 정렬이 효과적이다.

<br/>

## 📌 버블 정렬  
* 이웃한 두 값을 비교하여 정렬한다. 큰 값이 오론쪽으로 이동하는 과정이 반복되면서 비교했던 모든 값들의 최댓값이 맨 오른쪽으로 옮겨지게 된다.  
![gif](https://images.velog.io/images/jguuun/post/d02f445e-1936-4333-a703-642c0431db03/Bubble-sort.gif)
* 최악의 경우 $(N-1) + (N-2) + \cdots + 1$번 비교가 이루어지므로 $O(N^2)$이다. 그러나, 데이터가 잘 졍렬돼있다면 $O(N)$이므로 데이터의 정렬 여부를 파악하기 위한 알고리즘으로 사용될 수 있다. 

<br/>

> 버블 정렬 소스코드  
```python
def bubblesort(arr):
    
    length = len(arr) - 1
    
    for i in range(length):
        isSort = False
        
        for j in range(length-i):
            if(arr[j] > arr[j+1]):
                arr[j], arr[j+1] = arr[j+1], arr[j]
                isSort = True
                
        if isSort == False:
            break
                
    return arr
```
<br/>

## 📌 병합 정렬(Merge Sort)
* 폰 노이만이 개발했으며, 두 부분으로 쪼개는 작업을 재귀적으로 반복한 뒤, 쪼갠 순서의 반대로 작은 값부터 병합해나가는 분할 정복 알고리즘의 일종이다.  
![gif](http://ejklike.github.io/assets/20170301/mergesort.gif)

* 두 부분으로 쪼개는 데 $O(\log N)$ (이진탐색 참고)이고, 데이터 병합이 $O(N)$이므로, 정렬 상태와 무관하게 언제나 $O(N\log N)$이다. 데이터 크기만한 메모리가 더 필요한 게 단점이다.  
<br/>

> 병합 정렬 소스코드
```python
array = [8,4,6,2,9,1,3,7,5]

def merge_sort(array):
    # 두 부분으로 쪼개는 작업을 재귀적으로 반복
    if len(array) < 2:
    	return array
    mid = len(array) // 2
    low_arr = merge_sort(array[:mid])
    high_arr = merge_sort(array[mid:])
    
    # 쪼갠 순서의 반대로 작은 값부터 병합
    merged_arr = []
    l = h = 0
    while l < len(low_arr) and h < len(high_arr):
    	if low_arr[l] < high_arr[h]:
    		merged_arr.append(low_arr[l])
    		l += 1
    	else:
    		merged_arr.append(high_arr[h])
    		h += 1
    merged_arr += low_arr[l:]
    merged_arr += high_arr[h:]
    print(merged_arr)
    return merged_arr

print("before: ",array)
array = merge_sort(array)
print("after:", array)

>>>
before: [8, 4, 6, 2, 9, 1, 3, 7, 5]
[4, 8]
[2, 6]
[2, 4, 6, 8]
[1, 9]
[5, 7]
[3, 5, 7]
[1, 3, 5, 7, 9]
[1, 2, 3, 4, 5, 6, 7, 8, 9]
after: [1, 2, 3, 4, 5, 6, 7, 8, 9]
```

<br/>

## 📌 정렬 알고리즘 비교하기

|Name|Best|Worst|Stable|Memory|
|:---:|:---:|:---:|:---:|:---:|
|버블정렬|$n$|$n^2$|True|1|
|선택정렬|$n^2$|$n^2$|False|1|
|삽입정렬|$n$|$n^2$|True|1|
|병합정렬|$n\log n$|$n\log n$|True|$n$|
|퀵정렬|$n\log n$|$n\log n$ ~ $n^2$|False|	$\log n$ ~ $n$|
