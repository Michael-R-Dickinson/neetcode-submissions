class Solution:
    def isValid(self, s: str) -> bool:
        opposite_brackets = {
            "(": ")",
            "{": "}",
            "[": "]"
        }

        stack = []
        for bracket in s:
            top = stack[-1] if len(stack) > 0 else ""
            # Check if bracket is a closing bracket
            # if it is, it must close the top of the stack
            # If its an opening bracket, add it to the stack
            is_closing = opposite_brackets.get(bracket, None) == None
            if (is_closing):
                if (bracket != opposite_brackets.get(top)):
                    return False
                stack.pop()
            else:
                stack.append(bracket)
        
        if len(stack) != 0:
            return False

        return True
        
                