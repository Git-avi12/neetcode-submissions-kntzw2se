class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = {i:[] for i in range(n)}
        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)
        visited = set()
        order = []

        def dfs(start,graph,visited):
            stack = [start]
            while stack:
                node = stack.pop()
                if node not in visited:
                    visited.add(node)
                    order.append(node)
                    stack.extend(reversed(graph[node]))
        count = 0
        for i in range(n):
            if i not in visited:
                count+=1
                dfs(i,graph,visited)
        return count
        
