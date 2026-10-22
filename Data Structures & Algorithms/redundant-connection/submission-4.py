class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        # len(nodes) = len(edges) + 1 in a sparse graph
        # we have one more edge than we need to sparsely connect all nodes
        # thus len(nodes) = len(edges)
        n = len(edges)
        # index 0 is unused
        union = [i for i in range(0, n + 1)]

        def find_head(node):
            while union[node] != node:
                node = union[node]
                # path compression
            return node
        
        def merge(node1, node2):
            head1 = find_head(node1)
            head2 = find_head(node2)
            if head1 != head2:
                union[head1] = head2
                return True
            else:
                return False

        for u, v in edges:
            merged = merge(u,v)
            if not merged:
                return [u,v]

            