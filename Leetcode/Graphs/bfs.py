from collections import deque


def bfs(graph, start_node):
    visited = set([start_node])
    q = deque([start_node])

    while q:
        visiting = q.popleft()
        print(f"visiting: {visiting}")

        for i in graph[visiting]:
            if i not in visited:
                visited.add(i)
                q.append(i)


my_graph = {
    "A": ["B", "C"],
    "B": ["A", "D", "E"],
    "C": ["A", "F"],
    "D": ["B"],
    "E": ["B", "F"],
    "F": ["C", "E"],
}

print("BFS Traversal starting from node 'A':")
bfs(my_graph, "A")
