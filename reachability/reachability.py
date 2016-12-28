#Uses python3

import sys

def reach(adj, x):

    #count = 1

    stack = []
    stack.append(x)
    n = len(adj)
    visited = []
    for i in range (0,n):
        visited.append(False)

    while(len(stack)>0):
        #print(stack)
        v = stack.pop()
        if(not visited[v]):
            visited[v] = True
            print(v, " ", end ='')


            stack_aux = []
            for w in adj[v]:
                stack_aux.append(w)
            while(len(stack_aux)>0):
                stack.append(stack_aux.pop())

            #count = count+1
            # print(count)

    print("***")
    # if not(visited[y]):
    #     print(0)
    # else:
    #     print(1)


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    #print(n)
    #print(m)
    data = data[2:]
    #print(data)
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    #print(edges)
    x, y = data[2 * m:]
    # print(x,y)
    adj = [[] for _ in range(n)]

    x, y = x - 1, y - 1
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
        adj[b - 1].append(a - 1)

    #print(adj, len(adj))
    #print(adj[x], adj[y])
    for i in range(0, 4):
        reach(adj,i)