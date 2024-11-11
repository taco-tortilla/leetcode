from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_num = 0
        min_num = 1000000
        for i in prices:
            min_num = min(min_num, i)
            max_num = max(max_num, i - min_num)
        return max_num
