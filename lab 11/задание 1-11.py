from collections import deque

# 1. Создание структуры графа (список смежности)
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D'],
    'C': ['A', 'E'],
    'D': ['B'],
    'E': ['C']
}

# Добавление новых связей и узла 'F'
graph['F'] = ['A', 'D']
graph['A'].append('F')
graph['D'].append('F')

def get_neighbors(graph, node):
    """Возвращает список соседей узла."""
    return graph.get(node, [])

def dfs_stack(graph, start):
    """Обход в глубину (DFS) с использованием стека."""
    visited = set()
    stack = [start]
    result = []

    while stack:
        node = stack.pop()
        if node not in visited:
            result.append(node)
            visited.add(node)
            # reversed используется, чтобы обходить узлы в алфавитном порядке
            for neighbor in reversed(graph.get(node, [])):
                stack.append(neighbor)
    return result

def bfs(graph, start):
    """Обход в ширину (BFS) с использованием очереди."""
    visited = set()
    queue = deque([start])
    result = []

    while queue:
        node = queue.popleft()
        if node not in visited:
            result.append(node)
            visited.add(node)
            for neighbor in graph.get(node, []):
                queue.append(neighbor)
    return result

# --- Тестирование ---

print(f"Соседи узла A: {get_neighbors(graph, 'A')}")

print("DFS (в глубину):", "".join(dfs_stack(graph, 'A')))
# Ожидаемый вывод: ABDFCE (зависит от порядка в списке)

print("BFS (в ширину):", " ".join(bfs(graph, 'A')))
# Ожидаемый вывод: A B C F D E