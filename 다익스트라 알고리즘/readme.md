# 다익스트라 (Dijkstra)

> 다익스트라 알고리즘은 그래프에서 여러 개의 노드가 있을 대, 특정한 노드에서 출발하여 다른 노드로 가는 각각의 최단 경로를 구해주는 알고리즘이다.

* 다익스트라 알고리즘은 **"음의 간선"** 이 없을 때 정상적으로 동작한다.
  * 음의 간선 : 0보다 작은 값을 가지는 간선  

* 다익스트라 알고리즘은 기본적으로 **그리디 알고리즘** 으로 분류된다.  

매번 "가장 비용이 적은 노드"를 선택해서 임의의 과정을 반복하기 때문이다.

다익스트라 알고리즘의 원리를 간략히 설명하면 다음과 같다.

1. 출발 노드를 선정한다.

2. 최단 거리 테이블을 초기화한다.

3. **방문하지 않은 노드 중에서 최단 거리가 가장 짧은 노드를 선택한다.**

4. 해당 노드를 거쳐 다른 노드로 가는 비용을 계산하여 최단 거리 테이블을 갱신한다.

5. 위 과정에서 `3`과 `4`번을 반복한다.

다익스트라 알고리즘은 최단 경로를 구하는 과정에서 "각 노드에 대한 현재까지의 최단 거리" 정보를 항상 **1차원 리스트** 에 저장하며 리스트를 계속 갱신한다는 특징이 있다. 이러한 1차원 리스트를 최단 거리 테이블이라고 한다.

매번 현재 처리하고 있는 노드를 기준으로 주변 간선을 확인한다.

나중에 현재 처리하고 있는 노드와 인접한 노드로 도달하는 더 짧은 경로를 찾으면, "더 짧은 경로도 있었네? 이제부터 이 경로가 가장 짧은 경로야" 라고 판단하는 것이다.

따라서 "방문하지 않은 노드 중에서 현재 최단 거리가 가장 짧은 노드를 확인"해 그 노드에 대하여 `4`번 과정을 수행한다는 점에서 그리디 알고리즘으로 볼 수 있다.

<br/>

## 동작 원리
이제 다익스트라 알고리즘의 동작 원리를 그림과 함께 살펴보자. 아래와 같은 그래프가 있을 때 1번 노드에서 다른 모든 노드로 가는 최단 경로를 구하는 문제를 생각해보자.

![](https://velog.velcdn.com/images/wodnr0710/post/fee2990a-2adc-473d-abfb-6ff5d1f62a69/image.png)

예시에서 출발 노드를 1이라 하자. 1번 노드에서 다른 모든 노드로의 최단 거리를 계산해볼 것이다.

초기 상태에서는 다른 모든 노드로 가는 최단거리를 "무한"으로 초기화 한다.
> Tip. 가장 간단한 방법은 `1e9`를 사용하는 건데, 파이썬에서 기본으로 `1e9`를 실수 자료형으로 처리하므로, `int(1e9)`를 사용하자.

* step0  
먼저 방문하지 않은 노드 중에서 최단 거리가 가장 짧은 노드를 선택하는데, 출발 노드에서 출발 노드로의 거리는 `0`으로 보기 때문에 처음에는 출발 노드가 선택된다.  
![](https://velog.velcdn.com/images/wodnr0710/post/a3f0f3ac-8810-4c96-ab62-f51f5122a4b1/image.png)

* step1  
이제 **1번 노드를** 거쳐 다른 노드로 가는 비용을 계산한다. 즉, **1번 노드와** 연결된 모든 간선을 하나씩 확인하면 된다. 현재 1번 노드까지 오는 비용은 `0`이므로, 1번 노드를 거쳐서 2번, 3번, 4번 노드로 가는 최소 비용은 차례로 2(0 + 2), 5(0 + 5), 1(0 + 1)이다. 현재 2번, 3번, 4번 노드로 가는 비용이 "무한"으로 설정되어 있는데, 세 노드에 대하여 더 짧은 경로를 찾았으므로 각각 새로운 값으로 갱신한다. 처리된 결과는 아래 그림과 같다.  
![](https://velog.velcdn.com/images/wodnr0710/post/005851a5-f1b3-42ec-8464-8dc6b13af53d/image.png)  
![](https://velog.velcdn.com/images/wodnr0710/post/95037121-810e-40f4-9938-99623138a5d1/image.png)

* step2  
이후의 모든 단계에서도 마찬가지로 방문하지 않은 노드 중에서 최단 거리가 가장 짧은 노드를 선택해야 한다. 따라서 [step2]에서는 **4번 노드가** 선택된다. 이어서 **4번 노드를** 거쳐서 갈 수 있는 노드를 확인한다. 4번 노드에서 갈 수 있는 노드는 3번과 5번이다. 이대 4번 노드까지의 최단 거리는 1이므로 4번 노드를 거쳐서 3번과 5번 노드로 가는 최소 비용은 차례대로 4(1 + 3), 2(1 + 1) 이다. 이 두 값은 기존의 리스트에 담겨 있던 값보다 작으므로 아래처럼 리스트가 갱신된다.  
![](https://velog.velcdn.com/images/wodnr0710/post/82c67673-6b7c-4bb7-b24d-77543a55fe05/image.png)  
![](https://velog.velcdn.com/images/wodnr0710/post/46b60f22-843c-46f0-a212-0fd0f3fedd03/image.png)

* step3  
[step 3]에서는 **2번 노드가** 선택된다. 2번과 5번 노드까지의 최단 거리가 2로 값이 같은데, 이럴때는 일반적으로 번호가 작은 노드를 선택한다. 그리고 2번 노드를 거쳐서 도달할 수 있는 노드 중에서 거리가 더 짧은 경우가 있는지 확인한다. 이번 단계에서는 2번 노드를 거쳐서 가는 경우, 현재의 최단 거리를 더 짧게 갱신할 수 있는 방법은 없다.  
![](https://velog.velcdn.com/images/wodnr0710/post/fe55a6de-0426-47b4-bbf6-59c5885952eb/image.png)  
![](https://velog.velcdn.com/images/wodnr0710/post/f14e34df-72db-42bf-a8d4-ac2c16896023/image.png)

* step4  
[step 4]에서는 **5번 노드가** 선택된다. 5번 노드를 거쳐 3번과 6번 노드로 갈 수 있다. 현재 5번 노드까지 가는 최단 거리가 2이므로 5번 노드에서 3번 노드로 가는 거리인 1을 더한 3이 기존 값인 4보다 작기 때문에 새로운 값 3으로 갱신된다. 또한 6번 노드로 가는 거리도 마찬가지로 4로 갱신된다.  
![](https://velog.velcdn.com/images/wodnr0710/post/7bcde798-15bd-4bc8-883c-41c0b0a3a1e0/image.png)  
![](https://velog.velcdn.com/images/wodnr0710/post/2f2913de-4298-4b0d-be39-9039bbff4818/image.png)

* step5  
이어서 **3번 노드를** 선택한 다음 동일한 과정을 반복한다.  
![](https://velog.velcdn.com/images/wodnr0710/post/06a6cc5e-04c6-4412-a4c2-63666033a592/image.png)  
![](https://velog.velcdn.com/images/wodnr0710/post/6b450cab-926c-41d2-a436-c46f738cc58a/image.png)

* step6  
**6번 노드를** 선택한 후 같은 과정을 반복한다.  
![](https://velog.velcdn.com/images/wodnr0710/post/6c35cb27-f3a1-4ec5-9f26-a442beab61c3/image.png)  
![](https://velog.velcdn.com/images/wodnr0710/post/8faac895-a47c-4e39-a84b-e4b648523e9b/image.png)

최단 거리 테이블이 의미하는 바는 1번 노드로부터 출발했을 때 각 노드까지 가기 위한 최단 경로가 각각 2, 3, 1, 2, 4라는 의미다.

다익스트라 알고리즘에서는 **"방문하지 않은 노드 중에서 가장 최단 거리가 짧은 노드를 선택"** 하는 과정을 반복하는데, 이렇게 선택된 노드는 **"최단 거리"가 완전히 선택된 노드**이므로, 더 이상 **알고리즘을 반복해도 최단 거리가 줄어들지 않는다.**

예를 들어 [step 2]에서는 4번노드가	선택되어서 4번노드를	거쳐서	이동할	수 있는 경로를 확인했다. 이후에 [step 3] ~ [step 6]이 진행되었으나, 4번 노드에 대한 최단 거리는 더 이상 감소하지 않았다. 

다시 말해 다익스트라	알고리즘이 진행되면서	**한 단계당 하나의 노드에 대한 최단	거리를	확실히	찾는 것으로 이해할 수 있다.**

이제 실제로 알고리즘을 구현해보자.

<br/>

## 구현
다익스트라 일고리즘을	구현하는 방법은 2가지다.
* 방법 1.	구현하기 쉽지만 느리게 동작하는 코드
* 방법 2.	구현하기에 조금 더 까디롭지만 빠르게 동작하는 코드

### 방법 1. 간단한 다익스트라 알고리즘
간단한 다익스트라 알고리즘은 $O(V^2)$의 시간 복잡도를 가진다.

왜냐하면 총 $O(V)$번에 걸쳐서 최단 거리가 가장 짧은 노드를 매번 선형 탐색해야 하고, 현재 노드와 연결된 노드를 매번 일일이 확인하기 때문이다.

때문에 해당 코드는 노드의 개수가 5000개 이하 일때 일반적으로 사용할 수 있다.

```python
import sys

input = sys.stdin.readline
INF = int(1e9)

# 노드의 개수, 간선의 개수
n, m = map(int, input().split())
# 시작 노드 번호 입력 받기
start = int(input())
# 각 노드에 연결되어 있는 노드에 대한 정보를 담는 리스트 만들기
graph = [[] for _ in range(n + 1)]
# 방문 체크를 위한 리스트 만들기
visited = [False] * (n + 1)
# 최단 거리 테이블을 모두 무한으로 초기화
distance = [INF] * (n + 1)

# 모든 간선 정보를 입력받기
for _ in range(m):
    a, b, c = map(int, input().split())
    # a번 노드에서 b번 노드로 가는 비용이 c라는 의미
    graph[a].append((b, c))


# 방문하지 않은 노드 중에서, 가장 최단 거리가 짧은 노드의 번호를 반환
def get_smallest_node():
    min_value = INF
    index = 0  # 가장 최단 거리가 짧은 노드(인덱스)
    for i in range(1, n + 1):
        if distance[i] < min_value and not visited[i]:
            min_value = distance[i]
            index = i
    return index


def dijkstra(start):
    # 시작 노드에 대해서 초기화
    distance[start] = 0
    visited[start] = True
    for next in graph[start]:
        distance[next[0]] = next[1]

    # 시작 노드를 제외한 전체 n-1개의 노드에 대해 반복
    for i in range(n - 1):
        # 현재 최단 거리가 가장 짧은 노드를 꺼내서, 방문 처리
        now = get_smallest_node()
        visited[now] = True
        # 현재 노드와 연결된 다른 노드를 확인
        for next in graph[now]:
            cost = distance[now] + next[1]
            # 현재 노드를 거쳐서 다른 노드로 이동하는 거리가 더 짧은 경우
            if cost < distance[next[0]]:
                distance[next[0]] = cost


# 다익스트라 알고리즘 수행
dijkstra(start)

# 모든 노드로 가기 위한 최단 거리를 출력
for i in range(1, n + 1):
    # 도달할 수 없는 경우 INF라고 출력
    if distance[i] == INF:
        print("INF")
    else:
        print(distance[i])

"""
입력
6 11
1
1 2 2
1 3 5
1 4 1
2 3 3
2 4 2
3 2 3
3 6 5
4 3 3
4 5 1
5 3 1
5 6 2

출력
0 2 3 1 2 4
"""
```  
<br/>

### 방법 2. 개선된 다익스트라 알고리즘
개선된 다익스트라 알고리즘은 최악의 경우에도 $O(ElogV)$를 보장한다. V는 노드의 수, E는 간선의 수다.

간단한 다익스트라 알고리즘은 "최단	거리가	가장 짧은 노드"를 찾기 위해서, 매번 최단 거리 테이블을 선형적으로(모든 원소를 앞에서부터	하나씩) 탐색해야 했다. 이 과정에서만 $O(V)$의 시간이 걸렸다.

하지만	최단 거리가 가장 짧은 노드를 단순히 선형적으로 찾는 것이 아니라 더욱 빠르게 찾
을 수	있다면 알고리즘의 시간 복잡도를 더욱 줄일 수 있을 것이다.

개선된	다익스트라 알고리즘에서는 **힙 자료구조를** 사용한다.

힙 자료구조를	이용하게 되면 특정 노드까지의 최단 거리에 대한 정보를 힙에 담아서 처리하므로 출발 노드로부터 가장 거리가 짧은 노드를 더욱 빠르게 찾을 수 있다.

왜냐하면 이 과정에서 선형 시간이 아닌 로그 시간이 걸리기 때문이다.

최소힙을 이용하는 경우 힙에서 원소를 꺼내면 "가장 값이 작은 원소"가 추출되는 특징이 있으며, 파이썬의 우선순위 큐 라이브러리(heapq)는 최소힙에 기반한다는 점을 기억하자. 
우리는	이러한	최소힙을 다익스트라 알고리즘에 적용할 것이다. 

단순히 우선순위 큐를 이용해서 시작 노드로부터 "거리"가 짧은 노드 순서대로 큐에서 나올 수 있도록 다익스트라 알고리즘을 작성하면 된다.

우선순위 큐를 적용하여도 다익스트라 알고리즘이 동작하는 **기본원리는 동일**하다.

최단 거리를 저장하기 위한 1차원 리스트(최단 거리 테이블)는 아까와 같이 그대로 이용하고, **현재 가장 가까운 노드를 저장하기 위한 목적으로만 우선순위 큐를 추가로 이용한다고 보면 된다.**	

즉, 앞의 코드와 비교했을 때 `get_smallest_node()`라는 함수를 작성할 필요가 없다.

"최단 거리가 가장 짧은 노드"를 선택하는 과정을 우선순위 큐를 이용하는 방식으로 대체하기 때문이다.

```python
import sys
import heapq

input = sys.stdin.readline
INF = int(1e9)

# 노드의 개수, 간선의 개수
n, m = map(int, input().split())
# 시작 노드 번호 입력 받기
start = int(input())
# 각 노드에 연결되어 있는 노드에 대한 정보를 담는 리스트 만들기
graph = [[] for _ in range(n + 1)]
# 최단 거리 테이블을 모두 무한으로 초기화
distance = [INF] * (n + 1)

# 모든 간선 정보를 입력받기
for _ in range(m):
    a, b, c = map(int, input().split())
    # a번 노드에서 b번 노드로 가는 비용이 c라는 의미
    graph[a].append((b, c))


def dijkstra(start):
    q = []
    # 시작 노드로 가기 위한 최단 경로는 0으로 설정하여, 큐에 삽입
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:  # 큐가 비어있지 않다면
        # 가장 최단 거리가 짧은 노드에 대한 정보 꺼내기
        dist, now = heapq.heappop(q)
        # 현재 노드가 이미 처리된 적이 있는 노드라면 무시 (visited 대체)
        if distance[now] < dist:
            continue
        # 현재 노드와 연결된 다른 인접한 노드들을 확인
        for next in graph[now]:
            cost = dist + next[1]
            # 현재 노드를 거쳐서, 다른 노드로 이동하는 거리가 더 짧은 경우
            if cost < distance[next[0]]:
                distance[next[0]] = cost
                heapq.heappush(q, (cost, next[0]))


# 다익스트라 알고리즘 수행
dijkstra(start)

# 모든 노드로 가기 위한 최단 거리를 출력
for i in range(1, n + 1):
    # 도달할 수 없는 경우 INF라고 출력
    if distance[i] == INF:
        print("INF")
    else:
        print(distance[i], end=" ")

"""
입력
6 11
1
1 2 2
1 3 5
1 4 1
2 3 3
2 4 2
3 2 3
3 6 5
4 3 3
4 5 1
5 3 1
5 6 2

출력
0 2 3 1 2 4
"""
```

노드를	하나씩 꺼내 검사하는 반복문(while문)은 노드의 개수	V 이상의 횟수로는 반복되지	않는
다. 또한 V번 반복될 때마다 각각 자신과	연결된 간선들을 모두 확인한다. 따라서 "현재 우선순위 큐에서 꺼낸 노드와 연결된 다른 노드들을 확인"하는	총횟수는 총 최대 간선의 개수(E)만큼 연산이 수행될 수 있다.

따라서	전체 다익스트라 최단 경로 알고리즘은 E개의 원소를 우선순위 큐에 넣었다가 모두 빼내는 연산과 매우 유사하다고 볼	수 있다.

힙에 N개의 데이터를	모두 넣고, 이후에 모두 빼는 과정은 $O(NlogN)$이다. 간단하게 생각하면 다익스트라 알고리즘의 시간복잡도는 최대 E개의 간선 데이터를 힙에 넣었다가 다시 빼는 것으로 볼 수 있으므로 $O(ElogE)$ 임을	이해할	수 있다.

이때 중복 간선을 포함하지 않는 경우, E는 항상 $V^2$보다	작다. 왜냐하면, 모든 노드끼리 서로 다 연결되어	있다고	했을 때 간선의 개수를 약 $V^2$으로 볼 수 있고 E는 항상 $V^2$ 이하이기 때문이다.

다시 말해 $logE$는 $logV^2$보다 작다. 이때	$O(logV^2)$은 $O(2logV)$이고, 이는 $O(logV)$이다.

따라서	다익스트라 알고리즘의	전체 시간복잡도를 간단히 $O(ElogV)$ 라고 볼 수 있다.