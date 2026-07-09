# [1 2 3 4 5 6]
# [6]
# [1 2 3 4 5 ]
from collections import deque

class MyStack:
    def __init__(self):
        self.q1 = deque()
        self.q2 = deque()
        self.active = 1

    def push(self, x: int) -> None:
        self._get_primary().append(x)

    def pop(self) -> int:
        # drain active queue (except last element) into other queue
        primary = self._get_primary()
        secondary = self._get_secondary()
        for i in range(len(primary) - 1):
            secondary.append(
                primary.popleft()
            )
        out = primary.popleft()
        self._switch_queues()
        return out

    def top(self) -> int:
        # drain active queue (except last element) into other queue
        primary = self._get_primary()
        secondary = self._get_secondary()
        for i in range(len(primary) - 1):
            secondary.append(
                primary.popleft()
            )
        out = primary.popleft()
        secondary.append(out)
        self._switch_queues()
        return out

    def empty(self) -> bool:
        primary = self._get_primary()
        return len(primary) == 0
    def _get_primary(self):
        if self.active == 1:
            return self.q1
        else:
            return self.q2
    def _get_secondary(self):
        if self.active == 1:
            return self.q2
        else:
            return self.q1
    
    def _switch_queues(self):
        self.active = 2 if self.active == 1 else 1



# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()