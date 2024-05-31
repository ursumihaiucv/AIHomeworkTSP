from collections import deque


def leastcost_tsp(graph, start):
    n = len(graph)
    queue = deque([(start, [start], 0)])
    best_path = None
    min_cost = float('inf')

    while queue:
        current, path, cost = queue.popleft()

        if len(path) == n:
            cost += graph[current][start]  # back to start
            if cost < min_cost:
                min_cost = cost
                best_path = path + [start]
            continue

        for neighbor in range(n):
            if neighbor not in path:
                new_cost = cost + graph[current][neighbor]
                queue.append((neighbor, path + [neighbor], new_cost))

    return best_path, min_cost
