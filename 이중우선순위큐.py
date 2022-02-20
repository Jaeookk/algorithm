import heapq


def solution(operations):
    h = []
    for i in operations:
        if i[0] == 'I':
            heapq.heappush(h, int(i[2:]))
        elif not h:
            continue
        elif i[1:] == ' 1':
            h.pop(h.index(heapq.nlargest(1, h)[0]))
        elif i[1:] == ' -1':
            heapq.heappop(h)

    if h:
        return [heapq.nlargest(1, h)[0], heapq.heappop(h)]
    else:
        return [0, 0]
