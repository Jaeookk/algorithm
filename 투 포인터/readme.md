# 투 포인터 (Two Pointers)
* **투 포인터 알고리즘** 은 리스트에 순차적으로 접근해야 할 때 두 개의 점의 위치를 기록하면서 처리하는 알고리즘을 의미한다
* 배열에서 원래는 이중 for문으로 탐색을 해야한다면 O(N^2)이다. 그런데 포인터 2개를 두고 그 포인터를 잘 움직여서 O(N)에 해결하는게 투 포인터 알고리즘입니다. 
* 여기서 포인터라고 하는건 C에서 사람들을 굉장히 괴롭게 했던 int*와 같은 포인터는 아니고, 그냥 커서라고 생각을 하면 됩니다. 
* 그러면 왜 이렇게 시간복잡도를 줄일 수 있는거냐?
    * 이중 for문에서는 i = 0일 때 j가 0부터 n-1까지 돌고, i = 1일 때 j가 0부터 n-1까지 돌고, 이와 같이 각 i에 대해서 j가 0부터 n-1까지 돕니다. 그리고 이 과정에서 i = 0일 때 계산하면서 얻은 정보가 i = 1일 때에 전혀 쓰이지가 않습니다. 
    * 투 포인터에서는 i = 0일 때 계산하면서 얻은 정보를 i = 1일 때 활용합니다. 그 정보가 포인터의 이동으로 나타납니다.
* 리스트에 담긴 데이터에 순차적으로 접근해야 할 때는 **시작점** 과 **끝점** 2개의 점으로 접근할 데이터의 범위를 표현할 수 있다

<br/>

# 특정한 합을 가지는 부분 연속 수열 찾기: 문제 설명
* N개의 자연수로 구성된 수열이 있다
* **합이 M인 부분 연속 수열의 개수** 를 구하라
* 수행 시간 제한은 **O(N)** 이다

![image](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FmZ77y%2FbtqSATOPeoU%2FNYTJrfoQukTtW1iUNvhOg1%2Fimg.png)

<br/>

# 특정한 합을 가지는 부분 연속 수열 찾기: 문제 해결 아이디어
* 투 포인터를 활용하여 다음과 같은 **알고리즘** 으로 문제를 해결할 수 있다
    1. 시작점(start)과 끝점(end)이 첫 번째 원소의 인덱스(0)를 가리키도록 한다
    2. 현재 부분 합이 M과 같다면, 카운트한다
    3. 현재 부분 합이 M보다 작다면, end를 1 증가시킨다 
    4. 현재 부분 합이 M보다 크거나 같다면, start를 1 증가시킨다
    5. 모든 경우를 확인할 때까지 2번부터 4번까지의 과정을 반복한다

    ![image](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2Fb9LKEz%2FbtqSxA26YQn%2Fn2uliiFHWe7VeKstud2CWk%2Fimg.png)

* **𝑀 = 5**
* **[초기 단계]** 시작점과 끝점이 첫 번째 원소의 인덱스를 가리키도록 한다
    * 현재의 부분합은 1이므로 무시한다
    * **현재 카운트** : 0

    ![image](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2Fs7cCt%2FbtqSjBB3hlS%2Fyw4cdKIKzauPU1lfqeEfT0%2Fimg.png)

* **[Step 1]** 이전 단계에서의 부분합이 1이었기 때문에 end를 1 증가시킨다
    * 현재의 부분합은 3이므로 무시한다
    * **현재 카운트** : 0

    ![imag](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2Fb2ebQb%2FbtqSpF4XAfj%2FQdZlLTXkd4kD0K6wNyilB0%2Fimg.png)

* **[Step 2]** 이전 단계에서의 부분합이 3이었기 때문에 end를 1 증가시킨다
    * 현재의 부분합은 6이므로 무시한다
    * **현재 카운트** : 0

    ![img](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FlxEwk%2FbtqSjB29uzW%2Fv8kM14wTrceGCxlVHEmDL0%2Fimg.png)

* **[Step 3]** 이전 단계에서의 부분합이 6이었기 때문에 start를 1 증가시킨다
    * 현재의 부분합은 5이므로 카운트를 증가시킨다
    * **현재 카운트** : 1

    ![img](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2Fby9sIr%2FbtqSGi77a2r%2FbBPoOR5DWT4SYc6KUwKSl1%2Fimg.png)

* **[Step 4]** 이전 단계에서의 부분합이 5이었기 때문에 start를 1 증가시킨다
    * 현재의 부분합은 3이므로 무시한다
    * **현재 카운트** : 1

    ![img](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FlSS8A%2FbtqSDvfQCbm%2FqKfuTcENk9y3P6kbk86Qtk%2Fimg.png)

* **[Step 5]** 이전 단계에서의 부분합이 3이었기 때문에 end를 1 증가시킨다
    * 현재의 부분합은 5이므로 카운트를 증가시킨다
    * **현재 카운트** : 2

    ![img](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FbD0TJq%2FbtqSEKjvjSj%2FOEK6GwawUKTQ1Q3xkz9p60%2Fimg.png)

* **[Step 6]** 이전 단계에서의 부분합이 5이었기 때문에 start를 1 증가시킨다
    * 현재의 부분합은 2이므로 무시한다
    * **현재 카운트** : 2

    ![img](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FFR7fq%2FbtqSDvz89n7%2FkQfxbBdyLL44k4kYBM3A41%2Fimg.png)

* **[Step 7]** 이전 단계에서의 부분합이 2였기 때문에 end를 1 증가시킨다
    * 현재의 부분합은 7이므로 무시한다
    * **현재 카운트** : 2

    ![img](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FXlFqP%2FbtqSmAQnAxL%2Fx5OKK8hKlFd97IF2PerSnk%2Fimg.png)

* **[Step 8]** 이전 단계에서의 부분합이 7이었기 때문에 start를 1 증가시킨다
    * 현재의 부분합은 5이므로 카운트를 증가시킨다
    * **현재 카운트** : 3

    ![img](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2Fbm32FQ%2FbtqSpGpge76%2FKtsUTpY7kby8QVz0UnSlk1%2Fimg.png)

<br/>

# 특정한 합을 가지는 부분 연속 수열 찾기: 코드 예시 (Python)
```python
n = 5 # 데이터의 개수 N
m = 5 # 찾고자 하는 부분합 M
data = [1, 2, 3, 2, 5] # 전체 수열

count = 0
interval_sum = 0
end = 0

# start를 차례대로 증가시키며 반복
for start in range(n):
    # end를 가능한 만큼 이동시키기
    while interval_sum < m and end < n:
        interval_sum += data[end]
        end += 1
    # 부분합이 m일 때 카운트 증가
    if interval_sum == m:
        count += 1
    interval_sum -= data[start]

print(count)
```

실행 결과
```python
3
```