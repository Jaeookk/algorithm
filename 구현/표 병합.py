# https://school.programmers.co.kr/learn/courses/30/lessons/150366#

def solution(commands): 
    def update(*args):
        if len(args) == 3:
            r,c = int(args[0]), int(args[1])
            old_state = state[r][c]
            for i in range(51):
                for j in range(51):
                    if state[i][j] == old_state:
                        graph[i][j] = args[2]
        else:
            for i in range(51):
                for j in range(51):
                    if graph[i][j] == args[0]:
                        graph[i][j] = args[1]
                            
    def merge(args):
        r1,c1,r2,c2 = map(int,args)
        change = None
        if graph[r1][c1] == 'EMPTY' and graph[r2][c2] != 'EMPTY':
            change = graph[r2][c2]
        elif graph[r1][c1] != 'EMPTY' and graph[r2][c2] == 'EMPTY':
            change = graph[r1][c1]
        elif graph[r1][c1] != 'EMPTY' and graph[r2][c2] != 'EMPTY':
            change = graph[r1][c1]

        old_state = state[r2][c2]
        for i in range(51):
            for j in range(51):
                if state[i][j] == old_state:
                    state[i][j] = state[r1][c1]
        if change:
            for i in range(51):
                for j in range(51):
                    if state[i][j] == state[r1][c1]:
                        graph[i][j] = change
        
    def unmerge(args):
        r,c = map(int,args)
        old_value = graph[r][c]
        old_state = state[r][c]
        for i in range(51):
            for j in range(51):
                if state[i][j] == old_state:
                    state[i][j] = (i,j)
                    graph[i][j] = "EMPTY"
        graph[r][c] = old_value
        
    def print_(args):
        r,c = map(int, args)
        answer.append(graph[r][c])
    
    answer = []
    graph = [["EMPTY"]*51 for _ in range(51)]
    state = [[(i,j) for j in range(51)] for i in range(51)]
    for command in commands:
        order, *re = command.split()  
        if order == "UPDATE":
            update(*re)
        elif order == "MERGE":
            merge(re)
        elif order == "UNMERGE":
            unmerge(re)
        else:
            print_(re)
    return answer
