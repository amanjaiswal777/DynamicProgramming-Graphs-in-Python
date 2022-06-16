import itertools

def bellmanFordAlgorithm():
    graph = {
            's' : {'t' : 6, 'y' : 7},
            't' : {'x' : 5, 'y' : 8, 'z' : -4},
            'y' : {'t' : -2},
            'x' : {'t' : -3},
            'z' : {'s' : 2, 'x' : 7}
            }

    dist = {
        't': float("inf"),
        'y': float("inf"),
        'x': float("inf"),
        'z': float("inf"),
        's': 0
    }

    for _, (u, value) in itertools.product(range(len(graph)-1), graph.items()):
        for v in value:
            if dist[v] > dist[u] + graph[u][v]:
                dist[v] = dist[u] + graph[u][v]
    has_negative_cycle = False
    for u, value_ in graph.items():
        for v in value_:
            if dist[v] > dist[u] + graph[u][v]:
                has_negative_cycle = True
    return "Has Negative Cycle" if has_negative_cycle else dist

if __name__ == '__main__':
    print(bellmanFordAlgorithm())