from collections import defaultdict
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        """
        DFS for each node
        - enque positions
        - add traversed nodes to a set

        keep a count of unique
        """
        if len(edges) == 0:
            return n

        def dfs_connected(node):
            # add nearby nodes
            # don't add already seen
            seen.add(node)
            adjacent = adjacency[node]
            for target in adjacent:
                if target in seen:
                    continue
                dfs_connected(target)

        adjacency = defaultdict(set)
        for root, target in edges:
            adjacency[root].add(target)
            adjacency[target].add(root)

        extra_components = n - len(adjacency)
        print(extra_components, adjacency)

        # seen nodes
        seen = set()
        components = extra_components
        for node in list(adjacency.keys()):
            # skip already seen
            if node in seen:
                continue
            
            # dfs
            dfs_connected(node)
            components += 1

        return components

            

        