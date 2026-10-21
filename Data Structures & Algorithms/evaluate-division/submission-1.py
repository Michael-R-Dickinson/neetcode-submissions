'''
Input: equations = [["a","b"],["b","c"],["ab","bc"]], values = [4.0,1.0,3.25], queries = [["a","c"],["b","a"],["c","c"],["ab","a"],["d","d"]]

a/b -> b/a
aim to get both variables in a single expression

a/b * b/c = a/c

Output: [4.00000,0.25000,1.00000,-1.00000,-1.00000]

if a/b is the edge a->b the ratio a:b then the edge a:c is the ratio a:c which we can find by multiplying weights as we traverse

a 4-> b 1 -> c

a->b is a directed weight 4
so traversing the opposite direction is weight (1/4)

how do we handle this?

adjacency graph should include PAIRS (adjacent node, weight) where weight is different from a->b and b->a

BFS from the start node to the end node multiplying weights as we go


we want:
numerator/denominator
the edge numerator -> denominator should encode this


'''

from collections import defaultdict, deque

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        adjacency = defaultdict(list)
        for i in range(len(equations)):
            numerator, denominator = equations[i]
            value = values[i]
            # represents the ratio numerator/denominator
            adjacency[numerator].append((denominator, value))
            adjacency[denominator].append((numerator, 1 / value))
        
        def compute_ratio(numerator, denominator):
            if numerator not in adjacency.keys() or denominator not in adjacency.keys():
                return -1
            queue = deque()
            queue.append((numerator, 1))
            visited = set()
            # search for denominator
            success = False
            while queue:
                node, accumulated_weight = queue.popleft()
                if node == denominator:
                    return accumulated_weight
                    continue
                if node in visited:
                    continue

                visited.add(node)
                
                for neighbor, edge_weight in adjacency[node]:
                    queue.append((neighbor, accumulated_weight * edge_weight))
            if not success:
                return -1
                
        out = []
        for numerator, denominator in queries:
            out.append(compute_ratio(numerator, denominator))
        return out
                
                



        