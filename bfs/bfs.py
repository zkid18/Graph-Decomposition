#Uses python3

import sys
import queue

def distance(adj, s, t):

    n = len(adj)
    queue = []
    queue.append([s])
    visited = []

    while queue:
        path = queue.pop(0)
        node = path[-1]

        # print(path)
        # print(node)

        for v in adj[node]:
            new_path = list(path)
            new_path.append(v)
            queue.append(new_path)

        if node == t:
            return path
        else:
            return -1



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
    s, t = data[2 * m] - 1, data[2 * m + 1] - 1

    print(distance(adj, s, t))
