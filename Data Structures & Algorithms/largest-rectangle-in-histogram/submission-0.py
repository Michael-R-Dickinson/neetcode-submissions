class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)

        stack = []
        left_smaller = [-1] * n
        for i, height in enumerate(heights):
            while stack and height <= heights[stack[-1]]:
                # if height is less than the previous decreasing elements
                # pop until its greater
                stack.pop()
            # add height's index to the stack as it represents the 
            # next index of a dropoff in height
                
            if stack:
                left_smaller[i] = stack[-1]
            stack.append(i)
        
        stack = []
        right_smaller = [n] * n
        for i in range(n - 1, -1, -1):
            height = heights[i]
            while stack  and height <= heights[stack[-1]]:
                stack.pop()
            if stack:
                right_smaller[i] = stack[-1]
            stack.append(i)
        
        max_area = 0
        for left, right, height in zip(left_smaller, right_smaller, heights):
            width = right - left - 1
            area = width * height

            max_area = max(max_area, area)

        return max_area
            
                


