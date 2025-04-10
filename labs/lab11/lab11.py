import collections

def dfs(graph, start):
    visited = set()
    result = []

    def recursion(node):
        visited.add(node)
        result.append(node)
        for x in graph[node]:
            if x not in visited:
                recursion(x)
    recursion(start)
    return result


def bfs(graph, root):
    visited = set()
    queue = collections.deque([root])
    result = []

    visited.add(root)
    while queue:
        node = queue.popleft()
        result.append(node)
        for x in graph[node]:
            if x not in visited:
                visited.add(x)
                queue.append(x)
    return result