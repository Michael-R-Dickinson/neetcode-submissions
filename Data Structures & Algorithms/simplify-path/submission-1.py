# storing the current path
# FIFO -> stack
# "/neetcode/practice//...///../courses"
# neetcode, practice, courses

# trim leading slash
# slash handling - once we see one, traverse until there are no more - then continue
# dot handling - traverse until we have a count, then apply the releavnt operation - go back, stay there, add subdir to stack

# Note: need to handle trying to go back even when at the root -> popping when the stack is empty

class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        for segment in path.split("/"):
            if segment == "":
                continue

            numDots = 0
            while numDots < len(segment) and segment[numDots] == ".":
                numDots += 1
            only_dots = numDots == len(segment)

            if only_dots and numDots == 1:
                continue
            elif only_dots and numDots == 2:
                if not stack:
                    continue
                stack.pop()
            else:
                # normal path segment, or 3 or more dots (also a normal path segment)
                stack.append(segment)

        return "/" + "/".join(stack)
