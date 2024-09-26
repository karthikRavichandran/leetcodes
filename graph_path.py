

def find_the_path(graph, start, end):
    master_list =[]
    path_list = []
    loop_list = []
    def dfs(grap, st, end, path_list, master_list):
        path_list.append(st)
        for i in grap[st]: # for i in ['B']
            if i not in path_list:
                dfs(grap, i, end, path_list, master_list)
            else:
                path_list.append(i)
                id = path_list.index(i)
                loop_list.append(list(path_list[id:]))
                path_list.pop()

        path_list.pop()

    dfs(graph, start, end, path_list, master_list)
    return master_list, loop_list


def find_cycle(graph):
    def dfs(node, parent, visited, path):
        visited.add(node)
        path.append(node)

        for neighbor in graph[node]:
            if neighbor not in visited:
                if dfs(neighbor, node, visited, path):
                    master_set.append(list(path))
                    return True
            elif neighbor in path and neighbor != parent:
                return True

        path.pop()
        return False

    visited = set()
    path = []
    master_set = []

    for node in graph:
        if node not in visited:
            if dfs(node, None, visited, path):
                return True
    return False

graph = {
    'A': ['B'],
    'B': ['A', 'E', 'C', 'D'],
    'C': ['B','D','F'],
    'D': ['B','C'],
    'E': ['B','F'],
    'F': ['E','C']
}


# Finding all paths from A to E
start_node = 'A'
end_node = 'E'
all_paths, loop = find_the_path(graph, start_node, end_node)

print(f"All paths from {start_node} to {end_node}:")
for path in loop:
    print(" -> ".join(path))
