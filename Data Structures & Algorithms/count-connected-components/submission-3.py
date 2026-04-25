class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        if not n:
            return 0
        adj = {i:[] for i in range(n)}
        for n1,n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)
        
        visit = set()
        islands = 0

        def dfs(i,prev):
            if i in visit:
                return
            visit.add(i)
            for nei in adj[i]:
                if nei == prev:
                    continue
                dfs(nei,i)

        for i in range(n):
            if i not in visit:
                dfs(i,-1)
                islands +=1
        return islands