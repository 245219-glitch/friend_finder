maze = {
    "Entrance": ["Hall1", "Hall2"],
    "Hall1": ["Room1"],
    "Hall2": ["Room2", "Trap"],
    "Room1": [],
    "Room2": ["Exit"],
    "Trap": [],
    "Exit": [],
    "Vault": [],
}

def dfs_search(maze, room, exit_room, visited):
    visited.append(room)

    if room == exit_room:
        return True

    for next_room in maze[room]:
        if next_room not in visited:
            if dfs_search(maze, next_room, exit_room, visited):
                return True
    return False

def dfs_can_reach(maze, start, exit_room):
    visited = []
    found = dfs_search(maze, start, exit_room, visited)
    print("Visit order:", visited)
    print("Can reach", exit_room, "from", start + "?", found)
    return found

dfs_can_reach(maze, "Entrance", "Exit")