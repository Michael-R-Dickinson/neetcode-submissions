'''
compute in-degree for all courses
compute an adjacency list for all courses

create an order list which is the topological traversal order
enqueue nodes with in-degree = 0
BFS:
- for each item in the queue, pop - add to order list
- reduce the in_degree of all adjacents
- for those where in_degree == 0: add them to the queue

If len(order) = numCourses: then all courses are traversable
'''

from collections import deque


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        in_degree = [0] * numCourses
        adjacency = [[] for i in range(numCourses)]
        for course, prereq in prerequisites:
            adjacency[prereq].append(course)
            in_degree[course] += 1
        
        print(in_degree)
        print(adjacency)
        order = []
        queue = deque()
        for course, deg in enumerate(in_degree):
            if deg == 0:
                queue.append(course)

        while queue:
            course = queue.popleft()
            order.append(course)
            for adjacent in adjacency[course]:
                in_degree[adjacent] -= 1
                if in_degree[adjacent] == 0:
                    queue.append(adjacent)

        print(order)
        return len(order) == numCourses

            

