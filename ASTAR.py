import heapq


def a_star(graph, start):
    n = len(graph)
    pq = [(0, start, [start])]
    best_path = None
    min_cost = float('inf')

    while pq:
        estimated_cost, current, path = heapq.heappop(pq)
        unvisited = set(range(n)) - set(path)

        if len(path) == n:
            cost = sum(
                graph[path[i]][path[i + 1]]
                for i in range(n -
                               1)) + graph[path[-1]][start]  # back to start
            if cost < min_cost:
                min_cost = cost
                best_path = path + [start]
            continue

        for neighbor in unvisited:
            new_cost = graph[current][neighbor] + heuristic(
                graph, current, start, unvisited - {neighbor})
            heapq.heappush(pq, (new_cost, neighbor, path + [neighbor]))

    return best_path, min_cost


def heuristic(graph, current, start, unvisited):
    """Heuristic function for the A* TSP algorithm based on the minimum spanning tree."""
    if not unvisited:
        return 0  # If all cities have been visited, remaining cost is 0

    # Calculate the cost of the minimum spanning tree for the unvisited cities
    mst_cost = minimum_spanning_tree(graph, unvisited)

    # Calculate the remaining cost from the current node to each unvisited city, including the start city
    remaining_costs = [graph[current][city]
                       for city in unvisited] + [graph[current][start]]

    # Estimate the remaining cost as the minimum of these costs
    remaining_cost = min(remaining_costs)

    # Add the estimated remaining cost to the minimum spanning tree cost
    return mst_cost + remaining_cost


def minimum_spanning_tree(graph, unvisited):
    """Calculate the cost of the minimum spanning tree of the unvisited cities."""
    n = len(graph)
    visited = [False] * n
    min_cost = 0
    priority_queue = [(0, 0)]  # (cost, node)

    while priority_queue:
        cost, node = priority_queue.pop(0)

        if not visited[node]:
            min_cost += cost
            visited[node] = True

            for neighbor, weight in enumerate(graph[node]):
                if not visited[
                        neighbor] and weight > 0 and neighbor in unvisited:
                    priority_queue.append((weight, neighbor))

            priority_queue.sort()

    return min_cost
