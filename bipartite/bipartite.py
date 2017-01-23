#Uses python3

import sys
import queue

def bipartite(adj):

    n = len(adj)
    colorArr = [-1]*n
    visited = set()

    colorArr[0] = 1
    queue = set()
    queue.add(0)
    visited.add(0)

    while queue:
        u = queue.pop()
        for v in adj[u]:
            if (v not in visited) & (colorArr[v] == -1) :
                colorArr[v] = 1 - colorArr[u]
                queue.add(v)
                visited.add(v)

            elif (v in visited) & (colorArr[v] == colorArr[u]):
                visited.add(v)
                return 0

    return 1


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

    print(bipartite(adj))
