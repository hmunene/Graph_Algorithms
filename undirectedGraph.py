#Question One 

def dfs(graph, start):
    visited, stack = set(), [start]
    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.add(vertex)
            stack.extend(graph[vertex] - visited)
    return visited

def bfs(graph, start):
    visited, queue = set(), [start]
    p =[]
    while queue:
        vertex = queue.pop(0)
        if vertex not in visited:
            visited.add(vertex)
            p.append(vertex)
            queue.extend(graph[vertex] - visited)
    return p

def bfs_path(graph, start, goal):
    if start == goal:
        return [start]
    visited = {start}
    queue = [(start, [])]

    while queue:
        current, path = queue.pop(0) 
        visited.add(current)
        for neighbor in graph[current]:
            if neighbor == goal:
                return path + [current, neighbor]
            if neighbor in visited:
                continue
            queue.append((neighbor, path + [current]))
            visited.add(neighbor)   
    return None 

def dfs_path(graph, start, goal):
    stack = [(start, [start])]
    visited = set()
    while stack:
        (vertex, path) = stack.pop()
        if vertex not in visited:
            if vertex == goal:
                return path
            visited.add(vertex)
            for neighbor in graph[vertex]:
                stack.append((neighbor, path + [neighbor]))



def main():
    graph = {'A': set(['B', 'E', 'F']),
        'B': set(['A', 'C', 'F']),
        'C': set(['B', 'D','G']),
        'D': set(['G', 'G']),
        'E': set(['A', 'F', 'I']),
        'F': set(['A', 'B', 'E','I']),
        'G': set(['C', 'D', 'J']),
        'H': set(['K', 'L']),
        'I': set(['E', 'F', 'J']),
        'J': set(['I', 'G']),
        'K': set(['H', 'L', 'O']),
        'L': set(['H', 'K', 'P']),
        'M': set(['I', 'N']),
        'N': set(['M']),
        'O': set(['K']),
        'P': set(['L'])
        }
    
    p = dfs_path(graph, 'A', 'B')
    b = bfs_path(graph, 'A', 'B')
    v = dfs(graph, 'A')
    x = bfs(graph, 'A')
    print("The", len(v), "Connected Components with DFS: ", v)
    print("The", len(x), "Connected Components with BFS: ", x)
    print("DFS Path", p, "and BFS Path", b, "are not the same.")


if __name__ == '__main__':
    main()