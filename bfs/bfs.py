#Uses python3

import sys
import queue

def distance(adj, s, t):

    n = len(adj)
    queue = []
    visited = set()
    path = []

    queue.append([s])

    dist = 0

    while (len(queue) > 0):
        path = queue.pop(0)

        last_vertex = path[-1]

        if last_vertex == t:
            # print(path)
            dist = len(path)-1

        elif last_vertex not in visited:
            for w in adj[last_vertex]:
                new_path = list(path)
                new_path.append((w))
                queue.append(new_path)
            visited.add(last_vertex)

    if dist != 0:
        return dist
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
