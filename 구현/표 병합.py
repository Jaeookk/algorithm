def solution(commands):
    answer = []
    graph = [['EMPTY']*51 for _ in range(51)]
    state = [[]*51 for _ in range(51)]

    for command in commands:
        order, *re = command.split()
        
        if order == "UPDATE":
            if len(re) == 3:
                r,c = int(re[0]), int(re[1])
                old_state = state[r][c]
                for i in range(51):
                    for j in range(51):
                        if state[i] == old_state:
                            graph[i][j] = re[2]
            else:
                for i in range(51):
                    for j in range(51):
                        if re[0] == graph[i][j]:
                            graph[i][j] = re[1]
        
        elif order == "MERGE":
            r1,c1,r2,c2 = map(int,re)
            change = None
            if graph[r1][c1] == '' and graph[r2][c2] != '':
                change = graph[r2][c2]
            elif graph[r1][c1] != '' and graph[r2][c2] == '':
                change = graph[r1][c1]
            else:
                change = graph[r1][c1]
            olde_state = state[r2][c2]
            for i in range(51):
                for j in range(51):
                    if state[i][j] == old_state:
                        state[i][j] = state[r1][c1]
                        graph[i][j] = change
                    
        elif order == "UNMERGE":
            r,c = map(int,re)
            x = graph[r][c]
            for i in range(len(stack)):
                if (r,c) in stack[i]:
                    arr = list(stack[i])
                    for j in range(len(arr)):
                        r1,c1 = arr[j]
                        graph[r1][c1] = ''
            graph[r][c] = x

        else:
            r,c = map(int, re)
            if graph[r][c] == '':
                answer.append("EMPTY")
                continue
            answer.append(graph[r][c])

    return answer
