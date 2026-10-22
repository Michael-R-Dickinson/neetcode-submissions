'''
we want to detect cycles!
if we find a cycle, any edge in the cycle can be removed to make it no longer a cycle

find the cycle:
- dfs from one node until we run into an already visited node
- we need to figure out which edges are part of the cycle

we want: traversal order
- order[find_idx(cylce starting node):last edge before its reached again]

n vertices
m edges
time: O(m + n)
memory: O(m)

accumulate in the stack:
- node_path: [1, 2, 4]

when we walk a path, remove the opposite direction of edges we traversed over

when we reach an already visited node, find it in the node_path, then all edges from that node onwards are part of a cycle
- check which is the last in the edges list
'''

from collections import defaultdict

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        def dfs(node):
            if node in visited:
                idx = node_path.index(node)
                # return all the candidate edges - the edges we could remove to get a non cyclical graph
                res = {tuple(sorted([node_path[i], node_path[i+1]])) for i in range(idx, len(node_path)-1)} 
                res.add(tuple(sorted((node_path[-1], node))))
                return res

            visited.add(node)
            node_path.append(node)
            adjacents = list(adjacency[node])
            for neighbor in adjacents:
                adjacency[neighbor].remove(node)
                out = dfs(neighbor)
                if out is not None:
                    return out
            
            visited.remove(node)
            node_path.pop()

        
        adjacency = defaultdict(set)
        for u, v in edges:
            adjacency[u].add(v)
            adjacency[v].add(u)

        visited = set()
        node_path = [] 
        cycle_candidates = dfs(1)
        for edge in reversed(edges):
            if tuple(edge) in cycle_candidates:
                return edge




        



