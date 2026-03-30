class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        #1.We gotta prepare an adjacent list
        graph = {i:[] for i in range(n)}
        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)
        print(graph)
        visited=[]
        # lets now create a function to carry out the dfs algorithm
        def dfs_iter(start,graph,visited):
            stack = [start]
            while stack:
                node = stack.pop()
                if node not in visited:
                    visited.append(node)
                    for i in reversed(graph[node]):
                        stack.append(i)
        #lets now create the main loop that iteratively runs the dfs algo for every node of the graph 
        #we'll also have the main count variable whichll count the number of times the fn is called which says the number of connected comps are in the graph
        count=0
        for i in range(n):
            if i not in visited:
                count+=1
                dfs_iter(i,graph,visited)
        print(visited)
        return count