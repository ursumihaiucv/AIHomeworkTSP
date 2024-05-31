def dfs_tsp(graph, start):
    n = len(graph)
    stack = [(start, [start])]
    best_path = None
    min_cost = float('inf')

    while stack:
        current, path = stack.pop()

        if len(path) == n:
            cost = sum(
                graph[path[i]][path[i + 1]]
                for i in range(n -
                               1)) + graph[path[-1]][start]  # back to start
            if cost < min_cost:
                min_cost = cost
                best_path = path + [start]
            continue

        for neighbor in range(n):
            if neighbor not in path:
                stack.append((neighbor, path + [neighbor]))

    return best_path, min_cost
