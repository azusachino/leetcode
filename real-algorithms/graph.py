from collections import defaultdict


def dfs(graph, node, parent, visited, time, low, bridges, articulation_points):
    visited.add(node)
    time[node] = len(time)  # Assign a unique time for the current node
    low[node] = time[node]
    num_children = 0

    for neighbor in graph[node]:
        if neighbor not in visited:
            num_children += 1
            dfs(graph, neighbor, node, visited, time, low, bridges, articulation_points)
            low[node] = min(low[node], low[neighbor])

            if parent != -1 and low[neighbor] >= time[node]:
                articulation_points.add(node)

            if low[neighbor] > time[node]:
                bridges.add((node, neighbor))

        elif neighbor != parent:
            low[node] = min(low[node], time[neighbor])

    if parent == -1 and num_children > 1:
        articulation_points.add(node)


def find_bridges_and_articulation_points(graph):
    visited = set()
    time = {}
    low = {}
    bridges = set()
    articulation_points = set()

    for node in graph:
        if node not in visited:
            dfs(graph, node, -1, visited, time, low, bridges, articulation_points)

    return bridges, articulation_points


# Example usage
graph = {
    0: [1, 2],
    1: [0, 2],
    2: [0, 1, 3, 5],
    3: [2, 4],
    4: [3],
    5: [2, 6, 7],
    6: [5, 7],
    7: [5, 6],
}

bridges, articulation_points = find_bridges_and_articulation_points(graph)
print("Bridges:", bridges)
print("Articulation Points:", articulation_points)
