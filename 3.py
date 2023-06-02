def bfs(graph, start, goal):
    queue = [start]
    visited = set()
    while queue:
        current = queue.pop(0)
        if current == goal:
            return True
        visited.add(current)
        for neighbor in graph[current]:
            if neighbor not in visited:
                queue.append(neighbor)
    return False
