## BFS (Breadth-First Search)

* BFS는 **너비 우선 탐색** 이라고도 부르며, 그래프에서 **가까운 노드부터 우선적으로 탐색하는 알고리즘** 이다.
* BFS는 **큐 자료구조** 를 이용하며, 구체적인 동작 과정은 다음과 같다.
  1. 탐색 시작 노드를 큐에 삽입하고 방문 처리를 한다.
  2. 큐에서 **노드를 꺼낸 뒤에** 해당 노드의 인접 노드 중에서 **방문하지 않은 노드를 모두 큐에 삽입** 하고 방문 처리한다.
  3. 더 이상 2번의 과정을 수행할 수 없을때 까지 반복한다.

* **[Step 0]** 그래프를 준비한다. ( **방문 기준** : 번호가 낮은 인접 노드부터, 방문 기준은 문제에 따라 다를 수 있음 )
  * 시작 노드: 1  
  ![image](https://user-images.githubusercontent.com/78528903/180001196-3f602dca-e9e7-4724-89a3-6bba25acd282.png)

* **[Step 1]** 시작 노드인 '1'을 큐에 삽입하고 방문 처리를 한다.  
![image](https://user-images.githubusercontent.com/78528903/180001257-59b7df4c-b008-49ff-89f8-b4b62ed51017.png)

* **[Step 2]** 큐에서 노드 '1'을 꺼내고 방문하지 않은 인접 노드 '2', '3', '8'을 모두 큐에 삽입하고 방문 처리를 한다.  
![image](https://user-images.githubusercontent.com/78528903/180001303-de8becac-54fc-4d35-9e9b-0d6b339c4d95.png)

* **[Step 3]** 큐에서 노드 '2'를 꺼내고 방문하지 않은 인접 노드 '7'을 큐에 삽입하고 방문 처리를 한다.  
![image](https://user-images.githubusercontent.com/78528903/180001319-b2fd3da2-a1f8-4007-9d73-e180f859ecbb.png)

* **[Step 4]** 큐에서 노드 '3'을 꺼내고 방문하지 않은 인접 노드 '4'와 '5'를 모두 큐에 삽입하고 방문처리를 한다.  
![image](https://user-images.githubusercontent.com/78528903/180001336-f1a9fba7-42a1-41aa-998c-81a383faf7ef.png)

* **[Step 5]** 큐에서 노드 '8'을 꺼내고 방문하지 않은 인접 노드가 없으므로 무시한다.  
![image](https://user-images.githubusercontent.com/78528903/180001351-cabd1418-322b-4a52-9848-e03b93e02671.png)

* **[Step 6]** 큐에서 노드 '7'을 꺼내고 방문하지 않은 인접 노드 '6'을 큐에 삽입하고 방문 처리를 한다.  
![image](https://user-images.githubusercontent.com/78528903/180001375-2e743af2-b081-4253-b1cc-0b136d8471ec.png)

* **[Step 7]** 남아 있는 노드에 방문하지 않은 인접 노드가 없다. 따라서 모든 노드를 차례대로 꺼내면 최종적으로 다음과 같다.  
![image](https://user-images.githubusercontent.com/78528903/180001908-5901104d-c8a2-4dc7-98f4-2c11309d4fca.png)
  * 모든 간선의 비용이 1이라고 가정할때, 탐색 순서를 보면 시작 노드인 '1'에서 부터 거리가 1인 2와 3, 거리가 2인 4, 5, 7, 마지막으로 거리가 가장 먼 6이 순서대로 탐색되는 것을 확인할 수 있다.
  * BFS는 이러한 특징 때문에 각 간선의 비용이 모두 동일한 상황에서 **최단 거리 문제** 를 해결하기 위한 목적으로 사용할 수도 있다.

```python
from collections import deque

# BFS 메서드 정의
def bfs(graph, start, visited):
    # 큐(Queue) 구현을 위해 deque 라이브러리 사용
    queue = deque([start])
    # 현재 노드를 방문 처리
    visited[start] = True
    # 큐가 빌 때까지 반복
    while queue:
      # 큐에서 하나의 원소를 뽑아 출력하기
      v = queue.popleft()
      print(v, end=' ')
      # 아직 방문하지 않은 인접한 원소들을 큐에 삽입
      for i in graph[v]:
          if not visited[i]:
    	      queue.append(i)
            visited[i] = True

# 각 노드가 연결된 정보를 표현 (2차원 리스트)
graph = [
    [], # 일반적으로 그래프 문제가 출제되면 노드의 번호가 1번부터 시작하는 경우가 많기 때문에 index 0에 대한 내용은 비워두자
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]

# 각 노드가 방문된 정보를 표현 (1차원 리스트)
visited = [False] * 9

# 정의된 DFS 함수 호출
bfs(graph, 1, visited)

>>>
1 2 3 8 7 4 5 6
```
