#Uses python3

import sys


def dfs_visit(adj, u, color, found_cycle):

    if found_cycle[0]:
        return
    color[u] = "gray"

    for w in adj[u]:
        if color[w] == "gray":
            found_cycle[0] = True
            return
        if color[w] == "white":
            dfs_visit(adj, w, color, found_cycle)
    color[u] = "black"



def acyclic(adj):

    n = len(adj)
    found_cycle = [False]
    color = { u: "white" for u in range(n) }

    for u in range(n):
        # print(color[u])
        if color[u] == "white":
            dfs_visit(adj, u, color, found_cycle)
        if found_cycle[0]:
            break
    if found_cycle[0]:
        return 1
    elif not found_cycle[0]:
        return 0





if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)

    # print(edges)
    print(acyclic(adj))
