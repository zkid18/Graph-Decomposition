#Uses python3

import sys

sys.setrecursionlimit(200000)

def fillOrder(adj, node, visited, stack):
    if node not in visited:
        visited.add(node)

    for v in adj[node]:
        if v not in visited:
            fillOrder(adj, v, visited, stack)
    stack = stack.append(node)

def dsfUntil(adj, node, visited):
    if node not in visited:
        visited.add(node)

    for i in adj[node]:
        if node not in visited:
            dsfUntil(adj, node, visited)

def getTransponce(adj):
    for i in adj:
        for j in adj[i]:
            adj

def number_of_strongly_connected_components(adj):
    result = 0
    visited = set()
    stack = []

    for node in range(len(adj)):
        if node not in visited:
            fillOrder(adj, node, visited, stack)

    visited = set()

    while stack:
        i = stack.pop()
        if i not in visited:
            dsfUntil(adj, i, visited)
            print(stack)

    #write your code here
    return result

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
    print(number_of_strongly_connected_components(adj))
