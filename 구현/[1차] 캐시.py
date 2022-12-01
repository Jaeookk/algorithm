# https://school.programmers.co.kr/learn/courses/30/lessons/17680
# LRU(Least Recently Used)는 가장 오랫동안 참조되지 않은 페이지를 교체하는 방식
def solution(cacheSize, cities):
    answer = 0
    q = []
    if cacheSize == 0:
        return 5*len(cities)
    
    for city in cities:
        city = city.lower()
        if city in q:
            q.remove(city)
            q.append(city)
            answer += 1
        else:
            if len(q) >= cacheSize:
                q.pop(0)
                q.append(city)
            else:
                q.append(city)
            answer += 5
            
    return answer
