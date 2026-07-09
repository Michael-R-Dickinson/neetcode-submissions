# [80 60 70 60 75 85 70]
# Invariant: some data structure stores the peaks of prices walking backwards through the list
#            - elements > all future elements up to the current day

# for a new day:
# walk backwards through the structure until we find a value > the current: current_day - that_elements_day
# - each element we "walk" through gets popped from the stack 
# - at the end, add the current day's value to the top of the stack
# - need to keep track of the day that each value in the structure was added

# Note: if we reach the end of the stack - thats idx -1

class StockSpanner:
    def __init__(self):
        # stack with invariant
        self.mstack = []
        # each element corresponds to the same idx in mstack - gives the day that price occoured
        self.mstack_corresponding_days = []
        self.day_idx = 0

    def next(self, price: int) -> int:
        while self.mstack and self.mstack[-1] <= price:
            self.mstack.pop()
            self.mstack_corresponding_days.pop()

        if self.mstack:
            day_ending_span = self.mstack_corresponding_days[-1]
        else:
            # empty stack - stock spans until the beginning of time
            day_ending_span = -1
        
        self.mstack.append(price)
        self.mstack_corresponding_days.append(self.day_idx)

        span = self.day_idx - day_ending_span

        self.day_idx += 1

        return span


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)