from collections import deque

#Graph
graph = {
    "A": ["B"],
    "B": ["C", "D"],
    "C": ["E"],
    "D": ["F"],
    "E": [],
    "F": []
}


#BFS
def bfs_graph(graph, start, goal):
    queue = deque([start])

    visited = {start}
    parent = {start: None}
    explored = []

    while queue:
        current = queue.popleft()

        explored.append(current)

        if current == goal:
            break

        for neighbor in graph[current]:
            if neighbor not in visited:
                visited.add(neighbor)

                parent[neighbor] = current

                queue.append(neighbor)

    if goal not in parent:
        return None, explored

    path = []

    current = goal

    while current is not None:
        path.append(current)
        current = parent[current]

    path.reverse()

    return path, explored

#DFS
def dfs_graph(graph, start, goal):
    visited = set()
    explored = []
    parent = {start: None}

    def dfs(current):

        visited.add(current)
        explored.append(current)


        if current == goal:
            return True

        for neighbor in graph[current]:

            if neighbor not in visited:

                parent[neighbor] = current

                if dfs(neighbor):
                    return True

        return False

    found = dfs(start)

    if not found:
        return None, explored

    path = []

    current = goal

    while current is not None:
        path.append(current)
        current = parent[current]

    path.reverse()

    return path, explored


#BFS and DFS test
bfs_path, bfs_explored = bfs_graph(graph, "A", "E")

dfs_path, dfs_explored = dfs_graph(graph, "A", "E")


print("GRAPH SEARCH")
print("------------------------")

print("BFS path:")
print(" -> ".join(bfs_path))

print("BFS explored:")
print(bfs_explored)


print()

print("DFS path:")
print(" -> ".join(dfs_path))

print("DFS explored:")
print(dfs_explored)