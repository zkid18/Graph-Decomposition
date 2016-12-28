#Uses python3

import sys

def toposort(adj):
    visited = set()
    order = []

    for node in range(len(adj)):
        if node not in visited:
            dfs(adj, visited, order, node)

    order.reverse()
    return order


def dfs(adj, visited, order, x):
    if x not in visited:
        visited.add(x)
        for v in adj[x]:
            dfs(adj, visited, order, v)
        order.append(x)
    pass


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
    order = toposort(adj)
    for x in order:
        print(x + 1, end=' ')

