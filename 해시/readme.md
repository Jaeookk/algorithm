> [해시 자료구조 정복하기 - 바킹독](https://blog.encrypted.gg/1009)

<br/>

파이썬에서 **해시(Hash)** 는 어떻게 구현할 수 있을까?

파이썬에서는 **Dictionary** 라는 자료구조를 통해 해시를 제공한다. 그리고 Dictionary는 dict클래스에 구현되어있다.

<br/>

# 해시 언제 사용하면 좋을까?! 

1. **리스트를 쓸 수 없을 때**  

    리스트는 숫자 인덱스를 이용하여 원소에 접근한다.  
    즉, list[1]은 가능하지만 list['a']는 불가능하다.
    인덱스 값을 숫자가 아닌 다른 값 '문자열, 튜플'을 사용하려고 할 때 딕셔너리를 사용하면 좋다.

 

2. **빠른 접근  / 탐색이 필요할 때 (가장 중요)**

    아래에서 표를 보면 알 수 있듯이, 딕셔너리 함수의 시간복잡도는 대부분 **O(1)** 이므로 아주 빠른 자료구조 이다.

 

3. **집계가 필요할 때**

    원소의 개수를 세는 문제는 코딩 테스트에서 많이 출제되는 문제다.  
    이때 해시와, collections 모듈의 Counter 클래스를 사용하면 아주 빠르게 문제를 푸실 수 있다.

<br/>

# 딕셔너리와 리스트의 시간 복잡도 차이


|Operation|Dictionary|List|
|:---:|:---:|:---:|
|Get Item|O(1)|O(1)|
|Insert Item|O(1)|O(1) ~ O(N)|
|Update Item|O(1)|O(1)|
|Delete Item|O(1)|O(1) ~ O(N)|
|Search Item|O(1)|O(N)|

List에 비해 Dictionary가 매우 빠른 시간복잡도를 갖는 것을 볼 수 있다.

> 즉 , 원소를 넣거나 삭제, 찾는 일이 많을 때에는 딕셔너리를 사용하는 것이 좋다 


※ 파이썬 3.7 이상부터 딕셔너리는 **원소가 들어온 순서를 보장**. 반면, 3.7 미만은 순서를 보장하지 않는다.

<br/>

# Dictionary 사용법

## 📌 Init

`{}`를 사용하거나 `dict`함수 호출 시 빈 딕셔너리를 선언할 수 있다. 

`key - value 쌍`을 갖는 dictionary 선언도 바로 가능하다.

```python
# 빈딕셔너리 생성
dict1 = {} # {}
dict2 = dict() # {}
```

```python
# 특정 key-value쌍을 가진 dictionary 선언

Dog = {
    'name': '동동이',
    'weight': 4,
    'height': 100,
}


'''
{'height': 100, 'name': '동동이', 'weight': 4}
'''
```

```python
# dictionary를 value로 가지는 dictionary 선언

Animals = {
    'Dog': {
        'name': '동동이',
        'age': '5'
    },
    'Cat': {
        'name': '야옹이',
        'weight': 3
    }
}


'''
 { 'Dog': { 'name': '동동이', 'age': '5'},
   'Cat': {'name': '야옹이','weight': 3 }}
'''
 ```

## 📌 Get Item

Dictionary에서 원소를 가져오는 방법은 2가지 있다.

1. **`[]` 사용하기**

2. **`get` 메소드 이용하기**

    get 메소드는 `get(key,x)` 로 사용하실 수 있다.  
    이는 '딕셔너리에 key가 없는 경우, x를 리턴해줘라' 라는 용도다.

딕셔너리를 카운터하는 (집계) 경우에 get함수가 유용하게 사용된다.

```python
# [] 기호 사용해 원소 가져오기

dict = {'하이': 300, '헬로': 180, 3: 5}
dict['헬로'] # 180
```

```python
# get 메소드를 아용해 원소 가져오기 1
# 딕셔너리에 해당 key가 없을때 Key Error 를 내는 대신, 특정한 값을 가져온다.

dict = {'하이': 300, '헬로': 180}
dict.get('동동', 0) # 0
```

```python
# get 메소드를 아용해 원소 가져오기 2
# 물론, 딕셔너리에 해당 key가 있는 경우 대응하는 value를 가져온다.

dict = {'하이': 300, '헬로': 180}
dict.get('헬로', 0) # 180
 ```


## 📌 Insert / Update Item

딕셔너리에 값을 집어넣거나, 값을 업데이트 할 때 `[ ]` 를 사용.

```python
# 값 집어넣기

dict = {'김철수': 300, 'Anna': 180}
dict['홍길동'] = 100
dict #{'Anna': 180, '김철수': 300, '홍길동': 100}
```

```python
# 값 수정하기1

dict = {'김철수': 300, 'Anna': 180}
dict['김철수'] = 500
dict # {'Anna': 180, '김철수': 500}
```

```python
# 값 수정하기2

dict = {'김철수': 300, 'Anna': 180}
dict['김철수'] += 500
dict # {'Anna': 180, '김철수': 800}
 ```

## 📌 Delete Item

딕셔너리에서 특정 key값을 지울 때에 다음과 같은 방법을 사용할 수 있다.

1. **`del dict_obj[key]`**

    `del`은 키워드로써, 만약 딕셔너리에 key가 없다면 keyError가 발생.

2. **`pop(key[,default])`**

    `pop`은 메소드로써, key 값에 해당하는 value를 리턴.   
    key가 없다면 두번째 파라미터인 default를 리턴.  
    만약 default 설정하지 않았을 시엔 keyError가 발생. 

```python
# del 이용하기 - 키가 있는 경우
dict = {'김철수': 300, 'Anna': 180}
del dict['김철수']

dict #{'Anna': 180}
```

```python
# del 이용하기 - 키가 없는 경우 raise KeyError
my_dict = {'김철수': 300, 'Anna': 180}
del my_dict['홍길동'] 
'''
keyError 발생!
'''
```

```python
# pop 이용하기 - 키가 있는 경우 대응하는 value 리턴
my_dict = {'김철수': 300, 'Anna': 180}
my_dict.pop('김철수', 180) # 300
```

```python
# pop 이용하기 - 키가 없는 경우 대응하는 default 리턴
my_dict = {'김철수': 300, 'Anna': 180}
my_dict.pop('홍길동', 180) # 180
 ```

## 📌 Search Item

딕셔너리를 조회할 때 두가지 방법이 존재.

1. key로만 순회하기

2. key, value 동시 순회하기 (items() 사용)

```python
# key로만 순회
dict = {'김철수': 300, 'Anna': 180}
for key in dict:
    print(key)
    # 이 경우 value를 찾고 싶으면 dict[key] 와 같이 접근을 따로 해주어야.

'''
김철수
Anna
'''
```

```python
# key-value 동시 순회

dict = {'김철수': 300, 'Anna': 180}
for key, value in dict.items():
    print(key, value)

'''
김철수 300
Anna 180
'''
```
 

## 그 밖에 딕셔너리 유용한 팁
1. 특정 key가 딕셔너리에 있는지 없는지 조회할 때 -> `in` 사용하기
    ```python
    dict = {'김철수': 300, 'Anna': 180}
    print("김철수" in dict) #True
    print("김철수" not in dict) # False
    ```

2. key 또는 value만 뽑아내는 방법
    ```python
    # key만 뽑기 -> keys 사용


    my_dict = {'김철수': 300, 'Anna': 180}
    my_dict.keys() # dict_keys(['김철수', 'Anna'])
    ```

    ```python
    # value만 뽑기 -> values 사용


    my_dict = {'김철수': 300, 'Anna': 180}
    my_dict.values() # dict_values([300, 180])
    ```

3. key - value 모두 뽑기 : `items()`
    ```python
    # key, value 쌍을 extract - items 사용


    my_dict = {'김철수': 300, 'Anna': 180}
    my_dict.items() # dict_items([('김철수', 300), ('Anna', 180)])
    ```