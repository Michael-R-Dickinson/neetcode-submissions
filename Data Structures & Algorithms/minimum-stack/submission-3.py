class MinStack:
    def __init__(self):
        self.stack = []
        self.minElements = []

    def push(self, val: int) -> None:
        # if this element is less than the current min element
        # add it to the minElements array
        # else, add a repeat of the previous min element
        # stack empty? add this element

        if not self.stack or val < self.minElements[-1]:
            self.minElements.append(val)
        else:
            self.minElements.append(self.minElements[-1])
        self.stack.append(val)

    def pop(self) -> None:
        # just pop from both stack and minElement - minElement keeps track of the min at any time in the stack
        # so popping from it keeps it in sync with the stack
        self.stack.pop()
        self.minElements.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minElements[-1]
        
