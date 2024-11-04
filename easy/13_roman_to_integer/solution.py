class Solution:
    def romanToInt(self, s: str) -> int:
        SYMBOL = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        result = 0
        for i in range(len(s)):
            if i < len(s) - 1 and SYMBOL[s[i]] < SYMBOL[s[i + 1]]:
                result -= SYMBOL[s[i]]
            else:
                result += SYMBOL[s[i]]
        return result
