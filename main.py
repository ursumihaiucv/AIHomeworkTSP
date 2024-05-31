from DFS import dfs_tsp
from LeastCostSearch import leastcost_tsp
from ASTAR import a_star

# Input graph as adjacency matrix
graph = [[0, 3, 5, 10], [13, 0, 14, 9], [5, 3, 0, 13], [7, 4, 3, 0]]

# Input start city
start = int(input("Enter the starting city (0-indexed): "))

# Run chosen algorithm
algorithm = input("Enter the algorithm (DFS, LCUS, or A*): ").upper()
if algorithm == "DFS":
    best_path, min_cost = dfs_tsp(graph, start)
elif algorithm == "LCUS":
    best_path, min_cost = leastcost_tsp(graph, start)
elif algorithm == "A*":
    best_path, min_cost = a_star(graph,start)
else:
    print("Invalid algorithm choice. Please choose DFS, LCUS, or A*.")
    exit()

# Print results
print("Best Path:", best_path)
print("Minimum Cost:", min_cost)
