#Uses python3

import sys


def reach(adj, node, visited):

    stack = []
    stack.append(node)
    n = len(adj)


    while(len(stack)>0):
        v = stack.pop()
        if(not visited[v]):
            visited[v] = True
            #print(v, " ", end ='')


            stack_aux = []
            for w in adj[v]:
                stack_aux.append(w)
            while(len(stack_aux)>0):
                stack.append(stack_aux.pop())



def number_of_components(adj):

    n = len(adj)
    visited = []

    for i in range (0,n):
        visited.append(False)

    result = 0

    for node in range(n):
        if not visited[node]:
            reach(adj,node, visited)
            result += 1
    print(result)




if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
        adj[b - 1].append(a - 1)
    # print(adj)
    number_of_components(adj)
