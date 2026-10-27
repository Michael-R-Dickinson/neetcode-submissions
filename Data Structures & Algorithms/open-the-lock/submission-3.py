'''
Idea 1:
Each 4 digit combo represents a single graph node
Each node is connected to all the states it can become with just one turn:

0123 connects to:
- 1123
- 9123
- 0223
- 0023
...

Outgoing edges per node = 8 = 2(digits)

Full graph would have:
9999 * 15 nodes

8 * n = edges

Remove all edges for deadends

Then its a simple bfs towards the target

Idea 2:
4 different graphs - we represent the same 9999*15 node state with only 4 states

We compute adjacency on the fly and then drop any adjacents that are dead ends.

each graph is a loop - 0->9->0

We BFS from all graphs starting at 0:
- what nodes are adjacent: change any digit by 1
- drop deadends from the adjacency list
- avoid revisting the same combination twice
Represents the same internal info using no explicit graph in memory

Pseudocode:
queue = [(0,0,0,0)]
visited = set()

while queue:
    ignore deadends
    ignore already visited

    create list of adjacent combos
    add them to queue

    NOTE: keep a counter of how many iterations of BFS we've done
    if we reach target - return iterations
'''


from collections import deque

class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        def string_to_tuple(s: str):
            return tuple(int(d) for d in s)

        target_combo = string_to_tuple(target)
        deadends_set = set(string_to_tuple(deadend) for deadend in deadends)

        if ((0,0,0,0) in deadends_set):
            return -1

        queue = deque()
        queue.append((0,0,0,0))

        visited = set()

        # the number of turns required to reach any of the combos currently in the queue
        iterations = 0

        adjacent_directions = [
            (-1,0,0,0),(1,0,0,0),(0,-1,0,0),(0,1,0,0),(0,0,-1,0),(0,0,1,0),(0,0,0,-1),(0,0,0,1)
        ]

        while queue:
            for _ in range(len(queue)):
                combo = queue.popleft()
                if combo == target_combo:
                    return iterations
                
                visited.add(combo)

                for direction in adjacent_directions:
                    adjacent_combo = tuple((digit + digit_offset) % 10 for digit, digit_offset in zip(combo, direction))
                    if (adjacent_combo not in visited) and (adjacent_combo not in deadends_set):
                        # if :
                        #     print('skipped')
                        #     continue
                        queue.append(adjacent_combo)
                        visited.add(adjacent_combo)
                
            iterations += 1
            
        return -1
        