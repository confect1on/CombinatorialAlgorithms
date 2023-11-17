import Lab3

def alg_Kraskala_connectivity_graph(edges, n):
    edge: tuple

    tree = []
    adj = [[] for _ in range(n)]
    edges.sort(key=lambda edge: edge[0])
    for (_, v1, v2) in edges:
        if cycle(adj, (v1 - 1, v2 - 1), n):
            continue
        tree.append((v1, v2))
        adj[v1 - 1].append(v2 - 1)
        adj[v2 - 1].append(v1 - 1)
    return tree


def cycle(adj, inserted_edge, n):
    visited = [False for _ in range(n)]
    q = Lab3.Stack(inserted_edge[0])
    Lab3._search(adj, q, visited)
    return visited[inserted_edge[0]] and visited[inserted_edge[1]]


def test():
    rice_plant = [
        (5, 1, 2),
        (10, 2, 3),
        (3, 3, 1),
        (10, 1, 4),
        (1, 4, 5),
        (1, 5, 6),
        (1, 6, 4),
        (8, 6, 3),
        (10, 6, 7),
        (2, 5, 7),
        (10, 3, 7),
        (2, 3, 8),
        (2, 8, 7),
        (1, 7, 9),
        (3, 9, 8),
        (5, 2, 11),
        (7, 8, 11),
        (1, 8, 10),
        (1, 9, 10),
        (6, 10, 11)
    ]
    print(*alg_Kraskala_connectivity_graph(rice_plant, 11))


test()