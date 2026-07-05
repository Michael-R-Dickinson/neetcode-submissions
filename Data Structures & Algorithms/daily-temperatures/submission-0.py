class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # stack - INVARIANT: top element on the stack has the lowest temp
        # initalization: make sure that when theres nothing in the stack, its temp value = -inf
        # for any new value:
        #   if its greater than the top of the stack:
        #       assign the top of the stack's output next-temp to that idx
        #       pop that from the stack
        #    add the new value to the stack
        #  if we run out of elements - value = 0

        result = [0] * len(temperatures)
        stack = []
        for temp_idx, temp in enumerate(temperatures):
            while (len(stack) > 0 and temp > stack[-1][0]):
                stack_top_val, stack_top_idx = stack[-1]

                result[stack_top_idx] = temp_idx - stack_top_idx 
                stack.pop()

            stack.append((temp, temp_idx))
        
        return result
            