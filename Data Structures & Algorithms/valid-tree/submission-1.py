'''
detect any cycles

create adjacnecy list:

dfs method:
Start a dfs from ONE node
- track: visited-overall
- each time we go to visit a new node - remove the edge that we used to get there from the adjacency set
- if we end up on a node in visited-overall: return false

Note: the visited-within-dfs check should come before the visited-overall check

At the end before returning, check if we've actually visited all nodes - maybe theres separate connected components -> false
-> check len(visited) == n

'''


class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        def dfs(node):
            if node in visited:
                return False

            visited.add(node)
            for adjacent in adjacency[node]:
                adjacency[adjacent].remove(node)
                if not dfs(adjacent):
                    return False

            return True

        adjacency = [set() for i in range(n)]
        for src, target in edges: 
            adjacency[src].add(target)
            adjacency[target].add(src)
        
        visited = set()
        out = dfs(0)
        return out and len(visited) == n
        
