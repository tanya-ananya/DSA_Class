def course_schedule(n, prerequisites):
    adj_matrix = [[0 for _ in range(n)] for _ in range(n)]
    indeg = [0] * n

    for x, y in prerequisites:
        if adj_matrix[y][x] == 0:
            adj_matrix[y][x] = 1
            indeg[x] += 1

    result_list = []
    queue = []

    for y in range(n):
        if indeg[y] == 0:
            queue.append(y)

    while queue:
        current = queue.pop(0)
        result_list.append(current)

        for y in range(n):
            if adj_matrix[current][y] == 1:
                adj_matrix[current][y] = 0 
                indeg[y] -= 1
                if indeg[y] == 0:
                    queue.append(y)

    if len(result_list) == n:
        return result_list
    else:
        return []