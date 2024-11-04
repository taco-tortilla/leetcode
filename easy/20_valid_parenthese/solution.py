from typing import List


class Solution:
    def isValid(self, s: str) -> bool:
        BRACKETS = {")": "(", "}": "{", "]": "["}
        stack = []

        for x in s:
            if x in BRACKETS:
                if len(stack) == 0 or stack.pop() != BRACKETS[x]:
                    return False
            else:
                stack.append(x)

        return len(stack) == 0
