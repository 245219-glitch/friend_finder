network = {
    "Ali": ["Bilal", "Sara"],
    "Bilal": ["Ali", "Zara"],
    "Sara": ["Ali", "Omar"],
    "Zara": ["Bilal", "Hira"],
    "Omar": ["Sara"],
    "Hira": ["Zara"],
}

def bfs_shortest_path(graph, start, goal):
    visited = [start]
    queue = [[start]]          # queue stores the whole path, not just the node

    while queue:
        path = queue.pop(0)
        node = path[-1]

        if node == goal:
            print("Shortest chain from", start, "to", goal + ":", path)
            print("Number of introductions needed:", len(path) - 1)
            return path

        for neighbour in graph[node]:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(path + [neighbour])

    print("No connection found")
    return None

bfs_shortest_path(network, "Ali", "Hira")