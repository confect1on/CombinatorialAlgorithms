import collections

class Queue():
    def __init__(self, *elements):
        self._elements = collections.deque(elements)

    def __len__(self):
        return len(self._elements)

    def __iter__(self):
        while len(self) > 0:
            yield self.dequeue()

    def enqueue(self, element):
        self._elements.append(element)

    def dequeue(self):
        return self._elements.popleft()


class Stack(Queue):
    def dequeue(self):
        return self._elements.pop()


def dfs(adjacency_list):
    q = Stack(0)
    claims = [0 for _ in range(len(adjacency_list))]
    claims[0] = 1
    return _search(adjacency_list, q, claims)


def bfs(adjacency_list):
    q = Queue(0)
    claims = [0 for _ in range(len(adjacency_list))]
    claims[0] = 1
    return _search(adjacency_list, q, claims)


def _search(adjacency_list, vertex_container, claims):
    res = []
    if not isinstance(vertex_container, Queue):
        raise TypeError
    while len(vertex_container) > 0:
        vertex = vertex_container.dequeue()
        res.append(vertex)
        for incident_vertex in adjacency_list[vertex]:
            if not claims[incident_vertex]:
                claims[incident_vertex] = 1
                vertex_container.enqueue(incident_vertex)
    return res

def search_connectivity_components(adjacency_list):
    res = []
    claims = [0 for _ in range(len(adjacency_list))]
    q = Stack()
    for vertex, is_visited in enumerate(claims):
        if not is_visited:
            claims[vertex] = 1
            q.enqueue(vertex)
            res.append(_search(adjacency_list, q, claims))
    return res

def search_accessible_vertexes(adjacency_list, vertex):
    claims = [0 for _ in range(len(adjacency_list))]
    q = Stack(vertex)
    claims[vertex] = 1
    return _search(adjacency_list, q, claims)

def test():
    dfs_adj = [
        (7, 6, 1),
        (5, 2),
        (4, 3),
        (2,),
        (2,),
        (1,),
        (0,),
        (11, 0, 8),
        (10, 9, 7),
        [8],
        (8,),
        (7,)
    ]
    bfs_adj = [
        (1, 2, 3),
        (0, 4),
        (0, 5, 6),
        (0, 7),
        (1, 8),
        (2, 9),
        (2,),
        (3,),
        (4,),
        (5,)

    ]
    comp_adj = [
        (),
        (4, 3, 2),
        (4, 3, 1),
        (4, 2, 1),
        (3, 2, 1),
        (6,),
        (5,),
        (8,),
        (7,)
    ]

    access_adj = [
        (4, 1),
        (2,),
        (3, 1),
        (),
        (1,)
    ]
    print("dfs", *dfs(dfs_adj))
    print("bfs", *bfs(bfs_adj))
    print("connective components", *search_connectivity_components(comp_adj))
    print("accessible vertex ", *search_accessible_vertexes(access_adj, 1))


